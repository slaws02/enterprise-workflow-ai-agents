"""Synthetic connectors for the portfolio demo.

Production versions could be replaced with authenticated connectors to a CRM,
project tracker, collaboration platform, document store, fulfillment service,
and internal knowledge base.
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def _load(name: str):
    with open(DATA_DIR / name, "r", encoding="utf-8") as f:
        return json.load(f)

def get_crm_record(): return _load("crm_record.json")
def get_contract_requirements(): return _load("contract_requirements.json")
def get_project_tasks(): return _load("project_tasks.json")
def get_collaboration_messages(): return _load("collaboration_messages.json")
def get_meeting_notes(): return _load("meeting_notes.json")
def get_implementation_standard(): return _load("implementation_standard.json")
def get_decision_log(): return _load("decision_log.json")
