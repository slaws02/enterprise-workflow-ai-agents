# Connected Care Implementation Blueprint Agent

A portfolio demonstration of an AI-enabled, multi-source implementation workflow for a **fictional connected-care benefit** that includes a member mobile app, connected blood-pressure monitor, and smart scale.

> **Synthetic demo only.** All organizations, people, requirements, devices, dates, records, and implementation scenarios in this repository are fictional. The project does not represent or reproduce the internal processes of any real healthcare, insurance, employer, device, or technology company.

## Problem this demonstrates

Complex implementations rarely fail because one task is invisible. They fail because important information is distributed across contracts, CRM records, project trackers, collaboration messages, meeting notes, device-fulfillment workflows, technical integration work, and internal playbooks.

This agent demonstrates a workflow that can:

1. Ingest implementation context from several simulated business systems.
2. Normalize requirements into a single requirements matrix.
3. Detect conflicting or incomplete requirements.
4. Generate decision questions for the implementation team.
5. Extract actions from meeting notes.
6. Track connected-device dependencies across fulfillment, pairing, data sync, and support.
7. Assess launch readiness by domain.
8. Preserve an implementation memory so users can ask why a decision exists and see supporting evidence.

## Connected-device workflow

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

The demo intentionally includes conflicts and missing information so the agent has something meaningful to reconcile.

## Multi-step agent workflow

```text
Synthetic CRM ───────────┐
Synthetic Contract ──────┤
Project Tracker ─────────┤
Collaboration Messages ──┼─> Normalize ─> Reconcile ─> Decisions
Meeting Notes ───────────┤                           ├─> Actions
Implementation Standard ─┤                           ├─> Device Readiness
Decision Log ────────────┘                           ├─> Launch Readiness
                                                    └─> Implementation Memory
```

## Why this is an L2-style AI workflow

This is not a single prompt that drafts an email. The workflow coordinates multiple sources, compares business requirements, detects ambiguity, preserves evidence, generates structured downstream work, and keeps humans responsible for approvals.

The demo uses deterministic logic so it runs reliably without API keys. In a production design, the extraction and reconciliation layer could use an approved enterprise language model while retaining source citations, validation rules, access controls, and human approval gates.

## Human-in-the-loop guardrails

The agent can recommend actions, but it does **not** decide who is eligible, change launch dates, contact members, ship or replace devices, modify source systems, approve client requirements, or invent answers when sources disagree.

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
