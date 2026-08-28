import pandas as pd
import streamlit as st
from assurance_engine import assess_assurance, apply_resolution
from connectors import get_client, get_journey_tests

st.set_page_config(page_title="Implementation Assurance Agent", page_icon="🛡️", layout="wide")
st.title("Implementation Assurance Agent")
st.caption("Pre-launch assurance for a fictional employer-sponsored connected-health benefit.")
st.info("Synthetic demo only — all employers, employees, members, requirements, test populations, devices, dates, and results are fictional. This demo does not represent any real healthcare, insurance, employer, device, or technology company.")

client=get_client(); base_rows=get_journey_tests()

with st.sidebar:
    st.header("Assurance Simulation")
    resolution=st.selectbox("Simulate a remediation", ["None","Eligibility identity matching","Device entitlement","Readings ingestion"])
    st.divider()
    st.markdown("**Implementation hierarchy**")
    st.caption("Program Provider → Employer Client → Eligible Employees → Opt-in Members → App / Devices / Program Participation")
    st.divider()
    st.markdown("**Assurance question**")
    st.caption("If this employer launches as configured, will eligible employees who opt in successfully move through the member journey?")

rows=apply_resolution(base_rows,resolution) if resolution!="None" else base_rows
assessment=assess_assurance(client,rows)

st.markdown(f"### {assessment.client} — {assessment.program}")
st.caption("Implementation customer: employer client. Assurance tests validate the downstream experience before employees are invited to enroll.")

c1,c2,c3,c4=st.columns(4)
c1.metric("Member Journey Assurance",f"{assessment.assurance_score}%")
c2.metric("Synthetic Tests",assessment.tested_scenarios)
c3.metric("Failed Tests",assessment.failed_scenarios)
c4.metric("Largest Affected Population",f"{assessment.affected_estimate:,}")

if assessment.launch_recommendation.startswith("HOLD"):
    st.error(assessment.launch_recommendation)
elif assessment.launch_recommendation.startswith("CONDITIONAL"):
    st.warning(assessment.launch_recommendation)
else:
    st.success(assessment.launch_recommendation)

st.markdown("#### What the agent found")
if assessment.alerts:
    top=assessment.alerts[:3]
    cols=st.columns(len(top))
    for col,alert in zip(cols,top):
        with col:
            st.markdown(f"**{alert.severity}: {alert.title}**")
            st.write(f"Estimated affected: **{alert.affected_estimate:,}**")
            st.caption(alert.member_impact)
else:
    st.success("No assurance gaps detected in the synthetic test journey.")

st.markdown("#### What the agent did")
st.write("Compared pre-launch test outcomes across eligibility, enrollment, device entitlement, fulfillment, app activation, pairing, data ingestion, and support readiness; estimated downstream population impact; preserved evidence; and recommended human-owned remediation before employer launch approval.")

journey_tab,alerts_tab,domains_tab,scenario_tab,evidence_tab=st.tabs(["Member Journey Assurance","Assurance Alerts","Domain Scores","What-if Simulation","Test Evidence"])

with journey_tab:
    st.subheader("End-to-End Member Journey")
    st.caption("The implementation is tested from the employee's perspective before launch. A project can be operationally 'on track' while the member journey still contains preventable failures.")
    df=pd.DataFrame([x.__dict__ for x in assessment.journey])
    st.dataframe(df[["step","domain","status","pass_rate","tested","failed","affected_estimate","owner"]],use_container_width=True,hide_index=True)
    st.markdown("**Journey:** Employer launch → Eligibility match → Employee opt-in → Account creation → Device entitlement → Fulfillment → App activation → Pairing → Readings sync → Support")

with alerts_tab:
    st.subheader("Pre-Launch Assurance Alerts")
    if not assessment.alerts:
        st.success("No open assurance alerts in this simulation.")
    for i,a in enumerate(assessment.alerts,1):
        with st.expander(f"{i}. [{a.severity}] {a.title} — ~{a.affected_estimate:,} potentially affected",expanded=(i<=2)):
            st.markdown(f"**Root cause:** {a.root_cause}")
            st.markdown(f"**Employer impact:** {a.employer_impact}")
            st.markdown(f"**Member impact:** {a.member_impact}")
            st.markdown("**Evidence**")
            for e in a.evidence: st.write(f"- {e}")
            st.markdown(f"**Recommended action:** {a.recommended_action}")
            st.markdown(f"**Owner:** {a.owner}")

with domains_tab:
    st.subheader("Assurance by Domain")
    ddf=pd.DataFrame([{"domain":k,"assurance_pct":v} for k,v in assessment.domain_scores.items()])
    st.bar_chart(ddf.set_index("domain"))
    st.dataframe(ddf,use_container_width=True,hide_index=True)

with scenario_tab:
    st.subheader("What-if Remediation")
    st.write("Use the sidebar to simulate fixing one assurance gap. The score recalculates from the synthetic test outcomes rather than changing every downstream status automatically.")
    st.markdown(f"**Current simulation:** {resolution}")
    if resolution!="None":
        st.success("The selected failure mode was marked resolved for the synthetic retest. Remaining gaps are unchanged.")
    else:
        st.info("Select a remediation to demonstrate targeted retesting before launch approval.")

with evidence_tab:
    st.subheader("Synthetic Test Evidence")
    for check in assessment.journey:
        with st.expander(f"{check.step} — {check.status}"):
            st.write(f"**Test result:** {check.tested-check.failed}/{check.tested} passed ({check.pass_rate}%)")
            st.write(f"**Failure mode:** {check.failure_mode}")
            st.write(f"**Evidence:** {check.evidence}")
            st.write(f"**Employer impact:** {check.employer_impact}")
            st.write(f"**Member impact:** {check.member_impact}")
            st.write(f"**Recommended remediation:** {check.remediation}")
            st.write(f"**Owner:** {check.owner}")

st.divider()
st.caption("Human-in-the-loop guardrail: the agent identifies assurance gaps and recommends remediation. It does not change eligibility, enroll employees, approve launch, contact members, alter device entitlement, or modify source systems autonomously.")
