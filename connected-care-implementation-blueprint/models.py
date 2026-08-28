from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Requirement:
    domain: str
    requirement: str
    client_value: str
    standard: str
    status: str
    owner: str
    source: str

@dataclass
class Decision:
    title: str
    issue: str
    evidence: List[str]
    recommended_question: str
    owner: str
    severity: str = "Medium"

@dataclass
class Action:
    action: str
    owner: str
    due: str
    source: str
    dependency: str = ""
    status: str = "Open"

@dataclass
class DeviceCheck:
    stage: str
    status: str
    detail: str
    owner: str

@dataclass
class BlueprintAssessment:
    client: str
    program: str
    launch_date: str
    requirements: List[Requirement] = field(default_factory=list)
    decisions: List[Decision] = field(default_factory=list)
    actions: List[Action] = field(default_factory=list)
    device_checks: List[DeviceCheck] = field(default_factory=list)
    dependencies: List[Dict] = field(default_factory=list)
    blockers: List[str] = field(default_factory=list)
    readiness_by_domain: Dict[str, int] = field(default_factory=dict)
    memory: List[Dict] = field(default_factory=list)

    @property
    def requirements_complete_pct(self) -> int:
        if not self.requirements:
            return 0
        complete = sum(1 for r in self.requirements if r.status == "Confirmed")
        return round((complete / len(self.requirements)) * 100)
