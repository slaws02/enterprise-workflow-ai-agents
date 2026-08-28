from typing import List
from models import JourneyCheck, AssuranceAlert, AssuranceAssessment


def _severity(pass_rate: int, affected: int) -> str:
    if pass_rate < 80 or affected >= 1000:
        return "High"
    if pass_rate < 95 or affected >= 250:
        return "Medium"
    return "Low"


def assess_assurance(client, journey_rows) -> AssuranceAssessment:
    journey: List[JourneyCheck] = []
    alerts: List[AssuranceAlert] = []
    for row in journey_rows:
        tested = int(row["tested"])
        failed = int(row["failed"])
        pass_rate = round(100 * (tested - failed) / tested) if tested else 0
        status = "Pass" if failed == 0 else ("At Risk" if pass_rate >= 90 else "Fail")
        check = JourneyCheck(
            step=row["step"], domain=row["domain"], status=status,
            pass_rate=pass_rate, tested=tested, failed=failed,
            affected_estimate=int(row["affected_estimate"]),
            failure_mode=row["failure_mode"], employer_impact=row["employer_impact"],
            member_impact=row["member_impact"], evidence=row["evidence"],
            owner=row["owner"], remediation=row["remediation"]
        )
        journey.append(check)
        if failed:
            alerts.append(AssuranceAlert(
                severity=_severity(pass_rate, check.affected_estimate),
                title=f"{check.step} assurance gap",
                root_cause=check.failure_mode,
                affected_estimate=check.affected_estimate,
                employer_impact=check.employer_impact,
                member_impact=check.member_impact,
                evidence=[check.evidence, f"{failed} of {tested} synthetic tests failed ({pass_rate}% pass)."],
                recommended_action=check.remediation,
                owner=check.owner,
            ))

    total_tested = sum(x.tested for x in journey)
    total_failed = sum(x.failed for x in journey)
    weighted_pass = round(100 * (total_tested - total_failed) / total_tested) if total_tested else 0

    domains = {}
    for check in journey:
        domains.setdefault(check.domain, []).append(check)
    domain_scores = {}
    for domain, checks in domains.items():
        d_tested = sum(c.tested for c in checks)
        d_failed = sum(c.failed for c in checks)
        domain_scores[domain] = round(100 * (d_tested - d_failed) / d_tested) if d_tested else 0

    affected = max((a.affected_estimate for a in alerts), default=0)
    high = sum(a.severity == "High" for a in alerts)
    recommendation = (
        "HOLD — resolve high-severity assurance gaps before employer launch approval."
        if high else
        "CONDITIONAL GO — review remaining assurance gaps with accountable owners before launch approval."
        if alerts else
        "GO — synthetic member journey tests passed; human launch approval still required."
    )
    return AssuranceAssessment(
        client=client["client_name"], program=client["program"], launch_date=client["launch_date"],
        assurance_score=weighted_pass, tested_scenarios=total_tested,
        failed_scenarios=total_failed, affected_estimate=affected,
        journey=journey, alerts=sorted(alerts, key=lambda a: ({"High":0,"Medium":1,"Low":2}[a.severity], -a.affected_estimate)),
        domain_scores=domain_scores, launch_recommendation=recommendation
    )


def apply_resolution(journey_rows, resolution: str):
    rows=[dict(r) for r in journey_rows]
    targets={
        "Eligibility identity matching":"Eligibility & identity match",
        "Device entitlement":"Device kit entitlement",
        "Readings ingestion":"Connected readings ingestion",
    }
    target=targets.get(resolution)
    if target:
        for row in rows:
            if row["step"]==target:
                row["failed"]=0
                row["affected_estimate"]=0
                row["failure_mode"]="Resolved in simulation"
                row["evidence"]="Synthetic remediation validation passed."
    return rows
