# ADR 0005 — Freeze Architecture v1; separate operational and discovery planes

**Status:** Accepted

## Context

VPI-CVM Architecture v1 has converged on a stable cognitive substrate: explicit resident intelligence, immutable world snapshots, an independent Context Compiler, heterogeneous cognition, three epistemic planes, dual arenas, adversarial counterexample search, failure compilation, realized-value measurement, and verified skill compounding.

Further top-level redesign before real SoftwareWorld/arena evidence would create architecture churn. At the same time, two categories of requirements must remain explicit:

1. operational controls required to keep the system safe, recoverable, bounded, observable, and controllable while v1 is built;
2. later metacognitive machinery required for VPI-CVM to research and modify its own architecture under controlled experimentation.

Neither category belongs in the eight-contract minimal core.

## Decision

1. **Freeze `docs/ARCHITECTURE.md` as Architecture v1 / best current starting hypothesis.** Freeze means no speculative top-level redesign without empirical pressure; it does not mean the design is claimed optimal.
2. **Make `docs/OPERATIONAL_CONTROL_PLANE.md` the governing Phase 0 specification.** It covers trust/security, recovery/idempotency, operator control, bootstrap, termination/satisficing, resource scheduling, storage/query health, fingerprint/drift/surprise handling, known-unknown competence, decision provenance, calibration, skill retirement, and publication hygiene.
3. **Make `docs/DISCOVERY_PLANE.md` the post-v1 research roadmap.** It covers the metacognitive self-model, architectural uncertainty, weakness mining, hypothesis generation, ResearchWorld, architecture search, isolated system worktrees, shadow experiments, causal/ablation analysis, scientific memory, meta-governance, and safe recursive improvement.
4. **Keep the minimal core unchanged.** Operational and discovery capabilities remain evolvable services/policies around the kernel.
5. **No direct self-rewrite.** Future architectural change is performed in isolated challengers and requires matched evaluation, security/recovery checks, sealed promotion, and rollback.
6. **Keep V31M4 independent.** No bridge protocol is defined until a concrete interoperability use case exists.

## Consequences

- Phase 0 becomes a real operational precondition rather than scattered future hardening.
- Architecture v1 can begin implementation without pretending the final build spec is known in advance.
- Known weaknesses, surprise events, decision reasons, adversary blind spots, quality calibration, and skill retirement are first-class planned behaviors.
- Self-discovery remains possible without contaminating the correctness-critical core or allowing uncontrolled recursive modification.
- Future architectural ideas must be framed as hypotheses and earn promotion through reproducible evidence.
