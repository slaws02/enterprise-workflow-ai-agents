# Employer Connected-Care Implementation Blueprint Agent

A portfolio demonstration of an AI-enabled, multi-source implementation workflow for a **fictional employer-sponsored connected-health benefit** that includes a member mobile app, connected blood-pressure monitor, and smart scale.

> **Synthetic demo only.** All organizations, people, employees, members, requirements, devices, dates, records, and implementation scenarios in this repository are fictional. The project does not represent or reproduce the internal processes of any real healthcare, insurance, employer, device, or technology company.

## Implementation model

The implementation customer is the **employer client** purchasing a connected-health program for its workforce.

```text
Program Provider
    │
    └── Employer Client
          │
          ├── Employer Implementation
          │     ├── Contract / scope
          │     ├── Eligibility configuration
          │     ├── Data integration
          │     ├── Program configuration
          │     ├── Employee communications
          │     ├── Reporting
          │     ├── Billing
          │     └── Launch readiness
          │
          └── Eligible Employees
                │
                └── Employees who opt in become Members
                      ├── Mobile app
                      ├── BP monitor
                      ├── Smart scale
                      ├── Device fulfillment
                      ├── Pairing / data sync
                      └── Program participation / support
```

The agent's primary question is:

> **What must the implementation manager resolve so the employer client can successfully launch the benefit to its eligible workforce?**

Member enrollment and connected-device operations are downstream dependencies of that employer implementation.

## Fictional scenario

- Employer client: Summit Manufacturing Group
- Program: Connected Health Management Benefit
- Benefit model: Voluntary employee opt-in
- Eligible workforce: 18,500 employees in the CRM scenario
- Expected opt-in members: 3,700
- Member experience: mobile connected-care app plus contracted connected devices
- Target launch: November 1, 2026

The demo intentionally includes conflicts between fictional source systems so the agent has something meaningful to reconcile.

## What the agent demonstrates

1. Ingest implementation context from simulated CRM, contract, project, collaboration, meeting, and playbook sources.
2. Normalize employer implementation requirements into a single matrix.
3. Detect conflicting or incomplete client requirements.
4. Generate decision questions for human owners.
5. Extract employer-launch actions from meeting notes.
6. Track how employer-level decisions affect downstream employee enrollment and connected-device readiness.
7. Assess employer launch readiness by domain.
8. Preserve implementation memory so users can ask why a decision exists and see supporting evidence.

## Connected-device workflow

Devices are treated as part of the **downstream enrolled-member experience**, not as the implementation customer.

Employer eligibility → Employee opt-in → Member account → Device eligibility → Shipping address → Fulfillment → App access → Pairing → Readings sync → Support / replacement

The fictional program includes:

- Mobile connected-care app
- Connected blood-pressure monitor
- Smart scale
- Device-kit eligibility mapping
- Shipping-address validation
- Fulfillment file approval
- Test shipment
- App activation
- Device pairing
- Connected readings ingestion
- Pairing/sync support escalation
- Replacement-device workflow

## Multi-step agent workflow

```text
Synthetic CRM ───────────┐
Synthetic Contract ──────┤
Project Tracker ─────────┤
Collaboration Messages ──┼─> Normalize ─> Reconcile ─> Decisions
Meeting Notes ───────────┤                           ├─> Actions
Implementation Standard ─┤                           ├─> Member/Device Enablement
Decision Log ────────────┘                           ├─> Employer Launch Readiness
                                                    └─> Implementation Memory
```

## Why this is an L2-style AI workflow

This is not a single prompt that drafts an email. The workflow coordinates multiple sources, compares business requirements, detects ambiguity, preserves evidence, generates structured downstream work, and connects employer-level implementation decisions to downstream member operations while humans retain approval authority.

The demo uses deterministic logic so it runs reliably without API keys. In a production design, approved enterprise language models could support extraction and reconciliation while retaining citations, validation rules, access controls, and human approval gates.

## Human-in-the-loop guardrails

The agent can recommend actions, but it does **not** decide employer eligibility, enroll employees, change launch dates, contact employees or members, ship or replace devices, modify source systems, approve client requirements, or invent answers when sources disagree.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Run tests

```bash
pytest -q
```

## Streamlit Community Cloud

Deploy `connected-care-implementation-blueprint/app.py` from this repository. `requirements.txt` is stored beside the app entrypoint. No secrets or API keys are required for the portfolio demo.

## Repository structure

```text
app.py                    Streamlit UI
blueprint_engine.py       Reconciliation, decisions, actions, readiness, memory
connectors.py             Synthetic source adapters
models.py                 Domain models
data/                      Fictional source-system records
tests/                     Unit tests
docs/demo-script.md        Interview walkthrough
```
