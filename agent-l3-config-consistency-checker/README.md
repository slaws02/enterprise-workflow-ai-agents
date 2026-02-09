# L3 — Plan Configuration Consistency Checker (Demo)

## Purpose
Compares intended plan design values against configured values and flags mismatches that can lead to claims defects, member abrasion, and audit findings.

## Executive Value
Reduces downstream defects and rework by detecting configuration inconsistencies before go-live.

## Key Behaviors
- Cross-checks cost share values
- Validates deductible and OOP relationships
- Detects accumulator logic mismatches
- Flags preventive coverage errors
- Checks network tier consistency
- Labels severity levels
- Recommends correction actions
- Refuses to invent missing data

## Output Schema
PLAN DESIGN SUMMARY  
CONFIG SUMMARY  
MISMATCH FINDINGS  
SEVERITY LEVELS  
WHY IT MATTERS  
RECOMMENDED CORRECTIONS  
SME REVIEW NEEDED  

## Data Safety Note
Uses synthetic cross-check rules only. No proprietary configuration systems referenced.
