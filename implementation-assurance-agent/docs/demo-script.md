# 5-Minute Interview Demo Script — Implementation Assurance Agent

## 0:00–0:30 — Frame the problem

"This agent answers a different question than project status. A launch can look on track and still fail for employees. So the assurance question is: if this employer launches this configuration, will eligible employees who opt in actually be able to enroll, receive the right device experience, activate the app, sync readings, and get support?"

Point to the synthetic-data banner and employer/member hierarchy.

## 0:30–1:15 — Show the assurance score

Stay on the landing page.

"The agent has run synthetic pre-launch tests across the end-to-end member journey. It gives me an overall assurance score, failed test count, largest estimated affected population, and a launch recommendation."

Call out the top three alerts.

Key line:

"This is not just 'what tasks are late.' It is 'where will employees actually experience failure if we launch as configured?'"

## 1:15–2:15 — Member Journey Assurance

Open **Member Journey Assurance**.

Walk quickly across:

Employer launch → Eligibility match → Employee opt-in → Account creation → Device entitlement → Fulfillment → App activation → Pairing → Readings sync → Support

Call out the eligibility/identity failure and device entitlement failure.

"The agent estimates downstream population impact so the team can prioritize a 2,400-person eligibility problem over a low-volume activation issue."

## 2:15–3:00 — Assurance Alerts

Open **Assurance Alerts** and expand the eligibility alert.

Point to root cause, employer impact, member impact, evidence, owner, and remediation.

"The agent does not decide how eligibility should work. It gives the implementation manager evidence and a human-owned remediation path before production approval."

## 3:00–3:50 — What-if remediation

Use the sidebar and select **Eligibility identity matching**.

"Now I can simulate the targeted remediation and retest. The assurance score improves because those synthetic failures clear, but the other launch gaps remain."

Then optionally select **Readings ingestion**.

"The design avoids a common dashboard problem where fixing one issue makes the whole project look green. Each journey control is independently retested."

## 3:50–4:30 — Domain Scores / Evidence

Open **Domain Scores**.

"This lets leadership see which part of the member experience is least assured before launch."

Open **Test Evidence** briefly.

"Every score is traceable to synthetic test evidence and a failure mode, rather than being an unexplained AI confidence number."

## 4:30–5:00 — Close

"I see this as the third layer of an implementation AI operating model. The Blueprint Agent defines the employer implementation. The Risk Agent monitors execution. The Assurance Agent validates that the configured launch will actually work for employees who opt into the benefit. Together, they help teams move from task tracking to proactive implementation quality while humans retain approval authority."

## If they ask how production would differ

"This portfolio version uses synthetic JSON and deterministic scoring so it is safe and reproducible. In production, approved connectors could bring in eligibility test results, CRM configuration, fulfillment results, app/device test telemetry, support readiness, and reporting validation. An enterprise language model could help classify failures and summarize evidence, with validation rules and human approval gates."
