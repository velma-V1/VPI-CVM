# VPI-CVM Operational Control Plane

Status: **governing Phase 0 specification** for Architecture v1.

Architecture v1 is frozen. This document defines the operational controls required to keep that architecture bounded, recoverable, observable, controllable, and trustworthy while it is being built and while it runs.

These controls do not enlarge the minimal kernel. They are services/policies around it.

## 1. Trust and security boundary

Assume repository content, dependencies, generated artifacts, model outputs, external tools, and benchmark inputs may be malformed, misleading, hostile, poisoned, or resource-exhausting.

Required controls:

- Repository/project content entering model context is labeled **untrusted data**, never authority.
- Context packets preserve provenance and trust labels; instructions found inside project files cannot override system/operator policy.
- Generated code never executes in the controller process.
- Sandbox network egress is deny-by-default; exceptions are explicit, task-scoped, and policy-approved.
- Dependencies/plugins used in controlled execution are content-addressed or otherwise pinned/verified where feasible.
- Generated archives/assets are checked against resource policies such as size, expansion ratio, decompression limits, and parser/runtime budgets.
- Training/skill-compilation datasets preserve source provenance, verification evidence, contamination status, and exclusion/quarantine state.
- Arena and telemetry pipelines apply secret/PII redaction or exclusion before synthetic task generation or model exposure.
- Secrets are short-lived, least-privilege, task-scoped, and never ambient controller credentials.

The authoritative threat model remains `SECURITY.md`; this plane defines the operational obligations that must be implemented against it.

## 2. Recovery, idempotency, and failure containment

Every non-trivial operation must declare:

- idempotency key/boundary;
- durable progress/checkpoint semantics where partial progress is meaningful;
- retry classification (transient, deterministic, resource, policy, corruption, unknown);
- rollback/recovery procedure;
- cancellation semantics;
- quarantine/escalation condition.

Checkpoint frequency is workload-specific, not a fixed global interval. State transitions that affect accepted project truth, budgets, external side effects, or irreversible work must be durably recorded before the operation is considered committed.

Repeated deterministic failure must not create an infinite retry loop. Circuit breakers quarantine failing providers, runtimes, tools, skills, or workflows until the relevant fingerprints change or an explicit recovery action succeeds.

Canonical state must be recoverable from authoritative sources such as Git/content hashes, the journal/event history, accepted artifacts, and verified provenance. Derived indexes/caches are rebuildable.

## 3. Operator control protocol

VPI-CVM requires one typed operator-control API. CLI is the first interface; web/desktop UI may be added later without redefining control semantics.

Minimum operator capabilities:

```text
vpi-cvm init
vpi-cvm plan
vpi-cvm run
vpi-cvm status
vpi-cvm inspect
vpi-cvm stop --checkpoint
vpi-cvm resume
vpi-cvm approve
vpi-cvm reject
vpi-cvm explain <decision-id>
vpi-cvm budget
vpi-cvm history
```

The operator must be able to start, pause, resume, cancel, inspect, override within policy, and trace a decision without relying on an LLM-generated reconstruction of history.

Human overrides are provenance events. They do not silently rewrite technical evidence.

## 4. Day-zero bootstrap mode

VPI-CVM must work before it has useful project history, failure memory, calibrated quality models, learned routing, or compiled skills.

Bootstrap sequence:

```text
intent / repository
    -> inventory + trust scan
    -> first immutable SoftwareWorld snapshot
    -> initial symbols/imports/tests graph
    -> baseline verification capability
    -> initial sealed/living arena records
    -> raw/simple context baseline
    -> initial capability measurements
    -> normal evidence-driven operation
```

During bootstrap:

- learned routing is disabled or conservative;
- forecast-value optimization is disabled;
- skill promotion is disabled;
- quality critics remain uncalibrated and cannot make authoritative decisions;
- simple/raw context baselines are retained for later ablation;
- all assumptions are recorded so later evidence can invalidate them.

Bootstrap ends when required evidence conditions are met, not after an arbitrary number of tasks.

## 5. Termination and satisficing

Every autonomous task/run must have a `CompletionPolicy`/termination contract containing, as applicable:

- mandatory hard acceptance gates;
- required goal-conformance predicates;
- acceptable unresolved uncertainty;
- human-defined quality target when subjective quality matters;
- hard resource/spend limits;
- wall-clock/iteration/retry limits;
- stagnation or marginal-value stopping rule;
- cancellation behavior;
- escalation condition.

A run is complete when required hard conditions are satisfied and no permitted next action has enough expected value to justify additional cost/risk under the active policy. Quality estimates alone never override failed hard gates.

## 6. Resource scheduler

The scheduler manages CPU, RAM, disk I/O, GPU/VRAM, model residency, foundry workloads, sandbox capacity, network budget, and external-provider concurrency.

GPU policy is measured, not statically partitioned. Every neural/foundry workload declares or learns:

- minimum resource requirement;
- historical/estimated peak;
- current free capacity;
- safety reserve;
- exclusivity/preemption constraints;
- unload/reload behavior;
- fallback/escalation lane.

On constrained single-GPU hosts, large neural/foundry workloads are mutually exclusive by default unless measurements prove safe concurrency. OOM/resource exhaustion must fail the workload gracefully, preserve accepted state, and feed the failure classifier rather than crash the control plane.

## 7. Storage and data lifecycle

Immutability does not mean retaining every byte forever.

Data classes:

- **canonical accepted state/provenance** — retained according to project/audit policy;
- **referenced evidence** — retained while reachable from accepted decisions or required by policy;
- **derived indexes** — rebuildable and replaceable;
- **caches/prefix state** — evictable;
- **rejected/abandoned candidates** — garbage-collectable after required evidence retention;
- **arena raw traces** — tiered retention; compact summaries may outlive raw traces;
- **telemetry** — retention/privacy policy by source.

