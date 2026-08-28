# Implementation Assurance Agent

A portfolio demonstration of a pre-launch assurance workflow for a **fictional employer-sponsored connected-health benefit**.

> **Synthetic demo only.** All employers, employees, members, devices, test populations, requirements, dates, and results are fictional. This project does not represent the internal processes of any real healthcare, insurance, employer, device, or technology company.

## Business problem

A project can appear operationally on track while the downstream employee/member journey still contains preventable launch failures. This agent asks a different question than a project tracker:

> **If the employer launches this configuration, will eligible employees who opt in actually be able to enroll, receive the right connected-device experience, activate the app, sync readings, and get support?**

## What it does

The agent evaluates synthetic pre-launch tests across:

- employer/program discovery
- eligibility and identity matching
- employee opt-in enrollment
- member account creation
- connected-device entitlement
- shipping address and fulfillment
- mobile app activation
- device pairing
- connected readings ingestion
- member support readiness

For each journey step it records test coverage, pass rate, failed scenarios, estimated affected population, failure mode, employer impact, member impact, evidence, owner, and recommended remediation.

## Why this is distinct from the other implementation agents

1. **Implementation Blueprint Agent** — defines what must be configured and resolved for the employer launch.
2. **Implementation Risk Agent** — identifies execution risks while the project is underway.
3. **Implementation Assurance Agent** — tests whether the configured launch will actually work for employees who become members.

## Human-in-the-loop design

The agent does not approve launch, change eligibility, enroll employees, change device entitlement, contact members, or modify source systems. It surfaces assurance gaps and recommended remediation for accountable humans to review.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

## Run tests

```bash
pytest -q
```

## Streamlit Community Cloud

Deploy `implementation-assurance-agent/app.py` from this repository and select the `implementation-assurance-agent` branch. No secrets or API keys are required.
