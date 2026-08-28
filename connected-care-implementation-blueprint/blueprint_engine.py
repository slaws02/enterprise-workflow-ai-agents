from typing import List
from models import Action, BlueprintAssessment, Decision, DeviceCheck, Requirement


def _requirements(crm, contract) -> List[Requirement]:
    return [
        Requirement("Employer Scope", "Benefit model", contract["benefit_model"], "The employer's contracted benefit model must be confirmed before launch planning.", "Confirmed" if crm["benefit_model"] == contract["benefit_model"] else "Needs Review", "Client Benefits + Implementation", "CRM + Contract"),
        Requirement("Eligibility", "Eligible workforce", contract["eligible_population"], "The employer must define exactly which employees or spouses are eligible before files, billing, communications, and enrollment can be configured.", "Needs Decision" if crm["eligible_population"] != contract["eligible_population"] else "Confirmed", "Client Benefits + Implementation", "CRM + Contract"),
        Requirement("Eligibility", "Eligibility groups", ", ".join(contract["eligibility_groups"]), "Eligibility groups drive file mapping and determine who can opt into the program.", "Needs Review" if crm["eligibility_groups"] != contract["eligibility_groups"] else "Confirmed", "Implementation + Technical Integration", "CRM + Contract"),
        Requirement("Program Configuration", "Member experience", contract["member_app"], "The employer program tenant must be configured so enrolled members can access the app and connected services after opt-in.", "Confirmed", "Product Operations", "Contract"),
        Requirement("Communications", "Employee launch communications", contract["communication_owner"], "The employer and program provider need one approved distribution and approval path for benefit-launch communications.", "Needs Decision" if crm["communication_owner"] != contract["communication_owner"] else "Confirmed", "Client Benefits + Communications", "CRM + Contract + Meeting Notes"),
        Requirement("Data Integration", "Eligibility file cadence", contract["eligibility_file_cadence"], "Employer eligibility data must be approved and tested before employees can be validated for enrollment.", "Confirmed" if crm["eligibility_file_cadence"] == contract["eligibility_file_cadence"] else "Needs Review", "Technical Integration", "CRM + Contract"),
        Requirement("Devices", "Post-enrollment device bundle", ", ".join(contract["device_bundle"]), "Devices are a downstream member experience: contracted device rules must map from employer eligibility to member enrollment, fulfillment, activation, and support.", "Needs Decision" if set(crm["device_bundle"]) != set(contract["device_bundle"]) else "Confirmed", "Implementation + Operations", "CRM + Contract"),
        Requirement("Reporting", "Employer reporting", contract["reporting"], "The employer's reporting package should distinguish eligible population, enrollment, activation, and engagement measures.", "Needs Review" if crm["reporting"] != contract["reporting"] else "Confirmed", "Analytics + Client Benefits", "CRM + Contract"),
        Requirement("Support", "Enrolled-member support", contract["support"], "Support processes begin after enrollment and must cover app/device setup, pairing, sync, replacement, and escalation.", "Needs Review", "Member Support", "Contract + Collaboration"),
        Requirement("Billing", "Client billing model", crm["billing_model"], "Billing setup depends on the final contracted employer population and billing basis.", "Confirmed", "Billing Operations", "CRM"),
    ]


def _decisions(crm, contract):
    decisions = []
    if crm["eligible_population"] != contract["eligible_population"]:
        decisions.append(Decision("Resolve employer eligibility scope", f"CRM lists '{crm['eligible_population']}' while the contract lists '{contract['eligible_population']}'.", ["CRM: employer eligible population", "Contract: employer eligible population", "Meeting: sponsor confirmation pending"], "Are spouses included in the initial employer launch, or is Phase 1 limited to employees?", "Client Benefits Sponsor + Implementation", "High"))
    if set(crm["device_bundle"]) != set(contract["device_bundle"]):
        decisions.append(Decision("Confirm post-enrollment device benefit", "The employer-facing CRM reflects a blood-pressure monitor only, while the contract includes a monitor and smart scale for enrolled members.", ["CRM: device benefit", "Contract: enrolled-member device bundle", "Decision log: scale fulfillment mapping pending"], "Which enrolled members should receive the smart scale, and must that fulfillment path be launch-ready on day one?", "Client Benefits Sponsor + Operations", "High"))
    if crm["communication_owner"] != contract["communication_owner"]:
        decisions.append(Decision("Confirm employee communication ownership", "Sources disagree about whether the program provider or the employer benefits team distributes launch communications.", ["CRM: program delivery team", "Contract: client benefits team", "Meeting notes: employer expects to send"], "Who owns final approval, distribution, and timing of employee benefit-launch communications?", "Client Benefits Lead + Communications", "Medium"))
    if crm["reporting"] != contract["reporting"]:
        decisions.append(Decision("Define employer reporting package", "The contract requires enrollment, activation, and connected-device engagement reporting beyond the CRM's utilization summary.", ["CRM: monthly utilization", "Contract: enrollment + activation + device engagement", "Meeting: reporting breakout pending"], "Which employer-level and enrolled-member metrics must be included in the launch and ongoing reporting package?", "Analytics + Client Benefits", "Medium"))
    return decisions


def _actions():
    return [
        Action("Confirm employer eligibility scope for employees and spouses", "Client Benefits Sponsor", "2026-09-10", "Working session"),
        Action("Approve employer eligibility-file fields and group definitions", "Technical Integration", "2026-09-14", "Working session"),
        Action("Confirm employee launch communication ownership and approval path", "Client Benefits Lead", "2026-09-10", "Working session"),
        Action("Approve enrolled-member shipping-address collection workflow", "Client Benefits + Operations", "2026-09-12", "Working session"),
        Action("Provide sample enrolled-member IDs and device readings", "Technical Integration", "2026-09-18", "Working session"),
        Action("Document device pairing, sync-failure, and replacement escalation path", "Member Support Lead", "2026-09-15", "Working session"),
        Action("Confirm employer reporting metrics and device-engagement breakout", "Reporting Owner", "2026-09-12", "Working session"),
    ]


