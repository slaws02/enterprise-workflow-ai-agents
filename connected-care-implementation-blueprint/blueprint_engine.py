from typing import List
from models import Action, BlueprintAssessment, Decision, DeviceCheck, Requirement

def _requirements(crm, contract) -> List[Requirement]:
    return [
        Requirement("Eligibility","Eligible population",contract["eligible_population"],"Population must be explicitly confirmed before configuration and billing.","Needs Decision" if crm["eligible_population"] != contract["eligible_population"] else "Confirmed","Client + Implementation","CRM + Contract"),
        Requirement("Eligibility","Medical plan population",", ".join(contract["medical_plan_population"]),"Each included plan requires a validated eligibility mapping.","Confirmed" if crm["medical_plan_population"] == contract["medical_plan_population"] else "Needs Review","Implementation","CRM + Contract"),
        Requirement("Connected Devices","Device bundle",", ".join(contract["device_bundle"]),"Contracted devices must map to eligibility, fulfillment, activation, and support workflows.","Needs Decision" if set(crm["device_bundle"]) != set(contract["device_bundle"]) else "Confirmed","Implementation + Operations","CRM + Contract"),
        Requirement("Member App","App + device pairing",contract["member_app"],"App configuration and device-pairing workflow must be validated before launch.","Confirmed","Product Operations","Contract"),
        Requirement("Communications","Communication ownership",contract["communication_owner"],"One accountable communication owner and approval path is required.","Needs Decision" if crm["communication_owner"] != contract["communication_owner"] else "Confirmed","Client + Communications","CRM + Contract + Meeting Notes"),
        Requirement("Data Integration","Eligibility file cadence",contract["eligibility_file_cadence"],"Eligibility cadence and file specification must be approved and tested.","Confirmed" if crm["eligibility_file_cadence"] == contract["eligibility_file_cadence"] else "Needs Review","Technical Integration","CRM + Contract"),
        Requirement("Reporting","Implementation and engagement reporting",contract["reporting"],"Reporting scope, segmentation, frequency, and delivery method must be confirmed.","Needs Review" if crm["reporting"] != contract["reporting"] else "Confirmed","Analytics + Client","CRM + Contract"),
        Requirement("Support","Connected-device support",contract["support"],"Pairing, sync, replacement, and escalation support paths must be documented.","Needs Review","Member Support","Contract + Collaboration"),
        Requirement("Billing","Billing model",crm["billing_model"],"Billing setup depends on final eligible population and launch configuration.","Confirmed","Billing Operations","CRM")]

def _decisions(crm, contract):
    decisions=[]
    if crm["eligible_population"] != contract["eligible_population"]:
        decisions.append(Decision("Resolve eligible population conflict",f"CRM lists '{crm['eligible_population']}' while the contract lists '{contract['eligible_population']}'.",["CRM: eligible population","Contract: eligible population","Meeting: sponsor confirmation pending"],"Are spouses included in the initial launch population or deferred to a later phase?","Client Sponsor + Implementation","High"))
    if set(crm["device_bundle"]) != set(contract["device_bundle"]):
        decisions.append(Decision("Confirm contracted device bundle","The CRM reflects a blood-pressure monitor only, while the contract includes a monitor and smart scale.",["CRM: device bundle","Contract: connected-device bundle","Decision log: scale pending fulfillment mapping"],"Which members should receive the smart scale, and is it required for the initial launch?","Program Sponsor + Operations","High"))
    if crm["communication_owner"] != contract["communication_owner"]:
        decisions.append(Decision("Confirm member communication owner","Sources disagree about whether the program delivery team or client benefits team sends launch communications.",["CRM: program delivery team","Contract: client benefits team","Meeting notes: client expects to send"],"Who owns final distribution, approval, and timing of member launch communications?","Client Benefits Lead + Communications","Medium"))
    if crm["reporting"] != contract["reporting"]:
        decisions.append(Decision("Define connected-device reporting detail","The contract requires activation and device-engagement reporting beyond the CRM's utilization summary.",["CRM: monthly utilization","Contract: activation + connected-device engagement","Meeting: device-level breakout pending"],"Should engagement be reported separately for blood-pressure monitors and smart scales?","Analytics + Client","Medium"))
    return decisions

def _actions():
    return [
        Action("Confirm spouse inclusion in initial eligibility","Client Sponsor","2026-09-10","Working session"),
        Action("Send device shipping-address template","Implementation Lead","2026-09-08","Working session"),
        Action("Provide test member IDs and sample device readings","Technical Integration","2026-09-09","Working session"),
        Action("Confirm launch communication ownership and approval path","Client Benefits Lead","2026-09-10","Working session"),
        Action("Document device pairing, sync-failure, and replacement escalation path","Member Support Lead","2026-09-15","Working session"),
        Action("Confirm reporting breakout by device type","Reporting Owner","2026-09-12","Working session")]

