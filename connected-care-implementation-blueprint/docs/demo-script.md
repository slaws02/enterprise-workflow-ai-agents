# 5-Minute Interview Demo Script

## 0:00–0:30 — Frame the business problem

"This demo models an employer-sponsored connected-health benefit. The implementation customer is the employer client. The employer purchases the program for its workforce, eligible employees may opt in, and only then do those employees become members who use the app, devices, and ongoing program services.

The implementation challenge is that requirements and decisions can be spread across CRM records, contracts, project plans, collaboration messages, meeting notes, and internal standards. This agent creates one implementation layer across those sources."

Point briefly to the synthetic-data banner and sidebar hierarchy:

**Program Provider → Employer Client → Eligible Employees → Opt-in Members → App / Devices / Program Participation**

Do not spend time explaining code.

## 0:30–1:15 — Start with the executive summary

Stay on the landing screen.

Say:

"For this fictional employer, the agent immediately tells me how much of the implementation is confirmed, how many decisions are still open, how many cross-functional dependencies exist, and whether there are launch blockers. It also separates the 18,500 eligible employees from the estimated employees who may actually opt into the benefit."

Then point to **What the agent found** and **What the agent did**.

Key line:

"The value is not another project dashboard. The agent reconciles what the different systems are saying and tells the implementation manager where human judgment is still required."

## 1:15–2:05 — Employer Blueprint + Decisions

Open **Employer Blueprint**.

Say:

"This is the employer implementation blueprint: benefit scope, eligible workforce, program configuration, communications, integrations, reporting, billing, and downstream member enablement."

Call out the intentionally inconsistent requirements:
- Eligible population differs between CRM and contract.
- Device bundle differs between CRM and contract.
- Communication ownership differs across sources.

Then open **Decisions** and expand the eligible-population conflict.

Say:

"The agent does not decide which source is correct. It surfaces the conflict, preserves the evidence, recommends the question that needs to be answered, and identifies the human owner."

Connect it to downstream consequences:

"An eligibility decision can affect the eligibility file, who can enroll, employee communications, billing, and device-fulfillment rules."

## 2:05–2:45 — Actions

Open **Actions**.

Say:

"The same workflow converts an implementation working session into structured follow-up with owners and due dates. In production, reviewed actions could be sent through an approved project-management connector rather than manually re-entered."

Do not read every row. Point to two examples only.

## 2:45–3:35 — Member & Device Enablement

Open **Member & Device Enablement**.

Say:

"This is downstream of the employer implementation. Devices are part of the member experience; they are not the implementation customer."

Walk across the flow quickly:

**Employer launch → Employee eligibility → Employee opt-in → Member account → Device eligibility → Fulfillment → App access → Pairing → Readings sync → Support**

Call out the blocked readings-ingestion validation.

Use **Simulate device data issue resolved**.

Say:

"When I resolve this one technical dependency, the data-integration portion improves, but the agent does not pretend the whole implementation is suddenly ready. The employer still has unresolved business decisions and launch dependencies."

That is the strongest live-demo moment.

## 3:35–4:20 — Employer Launch Readiness

Open **Employer Launch Readiness**.

Say:

"The top-level question remains: is the employer ready to launch this benefit to its eligible workforce? The readiness view rolls up the separate workstreams without losing the underlying evidence."

Point to the weakest two domains and current blockers. Avoid reading every percentage.

## 4:20–4:50 — Implementation Memory

Open **Implementation Memory** and ask:

**Why is the smart scale still an open implementation issue?**

Say:

"Instead of searching old meeting notes or messages, the implementation manager can ask why a decision exists and get the relevant implementation history with its source and owner."

## 4:50–5:00 — Close

Use this closing:

"The design goal is not autonomous implementation. It is an L2 AI workflow that helps an implementation team work across the systems they already use: reconcile employer requirements, expose ambiguity earlier, turn meetings into actions, connect employer decisions to downstream member operations, and preserve decision context while humans retain approval authority."

## If they ask how it works

Keep the explanation short:

"For the portfolio demo I used synthetic JSON sources and deterministic logic so it runs without credentials or API keys. In an enterprise version, those source adapters could be replaced with approved connectors to CRM, project-management, collaboration, document, and knowledge systems. An approved language model could assist with extraction and reconciliation while keeping citations, validation rules, role-based access, and human approval gates."

## If they ask whether the agent writes back to systems

"Not autonomously. My design separates recommendation from action. The agent can prepare a structured update, but a human reviews it before any approved connector changes a project record, sends a communication, changes eligibility, or affects device fulfillment."

## What not to over-explain

- Python or Streamlit internals unless they ask.
- Every synthetic field.
- Every readiness percentage.
- The device workflow before establishing that the employer is the client.
- AI terminology before demonstrating the business problem it solves.
