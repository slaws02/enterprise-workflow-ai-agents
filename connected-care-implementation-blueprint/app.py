import pandas as pd
import streamlit as st
from blueprint_engine import build_blueprint, query_memory
from connectors import get_collaboration_messages, get_contract_requirements, get_crm_record, get_decision_log, get_implementation_standard, get_meeting_notes, get_project_tasks

st.set_page_config(page_title="Employer Connected-Care Implementation Blueprint", page_icon="🧭", layout="wide")
st.title("Employer Connected-Care Implementation Blueprint")
st.caption("Portfolio demonstration of a multi-source implementation workflow for a fictional employer-sponsored connected-health benefit.")
st.info("Synthetic demo only — all organizations, employees, members, requirements, device workflows, dates, and source records are fictional. This demo does not represent any real healthcare, insurance, employer, or technology company.")

with st.sidebar:
    st.header("Demo Controls")
    assessment_date = st.date_input("Assessment date", value=pd.to_datetime("2026-09-07"))
    resolved_device_feed = st.toggle("Simulate device data issue resolved", value=False, help="Shows how one downstream member/device dependency changes without changing the employer's other launch requirements.")
    st.divider()
    st.markdown("**Implementation hierarchy**")
    st.caption("Program Provider → Employer Client → Eligible Employees → Opt-in Members → App / Devices / Program Participation")
    st.divider()
    st.markdown("**Workflow**")
    st.caption("Ingest → Reconcile → Detect ambiguity → Generate actions → Assess employer launch readiness → Preserve implementation memory")

crm=get_crm_record(); contract=get_contract_requirements(); tasks=get_project_tasks(); messages=get_collaboration_messages(); notes=get_meeting_notes(); standard=get_implementation_standard(); decision_log=get_decision_log()
assessment=build_blueprint(crm,contract,tasks,messages,notes,standard,decision_log,resolved_device_feed=resolved_device_feed)

st.markdown(f"### {assessment.client} — {assessment.program}")
st.caption("Implementation customer: employer client. Eligible employees may opt into the benefit after the employer implementation is launch-ready.")

m1,m2,m3,m4=st.columns(4)
m1.metric("Requirements Confirmed",f"{assessment.requirements_complete_pct}%")
m2.metric("Open Decisions",len(assessment.decisions))
m3.metric("Cross-Functional Dependencies",len(assessment.dependencies))
m4.metric("Launch Blockers",len(assessment.blockers))

p1,p2,p3,p4=st.columns(4)
p1.metric("Eligible Employees",f"{crm['estimated_eligible_employees']:,}")
p2.metric("Expected Opt-in Members",f"{crm['expected_enrolled_members']:,}")
p3.metric("Benefit Model",crm['benefit_model'])
p4.metric("Target Launch",assessment.launch_date)

st.markdown(f"**Assessment date:** {assessment_date}")
if assessment.blockers: st.error("Employer launch readiness has unresolved blockers. The agent recommends action; final decisions remain human-owned.")
else: st.success("No blocking tasks remain in the simulated scenario. Human employer launch-readiness approval is still required.")

blueprint_tab,decisions_tab,actions_tab,devices_tab,readiness_tab,memory_tab,evidence_tab=st.tabs(["Employer Blueprint","Decisions","Actions","Member & Device Enablement","Employer Launch Readiness","Implementation Memory","Evidence"])

with blueprint_tab:
    st.subheader("Employer Implementation Requirements")
    st.caption("Primary focus: what must be configured, approved, tested, and communicated so the employer can launch the benefit to its workforce.")
    st.dataframe(pd.DataFrame([r.__dict__ for r in assessment.requirements]),use_container_width=True,hide_index=True)

with decisions_tab:
    st.subheader("Employer Implementation Decisions Required")
    for i,d in enumerate(assessment.decisions,1):
        with st.expander(f"{i}. [{d.severity}] {d.title}",expanded=(i<=2)):
            st.write(d.issue); st.markdown("**Evidence**")
            for e in d.evidence: st.write(f"- {e}")
            st.markdown(f"**Question to resolve:** {d.recommended_question}"); st.markdown(f"**Suggested owner:** {d.owner}")

with actions_tab:
    st.subheader("Implementation Action Extraction")
    st.caption("Structured employer-launch follow-up generated from the synthetic implementation working session.")
    st.dataframe(pd.DataFrame([a.__dict__ for a in assessment.actions]),use_container_width=True,hide_index=True)
    st.markdown("**Example downstream action:** Reviewed rows could be pushed to an approved project-management connector.")

with devices_tab:
    st.subheader("Downstream Member & Connected-Device Enablement")
    st.caption("Devices are not the implementation customer. They are part of the member experience that must be operationally ready once eligible employees opt into the employer-sponsored benefit.")
    st.markdown("**Employer implementation → Eligible employee → Opt-in member → App access → Device fulfillment → Pairing → Readings sync → Support**")
    st.dataframe(pd.DataFrame([d.__dict__ for d in assessment.device_checks]),use_container_width=True,hide_index=True)
    if resolved_device_feed: st.success("Simulation: sample enrolled-member device readings were received and data-ingestion validation passed. Other employer launch dependencies remain unchanged.")
    else: st.warning("Current downstream blocker: sample enrolled-member IDs and connected-device readings have not been received for ingestion validation.")

with readiness_tab:
    st.subheader("Employer Launch Readiness by Domain")
    st.caption("The top-level question is whether the employer client is ready to launch the benefit to eligible employees.")
    ready_df=pd.DataFrame([{"domain":k,"readiness_pct":v} for k,v in assessment.readiness_by_domain.items()])
    st.bar_chart(ready_df.set_index("domain")); st.dataframe(ready_df,use_container_width=True,hide_index=True)
    st.markdown("#### Current blockers")
    for blocker in assessment.blockers: st.write(f"- {blocker}")

with memory_tab:
    st.subheader("Implementation Memory")
    st.caption("Ask why an employer implementation requirement or downstream member decision exists without manually searching every source system.")
    q=st.text_input("Ask the implementation memory",value="Why is the smart scale still an open implementation issue?")
    st.markdown(query_memory(q,assessment.memory))
    with st.expander("View synthetic decision timeline"): st.dataframe(pd.DataFrame(assessment.memory),use_container_width=True,hide_index=True)

with evidence_tab:
    st.subheader("Cross-System Evidence")
    e1,e2,e3,e4,e5,e6=st.tabs(["CRM","Contract","Project Tracker","Collaboration","Meeting Notes","Implementation Standard"])
    with e1: st.json(crm)
    with e2: st.json(contract)
    with e3: st.dataframe(pd.DataFrame(tasks),use_container_width=True,hide_index=True)
    with e4: st.dataframe(pd.DataFrame(messages),use_container_width=True,hide_index=True)
    with e5: st.json(notes)
    with e6: st.json(standard)

st.divider()
st.caption("Human-in-the-loop guardrail: the agent reconciles employer implementation evidence, recommends questions and actions, and assesses readiness. It does not decide eligibility, enroll employees, change launch dates, ship devices, contact members, or modify source systems autonomously.")
