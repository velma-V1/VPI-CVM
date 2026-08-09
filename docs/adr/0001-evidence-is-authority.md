# ADR 0001 — Deterministic evidence is acceptance authority

**Status:** Accepted

## Decision

LLM outputs may propose work and repairs but may not declare their own artifacts correct. Task acceptance is computed from configured deterministic evidence gates.

## Consequences

- additional execution cost is accepted in exchange for verifiability
- model confidence is diagnostic metadata only
- missing evidence is a failure, not an implicit pass
