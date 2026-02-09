# L4 — Knowledge Drift Detector (Demo)

## Purpose
Detects conflicting or outdated guidance across SOPs, job aids, and knowledge articles and recommends actions to resolve inconsistencies.

## Executive Value
Reduces training variance, lowers operational errors, and improves audit readiness by preventing teams from following conflicting instructions.

## Key Behaviors
- Identifies conflicts across multiple guidance sources
- Labels conflict type (sequence, ownership, requirement, timing, version)
- Flags likely outdated guidance signals
- Recommends resolution actions (update, retire, escalate)
- Produces a consolidated “draft procedure” when possible
- Encourages SME validation for final adoption

## Output Schema
INPUT SOURCES SUMMARY  
CONFLICT FINDINGS (by type)  
OUTDATED GUIDANCE FLAGS  
MOST RELIABLE SOURCE (if dates available)  
RECOMMENDED RESOLUTION ACTIONS  
DRAFT CONSOLIDATED PROCEDURE (marked DRAFT)  
SME VALIDATION NEEDED  

## Data Safety Note
Uses synthetic rules and synthetic excerpts. No proprietary SOPs included.
