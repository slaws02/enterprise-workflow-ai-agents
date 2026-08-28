from blueprint_engine import build_blueprint, query_memory
from connectors import get_collaboration_messages, get_contract_requirements, get_crm_record, get_decision_log, get_implementation_standard, get_meeting_notes, get_project_tasks

def assessment(resolved=False):
    return build_blueprint(get_crm_record(),get_contract_requirements(),get_project_tasks(),get_collaboration_messages(),get_meeting_notes(),get_implementation_standard(),get_decision_log(),resolved_device_feed=resolved)

def test_detects_population_conflict():
    assert any("eligible population" in d.title.lower() for d in assessment().decisions)

def test_detects_device_bundle_conflict():
    assert any("device bundle" in d.title.lower() for d in assessment().decisions)

def test_device_data_resolution_removes_one_blocker():
    before=assessment(False); after=assessment(True)
    assert len(after.blockers)==len(before.blockers)-1
    assert after.readiness_by_domain["Data Integration"]==100

def test_memory_returns_device_evidence():
    answer=query_memory("Why is the smart scale an issue?",assessment().memory)
    assert "Smart scale" in answer or "smart scale" in answer
