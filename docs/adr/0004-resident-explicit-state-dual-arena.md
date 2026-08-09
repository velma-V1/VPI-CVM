# ADR 0004 — Resident intelligence is explicit state; promotion uses dual arenas

**Status:** Accepted

## Context

Earlier VPI-CVM design iterations alternated between competition framing, local-model-first framing, and increasingly rich persistent-neural-state ideas. Those approaches exposed useful mechanisms but created contradictory authority boundaries.

The system needs to remain resident and compounding without making any model, API, KV cache, benchmark generator, or external project its source of truth.

## Decision

1. **Durable resident intelligence lives in explicit verified state**: immutable project/world snapshots, evidence/provenance, failure memory, verified skills, capability history, human intent/value state, arena measurements, and real-world observations.
2. KV/prefix caches are disposable performance optimizations and cannot be authoritative memory.
3. Local and frontier models remain permanent replaceable cognition lanes selected empirically; neither local-first nor frontier-first is a governing ideology.
4. VPI-CVM uses a **dual-arena model**:
   - Living Arena for continuous project-derived surveillance, practice, synthetic tasks, and regression discovery.
   - Sealed/rotating evaluation for promotion, generalization, regression truth, and anti-overfitting.
5. Adversarial models/search are counterexample generators. Deterministic checks/contracts arbitrate whether the counterexample actually invalidates a candidate.
6. Correctness, goal conformance, and subjective quality remain separate epistemic planes. Hard gates require mechanically defensible predicates.
7. Economic policy begins with realized-value recording before forecast/expected-value optimization is trusted.
8. V31M4 remains independent. Any future bridge is optional interoperability and cannot become a VPI-CVM kernel dependency.

## Consequences

- A model can be killed, unloaded, upgraded, or replaced without erasing project intelligence.
- Living synthetic benchmarks cannot independently promote the behavior they helped train or optimize.
- Model routing, skill promotion, context compilation, and future training must be replayable from immutable fingerprints.
- Cross-domain transfer remains experimental until multiple mature domain world models provide evidence for real shared structure.
- Future architecture proposals must demonstrate measurable benefit without violating the explicit-state, dual-arena, or epistemic-boundary decisions above.