def _device_checks(tasks, resolved=False):
    by = {t["task"]: t for t in tasks}
    f = by["Approve device fulfillment file specification"]
    s = by["Complete enrolled-member test device shipment"]
    d = by["Validate connected-device readings ingestion"]
    return [
        DeviceCheck("Employer eligibility prerequisite", "Needs Decision", "Final employer eligibility scope is not reconciled across sources.", "Client Benefits + Implementation"),
        DeviceCheck("Member enrollment prerequisite", "In Progress", "Only employees/spouses who are eligible and opt in become members eligible for the downstream device experience.", "Implementation"),
        DeviceCheck("Device kit assignment", "Needs Decision", "Blood-pressure monitor vs. monitor + smart scale bundle is inconsistent across employer implementation sources.", "Client Benefits Sponsor + Operations"),
        DeviceCheck("Shipping address collection", "In Progress", f["dependency"], "Client Benefits + Operations"),
        DeviceCheck("Fulfillment file", f["status"], "File specification must be approved before an enrolled-member test shipment.", f["owner"]),
        DeviceCheck("Test shipment", s["status"], s["dependency"], s["owner"]),
        DeviceCheck("Member app access", "Ready", "Employer program tenant configuration is complete; access occurs after an eligible employee opts in.", "Product Operations"),
        DeviceCheck("Device pairing support", "Needs Review", "Pairing escalation path is not yet documented.", "Member Support"),
        DeviceCheck("Readings data sync", "Ready" if resolved else d["status"], "Sample enrolled-member device readings received and validation passed." if resolved else d["dependency"], d["owner"]),
        DeviceCheck("Replacement process", "Needs Review", "Replacement ownership and service-level expectations need documentation before member support go-live.", "Operations + Member Support"),
    ]


def _dependencies(tasks):
    return [{"dependency": t["dependency"], "task": t["task"], "owner": t["owner"], "status": t["status"]} for t in tasks if t.get("dependency")]


def _pct(values):
    return 0 if not values else round(100 * sum(v in {"Confirmed", "Complete", "Ready"} for v in values) / len(values))


def _readiness(reqs, devices, tasks, resolved=False):
    rb, tb = {}, {}
    for r in reqs:
        rb.setdefault(r.domain, []).append(r.status)
    for t in tasks:
        tb.setdefault(t["domain"], []).append(t["status"])
    return {
        "Employer Scope": _pct(rb.get("Employer Scope", [])),
        "Eligibility & Data": _pct(rb.get("Eligibility", []) + rb.get("Data Integration", []) + tb.get("Eligibility", []) + tb.get("Data Integration", [])),
        "Program Configuration": _pct(rb.get("Program Configuration", []) + tb.get("Program Configuration", [])),
        "Employee Communications": _pct(rb.get("Communications", []) + tb.get("Communications", [])),
        "Member & Device Enablement": _pct([d.status for d in devices]),
        "Reporting": _pct(rb.get("Reporting", []) + tb.get("Reporting", [])),
        "Billing": _pct(rb.get("Billing", []) + tb.get("Billing", [])),
        "Employer Launch Readiness": _pct(tb.get("Launch", [])),
    }


def _blockers(tasks, resolved=False):
    return [f"{t['task']}: {t['dependency']}" for t in tasks if t["status"] == "Blocked" and not (resolved and t["task"] == "Validate connected-device readings ingestion")]


def _memory(messages, notes, decision_log):
    memory = list(decision_log) + [{"date": m["date"], "decision": m["message"], "source": f"Collaboration / {m['team']}", "owner": m["author"]} for m in messages]
    memory.append({"date": notes["meeting_date"], "decision": "Employer sponsor to confirm eligibility scope; employee communications ownership and downstream member device support remain open.", "source": notes["meeting"], "owner": "Implementation"})
    return sorted(memory, key=lambda x: x["date"])


def query_memory(query, memory):
    q = (query or "").lower().strip()
    if not q:
        return "Enter a question about employer eligibility, communications, enrollment, devices, support, reporting, or launch decisions."
    words = [w for w in q.replace("?", "").split() if len(w) > 3]
    matches = []
    for row in memory:
        hay = " ".join(str(v) for v in row.values()).lower()
        score = sum(k in hay for k in words)
        if score:
            matches.append((score, row))
    matches.sort(key=lambda x: (-x[0], x[1]["date"]))
    if not matches:
        return "No supporting implementation-memory evidence was found in the synthetic sources."
    return "Relevant implementation memory:\n" + "\n".join(f"- {r['date']}: {r['decision']} (Source: {r['source']}; Owner: {r['owner']})" for _, r in matches[:3])


def build_blueprint(crm, contract, tasks, messages, notes, standard, decision_log, resolved_device_feed=False):
    reqs = _requirements(crm, contract)
    devices = _device_checks(tasks, resolved_device_feed)
    return BlueprintAssessment(client=crm["client_name"], program=crm["program"], launch_date=crm["launch_date"], requirements=reqs, decisions=_decisions(crm, contract), actions=_actions(), device_checks=devices, dependencies=_dependencies(tasks), blockers=_blockers(tasks, resolved_device_feed), readiness_by_domain=_readiness(reqs, devices, tasks, resolved_device_feed), memory=_memory(messages, notes, decision_log))
