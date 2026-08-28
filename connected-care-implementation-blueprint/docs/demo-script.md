# 5-Minute Demo Script

## 1. Frame the implementation model

"This demo models an employer-sponsored connected-health benefit. The implementation customer is the employer client. The employer purchases the program for its workforce, eligible employees may opt in, and only then do those employees become members who use the app, devices, and ongoing program services."

Point out the synthetic-data banner and the hierarchy in the sidebar:

**Program Provider → Employer Client → Eligible Employees → Opt-in Members → App / Devices / Program Participation**

## 2. Show the Employer Blueprint

Open **Employer Blueprint**.

Call out the employer-level requirements the implementation manager must reconcile before launch:
- Benefit scope and eligible workforce
- Eligibility-file configuration
- Program configuration
- Employee launch communications
- Reporting
- Billing
- Downstream device enablement

Show the deliberately inconsistent requirements:
- Eligible population differs between CRM and contract.
- Device bundle differs between CRM and contract.
- Communication ownership differs across sources.

Explain: "The agent is not deciding which source is correct. It is identifying ambiguity that can affect the employer launch and putting the decision in front of the right human owner."

## 3. Show Decisions and Actions

Open **Decisions** and expand the employer eligibility conflict.

Explain why it matters downstream: eligibility drives file configuration, who may enroll, communications, billing, and device fulfillment rules.

Then open **Actions** and show how a working session becomes structured employer-launch follow-up with owners and due dates.

## 4. Show Member & Device Enablement

Open **Member & Device Enablement**.

Say: "This is downstream of the employer implementation. Devices are part of what must be operationally ready for employees who become members; they are not the implementation customer."

Walk through:

Employer eligibility → Employee opt-in → Member account → Device eligibility → Shipping address → Fulfillment → App access → Pairing → Readings sync → Support / replacement

Call out the blocked readings-ingestion validation. Use the sidebar toggle **Simulate device data issue resolved** and show that one downstream technical issue moves to Ready without clearing the employer's other launch requirements.

## 5. Show Employer Launch Readiness + Memory

Open **Employer Launch Readiness** and emphasize that the top-level question is:

> Is the employer client ready to launch this benefit to its eligible workforce?

Show that readiness spans employer scope, eligibility/data, program configuration, employee communications, member/device enablement, reporting, billing, and final launch approval.

Then open **Implementation Memory** and ask:

"Why is the smart scale still an open implementation issue?"

Close with:

"The goal is not autonomous implementation. It is to give an implementation manager a reliable layer across the systems they already use: reconcile employer requirements, expose ambiguity early, convert meetings into actions, connect employer decisions to downstream member operations, and preserve decision context while humans retain approval authority."