def _device_checks(tasks, resolved=False):
    by={t["task"]:t for t in tasks}; f=by["Approve device fulfillment file specification"]; s=by["Complete test device shipment"]; d=by["Validate connected-device readings ingestion"]
    return [
        DeviceCheck("Eligibility","Needs Decision","Final population is not yet reconciled across sources.","Client + Implementation"),
        DeviceCheck("Device kit assignment","Needs Decision","Blood-pressure monitor vs. monitor + smart scale bundle is inconsistent across sources.","Program Sponsor + Operations"),
        DeviceCheck("Shipping address validation","In Progress",f["dependency"],"Client + Operations"),
        DeviceCheck("Fulfillment file",f["status"],"File specification must be approved before test shipment.",f["owner"]),
        DeviceCheck("Test shipment",s["status"],s["dependency"],s["owner"]),
        DeviceCheck("Member app configuration","Ready","Mobile app tenant configuration is complete.","Product Operations"),
        DeviceCheck("Device pairing support","Needs Review","Pairing escalation path is not yet documented.","Member Support"),
        DeviceCheck("Readings data sync","Ready" if resolved else d["status"],"Sample device readings received and validation passed." if resolved else d["dependency"],d["owner"]),
        DeviceCheck("Replacement process","Needs Review","Replacement ownership and service-level expectations need documentation.","Operations + Member Support")]

def _dependencies(tasks):
    return [{"dependency":t["dependency"],"task":t["task"],"owner":t["owner"],"status":t["status"]} for t in tasks if t.get("dependency")]

def _pct(values):
    return 0 if not values else round(100*sum(v in {"Confirmed","Complete","Ready"} for v in values)/len(values))

def _readiness(reqs, devices, tasks, resolved=False):
    rb={}; tb={}
    for r in reqs: rb.setdefault(r.domain,[]).append(r.status)
    for t in tasks: tb.setdefault(t["domain"],[]).append(t["status"])
    return {"Eligibility":_pct(rb.get("Eligibility",[])),"Connected Devices":_pct([d.status for d in devices]),"Member App":100,"Data Integration":100 if resolved else _pct(tb.get("Data Integration",[])),"Communications":_pct(rb.get("Communications",[])+tb.get("Communications",[])),"Support":_pct(rb.get("Support",[])),"Reporting":_pct(rb.get("Reporting",[])),"Billing":_pct(rb.get("Billing",[])+tb.get("Billing",[])),"Launch Readiness":_pct(tb.get("Launch",[]))}

def _blockers(tasks,resolved=False):
    return [f"{t['task']}: {t['dependency']}" for t in tasks if t["status"]=="Blocked" and not (resolved and t["task"]=="Validate connected-device readings ingestion")]

def _memory(messages, notes, decision_log):
    memory=list(decision_log)+[{"date":m["date"],"decision":m["message"],"source":f"Collaboration / {m['team']}","owner":m["author"]} for m in messages]
    memory.append({"date":notes["meeting_date"],"decision":"Client sponsor to confirm spouse inclusion; communication ownership and device support escalation remain open.","source":notes["meeting"],"owner":"Implementation"})
    return sorted(memory,key=lambda x:x["date"])

def query_memory(query,memory):
    q=(query or "").lower().strip()
    if not q: return "Enter a question about eligibility, devices, communications, support, or reporting."
    words=[w for w in q.replace("?","").split() if len(w)>3]; matches=[]
    for row in memory:
        hay=" ".join(str(v) for v in row.values()).lower(); score=sum(k in hay for k in words)
        if score: matches.append((score,row))
    matches.sort(key=lambda x:(-x[0],x[1]["date"]))
    if not matches: return "No supporting implementation-memory evidence was found in the synthetic sources."
    return "Relevant implementation memory:\n"+"\n".join(f"- {r['date']}: {r['decision']} (Source: {r['source']}; Owner: {r['owner']})" for _,r in matches[:3])

def build_blueprint(crm,contract,tasks,messages,notes,standard,decision_log,resolved_device_feed=False):
    reqs=_requirements(crm,contract); devices=_device_checks(tasks,resolved_device_feed)
    return BlueprintAssessment(client=crm["client_name"],program=crm["program"],launch_date=crm["launch_date"],requirements=reqs,decisions=_decisions(crm,contract),actions=_actions(),device_checks=devices,dependencies=_dependencies(tasks),blockers=_blockers(tasks,resolved_device_feed),readiness_by_domain=_readiness(reqs,devices,tasks,resolved_device_feed),memory=_memory(messages,notes,decision_log))
