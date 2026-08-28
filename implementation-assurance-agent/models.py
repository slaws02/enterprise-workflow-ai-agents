from dataclasses import dataclass
from typing import List, Dict

@dataclass
class JourneyCheck:
    step: str
    domain: str
    status: str
    pass_rate: int
    tested: int
    failed: int
    affected_estimate: int
    failure_mode: str
    employer_impact: str
    member_impact: str
    evidence: str
    owner: str
    remediation: str

@dataclass
class AssuranceAlert:
    severity: str
    title: str
    root_cause: str
    affected_estimate: int
    employer_impact: str
    member_impact: str
    evidence: List[str]
    recommended_action: str
    owner: str

@dataclass
class AssuranceAssessment:
    client: str
    program: str
    launch_date: str
    assurance_score: int
    tested_scenarios: int
    failed_scenarios: int
    affected_estimate: int
    journey: List[JourneyCheck]
    alerts: List[AssuranceAlert]
    domain_scores: Dict[str, int]
    launch_recommendation: str
