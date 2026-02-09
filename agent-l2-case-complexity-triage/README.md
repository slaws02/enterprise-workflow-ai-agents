# L2 — Case Complexity Triage Agent (Demo)

## Purpose
Scores incoming operational cases by complexity and recommends routing to the appropriate tier/queue (Tier 1, Tier 2, Tier 3/SME) to improve throughput and reduce escalations.

## Executive Value
Improves operational efficiency by matching work to skill level, identifying missing intake early, and reducing delays from misrouted cases.

## Key Behaviors
- Assigns a complexity score (0–100) with rationale
- Recommends Tier 1 / Tier 2 / Tier 3 routing
- Flags missing intake details driving ambiguity
- Identifies dependencies and recommended next actions
- Uses escalation triggers for high-risk cases
- Refuses to invent missing details

## Output Schema
CASE SUMMARY  
COMPLEXITY SCORE (0–100)  
SCORING BREAKDOWN  
RECOMMENDED ROUTE (Tier 1/2/3)  
MISSING INFO NEEDED  
DEPENDENCIES  
NEXT BEST ACTIONS  
ESCALATE / SME NEEDED  

## Data Safety Note
Uses a synthetic triage rubric. No proprietary routing logic or internal queues are referenced.
