# VPI-CVM Adaptive Institution Layer — Superseded Architecture Note

Status: **historical**.

This document previously expanded VPI-CVM beyond a software-only verification pipeline by adding intent/value, day-zero bootstrap, anti-Goodhart evaluation, world grounding, survival modes, economic reasoning, model drift control, and optional creative/collaborative extensions.

Those ideas have been reconciled into [`ARCHITECTURE.md`](ARCHITECTURE.md) and [`PLAN.md`](PLAN.md). Where this note conflicts with Architecture v1, **Architecture v1 is authoritative**.

## Ideas retained

- human intent/value is explicit state and authority, not a fallback error path;
- day-zero work must not assume mature repository history;
- repository truth is not production/world truth;
- anti-Goodhart evaluation requires independent holdouts and metric-divergence awareness;
- provider/model drift must trigger canary replay and quarantine;
- provider/runtime failure must degrade capability without destroying project truth;
- background work requires budgets, cancellation, and measurable objectives;
- human preference and domain-quality evaluation must not silently override machine-defensible correctness.

## Corrections in Architecture v1

Architecture v1 makes several boundaries sharper:

- durable intelligence is explicit verified state, never opaque KV state;
- canonical knowledge uses immutable/versioned snapshots, while ephemeral operational coordination may mutate transactionally;
- correctness, mechanical goal conformance, interpretive goal conformance, and subjective quality are not collapsed into one acceptance score;
- Living Arena tasks are surveillance/practice data and cannot independently promote capabilities;
- sealed and rotating evaluation remains independent promotion/generalization truth;
- adversarial models search for counterexamples but deterministic arbiters remain the authority;
- economic optimization starts with realized-value observation before forecast models are trusted;
- cross-domain transfer remains research until multiple mature domain world models create actual evidence;
- V31M4 is independent and any bridge is optional interoperability only.

The Git history preserves the complete original addendum for research/reference.
