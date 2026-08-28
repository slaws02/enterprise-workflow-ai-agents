# 5-Minute Demo Script

## 1. Frame the problem

"Implementation information usually lives in several places. A project manager may have the contract in a document store, account details in a CRM, milestones in a project tracker, technical updates in collaboration messages, and decisions buried in meeting notes. This demo shows how an agent can reconcile those sources into an implementation blueprint rather than asking the team to manually search each system."

Point out the synthetic-data banner.

## 2. Show the Blueprint

Open **Blueprint** and call out that the fictional program includes a mobile app, blood-pressure monitor, and smart scale.

Show three deliberately inconsistent requirements:
- Eligible population differs between the CRM and contract.
- Device bundle differs between the CRM and contract.
- Communication ownership differs across sources.

Explain: "The agent is not deciding which source is correct. It is identifying the ambiguity and putting the decision in front of the right human owner."

## 3. Show Decisions and Actions

Open **Decisions** and expand the device-bundle conflict. Point out the evidence and recommended question.

Then open **Actions** and show how working-session notes become structured follow-up items with owners and due dates.

## 4. Show Connected Devices

Open **Connected Devices** and walk through:

Eligibility → Kit Assignment → Address Validation → Fulfillment → Delivery → App Activation → Pairing → Readings Sync → Support / Replacement

Call out the blocked readings-ingestion validation. Use the sidebar toggle **Simulate device data issue resolved** and show the data-sync stage moving to Ready.

## 5. Show Launch Readiness + Memory

Open **Launch Readiness** and show that resolving one technical issue improves one domain but does not resolve eligibility, communications, billing, or fulfillment.

Then open **Implementation Memory** and ask:

"Why is the smart scale still an open implementation issue?"

Close with: "The design goal is not autonomous implementation. It is to give an implementation manager a reliable layer across the systems they already use: reconcile requirements, expose ambiguity early, convert meetings into actions, manage connected-device dependencies, and preserve decision context while humans keep approval authority."
