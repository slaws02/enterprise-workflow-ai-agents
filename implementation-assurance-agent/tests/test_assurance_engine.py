from assurance_engine import assess_assurance, apply_resolution
from connectors import get_client, get_journey_tests


def test_assurance_detects_failures():
    result=assess_assurance(get_client(),get_journey_tests())
    assert result.failed_scenarios>0
    assert result.assurance_score<100
    assert any(a.severity=="High" for a in result.alerts)


def test_identity_resolution_improves_score():
    rows=get_journey_tests()
    before=assess_assurance(get_client(),rows)
    after=assess_assurance(get_client(),apply_resolution(rows,"Eligibility identity matching"))
    assert after.assurance_score>before.assurance_score


def test_readings_resolution_removes_alert():
    rows=apply_resolution(get_journey_tests(),"Readings ingestion")
    result=assess_assurance(get_client(),rows)
    assert not any("Connected readings ingestion" in a.title for a in result.alerts)