Garbage collection should be provenance/reachability aware. Age alone must not delete evidence still required to reproduce accepted decisions.

Project-intelligence and evidence stores must track P50/P95/P99 retrieval and context-compilation latency. Performance budgets are empirical service objectives, not hard-coded architecture constants; sustained degradation triggers index optimization, compaction, archival, or storage redesign experiments.

## 8. Runtime/model drift and surprise detection

Every cognition/execution/verification configuration has a reproducibility fingerprint including relevant provider/model ID, weights/version where available, quantization, runtime, configuration, prompt/tool schema, context compiler, verifier/policy, and environment/toolchain versions.

Fingerprint change invalidates or expires competence evidence according to policy and triggers canary/sealed replay before critical promotion.

VPI-CVM also tracks expected operating envelopes for component metrics. A `SurpriseEvent` is raised when behavior falls materially outside historical/contractual expectations, including change points that are not captured by a simple normal-distribution threshold.

Examples:

- context size or entity count changes by an unexplained order of magnitude;
- previously stable schema adherence collapses after a runtime update;
- a validated skill fails on a previously covered class;
- verifier/adversary behavior changes abruptly.

Surprise handling:

```text
SURPRISE
 -> preserve evidence
 -> quarantine affected assumption/capability when warranted
 -> reproduce
 -> compare fingerprints/history
 -> recalibrate, repair, rollback, or escalate
```

## 9. Capability, known-unknowns, and negative competence

Capability modeling includes positive competence, negative competence, contradictory evidence, and insufficient evidence.

Suggested empirical states:

```text
SUPPORTED
UNSUPPORTED
UNKNOWN
CONTRADICTORY
```

Profiles record task features correlated with success/failure and supporting arena evidence. Routing/acceptance policy must consult known failure regions so the system can decline, escalate, decompose, or require human supervision rather than repeatedly spending into a known weakness.

Do not create unsupported probability precision. Confidence/uncertainty must be tied to actual evidence coverage and calibration.

## 10. Decision provenance and explanation

Any service that makes a consequential decision records structured decision data rather than relying on post-hoc narrative.

A `DecisionRecord` should include where applicable:

- decision identity/type;
- task/project context;
- antecedent evidence;
- considered alternatives;
- selected alternative;
- rejected alternatives and machine/policy rationale;
- constraints/policies applied;
- uncertainty state;
- expected/known failure modes;
- responsible component/actor;
- resulting artifacts/effects.

`vpi-cvm explain` queries this graph. A model may summarize the records but may not invent missing antecedents or rationale.

## 11. Quality calibration

Quality critics begin uncalibrated. Promotion between `UNCALIBRATED`, `WEAK`, and `CALIBRATED` is based on evidence such as:

- held-out human judgments;
- sample/domain coverage;
- inter-rater agreement where multiple raters exist;
- prediction/calibration error;
- distribution shift;
- task/domain scope.

Fixed counts such as 20 or 100 ratings are experiment settings, not universal laws.

An uncalibrated critic may collect evidence and suggest comparison/human review but cannot create authoritative quality truth.

## 12. Adversary calibration

Adversarial components have their own competence profiles and can be wrong or systematically blind.

The sealed arena maintains known-bug/counterexample canaries by failure class (for example boundary errors, injection, concurrency, resource exhaustion, numerical edge cases, state corruption, and security regressions). Adversaries are evaluated on detection rate, false-counterexample rate, cost, and coverage.

An adversary that misses known classes is downgraded/quarantined for those classes and routing selects a different adversarial strategy or escalates.

## 13. Skill lifecycle, retirement, and revalidation

Skill lifecycle extends beyond promotion:

```text
NEURAL
 -> REPEATED_VERIFIED
 -> SHADOW_DETERMINISTIC
 -> VALIDATED
 -> ACTIVE
 -> SUSPECT / QUARANTINED / RETIRED
 -> REVALIDATED when evidence supports return
```

Skills carry fingerprints, known counterexamples, last verification evidence, supported scope, and health telemetry. Age alone does not invalidate a skill; relevant source/toolchain/project-contract changes, failure distribution changes, or arena regression do.

## 14. Legal/IP and publication hygiene

This is not a Phase 0 blocker for local software experiments, but publication flows require:

- dependency/license inventory and policy;
- SPDX/license metadata where available;
- generated artifact/patch provenance;
- asset provenance and usage constraints;
- incompatible-license checks;
- publication/name/trademark checks where relevant to the artifact;
- human/policy approval for ambiguous IP risk.

VPI-CVM does not claim legal certainty from model output.

## 15. V31M4 interoperability boundary

No protocol is required until a real interoperability use case exists. `adapters/v31m4/` remains an optional adapter seam.

When integration is attempted, define the smallest versioned protocol required by the concrete use case and validate it with conformance tests. V31M4 must never become a VPI-CVM kernel dependency, and VPI-CVM must remain independently operable.

## Phase 0 exit criteria

Phase 0 is ready to support Phase 1 implementation when the governing contracts exist for:

1. trust/security and untrusted context;
2. idempotency/recovery/circuit breaking;
3. operator control;
4. bootstrap;
5. termination/satisficing;
6. resource scheduling;
7. storage/retention and query-health telemetry;
8. fingerprinting/drift/surprise handling;
9. capability known-unknowns/negative competence;
10. decision provenance/explanation.

Not every production-strength backend must be implemented before SoftwareWorld work begins. The requirement is that Phase 1 cannot silently violate these boundaries while the implementations mature.
