# L1 — Implementation Risk Pre-Check Agent (Demo)

## Purpose
Flags missing intake information, conflicting requirements, dependency gaps, and likely delay risks before implementation build begins.

## Executive Value
Prevents downstream rework, reduces defects, and improves implementation predictability by catching risk early.

## Key Behaviors
- Identifies missing required intake fields
- Flags high-risk conditions that commonly drive rework
- Lists dependencies and sequencing constraints
- Recommends next best actions
- Uses compliance-safe language and escalation triggers
- Refuses to invent missing details

## Output Schema
REQUEST / INTAKE SUMMARY  
MISSING REQUIRED INTAKE ITEMS  
RISK FLAGS (with rationale)  
DEPENDENCIES / SEQUENCING  
RECOMMENDED NEXT ACTIONS  
ESCALATE / SME NEEDED  

## Data Safety Note
Uses synthetic, portfolio-safe intake risk rules. No proprietary systems or client data.
