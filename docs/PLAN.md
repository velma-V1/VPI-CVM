# VPI-CVM Implementation Plan

Status: **governing build plan for frozen Architecture v1**.

Architecture v1 is the best current starting hypothesis, not a claim of optimality. The purpose of this plan is to build a system that can discover its next failures without collapsing, measure them reproducibly, and improve only when evidence justifies change.

A checked item means the capability exists in the repository. It does **not** imply the target system is complete.

Governing companions:

- `ARCHITECTURE.md` — frozen Architecture v1.
- `OPERATIONAL_CONTROL_PLANE.md` — Phase 0 survival/control requirements.
- `DISCOVERY_PLANE.md` — post-v1 metacognitive/self-research roadmap.
- `SECURITY.md` — threat model.

## Development laws

1. **Arena first.** Substantial mechanisms require baseline/challenger measurement and explicit retain/reject/inconclusive decisions.
2. **Canonical knowledge is immutable/versioned.** New project intelligence creates new snapshots/hashes. Ephemeral operational state may mutate transactionally but never rewrites historical truth.
3. **Three epistemic planes.** Correctness is hard where mechanically defensible; goal conformance is hard only for mechanical predicates; subjective quality remains advisory until calibrated.
4. **Explicit state is the resident brain.** KV/prefix caches may accelerate inference but are never authoritative memory.
5. **Models are replaceable resources.** Local and frontier models remain permanent eligible lanes selected by evidence and value, not ideology.
6. **Living evaluation does not judge itself.** Synthetic/living tasks drive surveillance/practice; sealed/rotating holdouts govern promotion/generalization.
7. **Adversaries discover counterexamples; deterministic arbiters decide whether they break a candidate.** Adversaries themselves are calibrated.
8. **Measure realized value before optimizing forecast value.** Human time, failure recurrence, reuse, cost, compute, and latency all matter.
9. **No arbitrary architectural numerology.** Fixed task counts, p-values, rating counts, latency targets, token savings, or promotion thresholds are experiment parameters, not universal laws.
10. **Capability includes weakness and uncertainty.** Supported, unsupported, unknown, and contradictory regions are all first-class evidence.
11. **Consequential decisions are explainable from structured records.** Do not reconstruct rationale from model prose after the fact.
12. **Operational survival precedes intelligence claims.** Security, recovery, termination, resource scheduling, operator control, storage health, and surprise/drift handling are Phase 0 concerns.
13. **Cross-domain abstractions are discovered, not invented.** SoftwareWorld is first; Meta-World transfer waits for multiple mature domains.
14. **Self-modification is research, not runtime behavior.** Architectural challengers run in isolated shadow systems and require sealed promotion/rollback.
15. **V31M4 is independent.** Any bridge is optional interoperability and cannot become a VPI-CVM kernel dependency.

---

## Phase 0 — Operational Control Plane + executable-foundation hardening

Phase 0 defines the contracts that keep Phase 1+ bounded and recoverable. Not every production backend must be complete before SoftwareWorld work starts, but Phase 1 cannot silently violate these boundaries.

### Existing executable foundation

- [x] Model is proposal generator, not verifier.
- [x] Deterministic evidence controls current acceptance.
- [x] Validated Pydantic task/candidate schemas.
- [x] Validated dependency DAG and cycle rejection.
- [x] SQLite WAL task/evidence journal.
- [x] Resumable dependency-aware supervisor.
- [x] Canonical workspace containment.
- [x] Structured Ollama planner/generator.
- [x] Hardened Docker validation boundary.
- [x] Python AST gate.
- [x] Bounded evidence-fed repair loop.
- [x] NVIDIA telemetry primitive.

### Reproducibility and provenance hardening

- [ ] Schema migration/version table for durable storage.
- [ ] Content hashes for evidence and produced artifacts.
- [ ] Immutable accepted-base commit recorded for every mutable candidate.
- [ ] Append-only decision/provenance record.
- [ ] Reproducibility fingerprint envelope for model/runtime/prompt/context/verifier/toolchain configuration.
- [ ] Epistemic labels for MEASURED / DERIVED / INFERRED / HEURISTIC / UNKNOWN quantitative claims.

### Trust/security boundary

- [ ] Context trust labels: project/repository content is untrusted data, never authority.
- [ ] Structured separation between system/operator policy and project-file content to resist prompt injection.
- [ ] Dependency/plugin pinning/hash verification where feasible.
- [ ] Artifact resource policies for file size, archive expansion, parser/runtime budgets, and dangerous payload classes.
- [ ] Arena/telemetry secret and PII exclusion/redaction path.
- [ ] Short-lived least-privilege secret capability model.
- [ ] Network egress deny-by-default preserved across all execution backends.

### Recovery and circuit breaking

- [ ] Operation-level idempotency keys/boundaries.
- [ ] Durable progress semantics for long-running operations.
- [ ] Retry classification: transient / deterministic / resource / policy / corruption / unknown.
- [ ] Cancellation and rollback semantics.
- [ ] Provider/tool/runtime/workflow circuit breakers.
- [ ] Quarantine path for repeated or unexplained failure.
- [ ] Recovery from canonical Git/content/evidence sources; derived indexes/caches rebuildable.

### Operator control API

- [ ] Typed operator-control protocol independent of UI surface.
- [x] `plan` and `run` CLI entrypoints exist.
- [ ] `init`, `status`, `inspect`, `stop --checkpoint`, `resume`, `approve`, `reject`, `explain`, `budget`, and `history` behaviors.
- [ ] Human override recorded as provenance rather than silent state rewrite.

### Day-zero bootstrap

- [ ] Repository/project inventory and trust scan.
- [ ] First immutable SoftwareWorld snapshot bootstrap path.
- [ ] Initial simple/raw context baseline retained for ablation.
- [ ] Initial arena/capability baselines.
- [ ] Learned routing disabled/conservative until evidence exists.
- [ ] Forecast-value optimization disabled until calibrated.
- [ ] Skill promotion disabled until replay/holdout evidence exists.
- [ ] Quality critics cannot become authoritative while uncalibrated.
- [ ] Bootstrap exits on evidence conditions, not an arbitrary task count.

### Termination and satisficing

- [ ] `CompletionPolicy`/termination contract.
- [ ] Mandatory hard acceptance gates.
- [ ] Required mechanical goal predicates.
- [ ] Allowed unresolved uncertainty.
- [ ] Resource/spend/wall-time/retry/iteration ceilings.
- [ ] Stagnation or marginal-value stopping policy.
- [ ] Cancellation/escalation behavior.
- [ ] Subjective quality target only where human/domain policy requires it; quality never overrides failed hard gates.

### Resource scheduling

- [ ] Scheduler for CPU/RAM/disk/GPU/VRAM/sandbox/provider capacity.
- [ ] Runtime observation of free capacity and historical peak demand.
- [ ] Safety reserve, exclusivity, preemption, unload/reload, and fallback semantics.
- [ ] Large local neural/foundry workloads mutually exclusive by default on constrained single-GPU hosts until measurements prove safe concurrency.
- [ ] OOM/resource exhaustion fails workload gracefully without corrupting accepted state.

### Storage/query lifecycle

- [ ] Provenance/reachability-aware retention classes for canonical state, evidence, derived indexes, caches, rejected candidates, arena traces, and telemetry.
- [ ] Garbage collection cannot delete evidence required to reproduce accepted decisions.
- [ ] P50/P95/P99 query/context-compilation latency telemetry.
- [ ] Degradation triggers compaction/index/archive/redesign investigation rather than silent slowdown.

### Drift and surprise

- [ ] Model/runtime/context/verifier/toolchain fingerprints.
- [ ] Behavioral canary/sealed replay policy when fingerprints change.
- [ ] Expected operating envelopes and change-point/anomaly detection.
- [ ] `SurpriseEvent` preserving evidence and identifying affected assumptions/capabilities.
- [ ] Surprise handling: reproduce -> compare fingerprints/history -> quarantine/repair/rollback/escalate.

### Decision provenance

- [ ] `DecisionRecord` data model with antecedents, alternatives, selected/rejected rationale, policies, uncertainty state, expected failure modes, actor/component, and resulting effects.
- [ ] `explain` reads structured decision/evidence history; model-generated prose is summary only.

**Phase 0 exit:** Phase 1 can run without violating the trust, recovery, operator-control, bootstrap, termination, resource, retention, fingerprint, known-unknown, and explanation boundaries defined in `OPERATIONAL_CONTROL_PLANE.md`.

---

## Phase 1 — minimal Architecture v1 contracts + immutable SoftwareWorld + dual arena

### Minimal contracts

- [ ] `TaskContract`
- [ ] `ArtifactRef`
- [ ] `EvidenceRecord`
- [ ] `ProvenanceRecord`
- [ ] `CapabilityRecord`
- [ ] `PolicyDecision`
- [ ] `WorldSnapshotRef`
- [ ] `ExecutionResult`

Do not promote Mission/Job/Checkpoint/provider/parser/engine/discovery concepts into the minimal core merely for future-proofing.

### Read-only world-model seam

- [ ] Read-oriented `WorldModel` interface.
- [ ] Immutable `WorldSnapshot` with snapshot hash, source hash, toolchain fingerprint, parent snapshot, and timestamp.
- [ ] Snapshot compiler creates new state rather than mutating authoritative intelligence.

### SoftwareWorld v0

Start deliberately small:

- [ ] Git source pinned to exact commit/tree.
- [ ] One language parser/AST path.
- [ ] Symbol definitions/references.
- [ ] Import/module graph.
- [ ] Test-file to source/symbol mapping where deterministically discoverable.
- [ ] Snapshot reproducibility test.

Do **not** add SCIP, CodeQL, dynamic coverage, or failure history yet unless later ablations justify them.

### Minimal dual arena

- [ ] Trial recorder.
- [ ] Stable sealed task set.
- [ ] Living/project-derived task stream recorder.
- [ ] Rotating external/unseen task slot.
- [ ] Trial fingerprints: repo commit, world snapshot, context, cognition/runtime config, prompt/tool schema, verifier/policy, result, timing/cost/tokens/human intervention.
- [ ] Baseline reports for verified pass rate, localization precision/recall, context size, wall time, cost, and human intervention.
- [ ] Living-task provenance prevents synthetic tasks from independently promoting champions.

**Primary gate:** given a real repository plus known bug/localization tasks with known relevant/irrelevant symbols, SoftwareWorld produces reproducible snapshots and measurable localization precision/recall; the arena can replay the same trial from fingerprints.

---

## Phase 2 — Context Compiler + empirical capability/known-unknown model

### Context Compiler

- [ ] Context Compiler separate from `WorldModel`.
- [ ] Explicit token/entity budget.
- [ ] Inclusion scoring trace using measurable proxies rather than claiming calibrated utility.
- [ ] Initial proxies: task relevance, dependency distance, failing-stack proximity, test association, changed-file proximity, reference strength, historical association when available, token cost.
- [ ] Record included/excluded entities, reasons, provenance, and trust labels.
- [ ] Raw-repository baseline.
- [ ] Compiled-context challenger.
- [ ] Paired arena comparison.

Promotion uses predefined primary metrics, practical effect size, uncertainty, and safety/non-regression guardrails. If evidence is inconclusive, gather more trials rather than forcing a verdict.

### Capability / negative competence

- [ ] Capability profiles support `SUPPORTED`, `UNSUPPORTED`, `UNKNOWN`, and `CONTRADICTORY` evidence states.
- [ ] Record task features correlated with success/failure and required escalation/supervision.
- [ ] Router can reject/escalate/decompose known failure regions rather than repeatedly spending into them.
- [ ] Do not emit unsupported calibrated probabilities.

### Candidate intelligence additions after baseline

- [ ] SCIP challenger — retain only if it improves measured outcomes.
- [ ] dynamic coverage mapping challenger.
- [ ] CodeQL/data-flow challenger for relevant task classes.
- [ ] Git-history/failure-history relationships.

**Exit:** project intelligence demonstrates measurable localization/context value over simpler baselines, and the system can state where evidence supports competence, known weakness, contradiction, or ignorance.

---

## Phase 3 — heterogeneous cognition + drift-aware routing

### Provider/runtime protocol

- [ ] Narrow provider-neutral model request/result envelope.
- [ ] Provider/model/runtime/configuration fingerprinting integrated with Phase 0 drift policy.
- [ ] Behavioral canary suite.

### Initial lanes

- [x] Ollama development adapter exists.
- [ ] Local reference adapter (`llama.cpp` initially).
- [ ] One frontier challenger adapter selected from current evidence/cost/availability.
- [ ] Structured-output conformance tests.
- [ ] Provider health/rate-limit circuit breaker.
- [ ] Local/offline fallback.

### Routing baseline

- [ ] Deterministic eligibility/capability floors.
- [ ] No permanent model winner.
- [ ] Closed-loop escalation after verification failure or dependency/risk expansion.
- [ ] Sealed-arena model comparison under identical task/context/tool/verifier conditions.
- [ ] Fingerprint/drift change can invalidate competence evidence and trigger recertification.
- [ ] Resource scheduler prevents unsafe local concurrency/OOM.

**Exit:** at least one local and one frontier lane produce verifiable candidates through the same contracts, and their relative strengths/weaknesses are measured rather than assumed.

---

## Phase 4 — correctness verification + Adversarial Verification Fabric

### Correctness ladder

- [x] Python syntax/AST gate exists.
- [x] Sandbox command exit-status evidence exists.
- [ ] L0 schema/patch parser validation.
- [ ] L1 lint/type/compiler checks.
- [ ] L2 targeted existing tests.
- [ ] L3 generated regression/property tests.
- [ ] L4 risk-selected mutation/security checks.
- [ ] L5 integration/performance/resource checks.
- [ ] L6 hidden/final acceptance suite.

Verification depth is risk-adaptive. Failure can escalate required verification; it cannot silently downgrade after new risk is discovered.

### Counterexample search

- [ ] Counterexample contract.
- [ ] Hostile-input generator.
- [ ] Boundary/edge-case generator.
- [ ] Property-violation search.
- [ ] Mutation-survivor targeting.
- [ ] Concurrency/race schedule search where applicable.
- [ ] Security/exploit adversary where applicable.
- [ ] Deterministic arbiter that proves whether a proposed counterexample violates a contract.

### Adversary calibration

- [ ] Known-bug/counterexample canary corpus by failure class.
- [ ] Detection-rate, false-counterexample, cost, and coverage telemetry.
- [ ] Adversary capability profiles and class-specific downgrade/quarantine.
- [ ] Route to alternative adversarial strategies when blind spots are measured.

**Exit:** adversarial search demonstrably discovers valid failures missed by the baseline path, while its own blind spots/false positives are measured and deterministic acceptance authority remains independent.

---

## Phase 5 — Failure Compiler + reusable counterexample memory

- [ ] Structured `FailureSignature`.
- [ ] Violated contract/gate.
- [ ] Affected symbols/entities.
- [ ] Minimal reproducer/counterexample when available.
- [ ] Expected vs actual behavior.
- [ ] Dependency-radius estimate.
- [ ] Environment/toolchain/model/runtime fingerprints.
- [ ] Prior matching failures.
- [ ] Prior successful repairs.
- [ ] Link signatures to regression fixtures and project/world snapshots.
- [ ] Feed signatures to repair/context/routing without dumping raw logs unnecessarily.
- [ ] Link failures to SurpriseEvents and suspected component weaknesses without claiming causality prematurely.

**Exit:** paired arena trials show the Failure Compiler improves repair success, root-cause localization, or time-to-verified-repair over raw-log feedback without hiding critical evidence.

---

## Phase 6 — capability routing + Realized Value Ledger

### Realized value recorder

- [ ] verified task success/failure;
- [ ] dollars/API cost;
- [ ] GPU/compute consumption;
- [ ] wall-clock time;
- [ ] human intervention/time;
- [ ] future reuse actually observed;
- [ ] recurrence of known failures;
- [ ] capability gained/lost/quarantined.

### Forecast value

- [ ] Forecast records separated from realized records.
- [ ] Assumptions attached to every forecast.
- [ ] Calibration status attached to forecast models.
- [ ] No false-precision NPV claims from uncalibrated estimates.

### Capability router

- [ ] Capability history by task class and fingerprinted lane.
- [ ] Positive/negative/unknown/contradictory competence influences acceptance/routing.
- [ ] Route on empirical competence + risk + reversibility + current budget.
- [ ] Use expected value only after realized history is sufficient to calibrate it.
- [ ] Escalate when observed evidence invalidates the initial route.
- [ ] Every consequential route emits a `DecisionRecord`.

**Exit:** VPI-CVM can explain a route from measured capability/weakness, risk, resources, uncertainty, and realized history rather than prestige or simplistic $/token minimization.

---

## Phase 7 — Verified Skill Compiler + Living Benchmark generator

### Skill compiler and retirement

- [ ] Fingerprint repeated verified operations.
- [ ] `NEURAL -> REPEATED_VERIFIED -> SHADOW_DETERMINISTIC -> VALIDATED -> ACTIVE` promotion lifecycle.
- [ ] `SUSPECT -> QUARANTINED -> RETIRED` degradation path.
- [ ] Revalidation path when new evidence supports return.
- [ ] Historical replay.
- [ ] Sealed/rotating holdout replay.
- [ ] Adversarial replay using known counterexamples.
- [ ] Toolchain/project-contract/distribution invalidation.
- [ ] Health checks, last-verification evidence, and regression sampling.
- [ ] Rollback/quarantine.

### Living benchmark

- [ ] Generate bounded synthetic tasks from current project graph/world snapshots.
- [ ] Generate changed-symbol regression probes.
- [ ] Generate test-gap/dependency-impact probes.
- [ ] Generate adversarial practice tasks where a deterministic fitness function exists.
- [ ] Background budgets and cancellation.
- [ ] No mutation of accepted state from background practice.
- [ ] Living-task provenance label prevents synthetic tasks from independently promoting champions.

**Exit:** repeated verified work produces at least one shadowed deterministic capability whose promotion preserves correctness/quality under historical and sealed replay, and retirement/quarantine can remove a degraded skill safely.

---

## Phase 8 — human intent/value + goal conformance + quality calibration

### Intent/value contract

- [ ] Explicit objective and non-goals.
- [ ] Mechanical hard constraints.
- [ ] Interpretive preferences/taste criteria.
- [ ] Reversible vs irreversible decisions.
- [ ] Examples of accepted/rejected outcomes.
- [ ] Unresolved ambiguities and authority boundaries.
- [ ] Human override as provenance event.

### Goal conformance

- [ ] Mechanical constraints produce hard PASS/FAIL only where deterministically checkable.
- [ ] Interpretive constraints produce evidence-backed assessment, not fake binary truth.

### Quality assessment and calibration

- [ ] Advisory `QualityAssessment` interface.
- [ ] Calibration status: UNCALIBRATED / WEAK / CALIBRATED.
- [ ] Evidence/conflict reporting.
- [ ] Human review/variant-comparison recommendation.
- [ ] Held-out human-rating calibration loop.
- [ ] Promotion criteria use coverage, agreement, held-out prediction/calibration error, and distribution shift rather than arbitrary rating counts.
- [ ] No confidence intervals/numeric probability precision until calibration supports them.

**Exit:** VPI-CVM preserves/enforces human intent without conflating subjective taste with machine-defensible correctness, and the critic can state the scope in which its calibration is supported.

---

## Phase 9 — full SoftwareWorld lifecycle: intent -> observe

Lifecycle:

1. **Design** — resolve intent/constraints and define acceptance evidence.
2. **Plan** — deterministic task/dependency decomposition with impact analysis.
3. **Build** — context-compiled neural/deterministic leaf execution in isolated candidate workspaces.
4. **Test** — targeted/generated behavioral evidence.
5. **Verify** — correctness, mechanical goal conformance, adversarial counterexamples, advisory quality where applicable.
6. **Publish** — immutable artifact promotion/deployment with rollback plan.
7. **Observe** — runtime telemetry/incidents/feedback/environment data back into project intelligence.

Required infrastructure:

- [ ] Isolated Git worktree per candidate/task group.
- [ ] Atomic accepted checkpoint and rejected-worktree discard.
- [ ] Rollback to last accepted checkpoint.
- [ ] SWE-ReX or equivalent execution interface.
- [ ] gVisor/runsc hardened backend where compatible.
- [ ] Firecracker/microVM high-assurance tier where infrastructure permits.
- [ ] Task-scoped network allowlists and short-lived secrets.
- [ ] Durable long-run workflow backend protocol.
- [ ] Temporal adapter or evidence-backed equivalent rather than a bespoke fake scheduler.
- [ ] Typed world/production telemetry ingestion.
- [ ] Survival modes: FULL / DEGRADED / SAFE_LOCAL / RECOVERY / READ_ONLY.
- [ ] Operator approval/escalation only where policy/authority requires it.
- [ ] CompletionPolicy enforced end-to-end so autonomous runs have explicit done/stop/escalate semantics.
- [ ] Publication provenance/license/dependency policy before autonomous external release.

**Exit:** one real software project can move from intent through published/observed artifact with reproducible evidence, bounded termination, rollback, and post-deployment feedback.

---

## Phase 10 — second domain + cross-domain transfer research

Do not build a Meta-World transfer engine before domain pressure exists.

### Second domain

- [ ] Select GameWorld or another domain based on actual project goals.
- [ ] Implement its own ontology/world model rather than renaming software symbols.
- [ ] Define domain-specific correctness signals.
- [ ] Define mechanical goal-conformance checks.
- [ ] Define advisory quality signals and human calibration path.
- [ ] Define domain-specific adversaries/simulators only where outputs can be evaluated defensibly.

### Meta-World research seam

- [ ] Mine structural pattern **candidates** from at least two mature domains.
- [ ] Record source-domain evidence and target-domain assumptions.
- [ ] Transfer only in shadow mode.
- [ ] Validate under target-domain verification and arena.
- [ ] Detect negative transfer.
- [ ] Promote reusable cross-domain abstractions only after repeated target-domain evidence.

**Exit:** cross-domain transfer is demonstrated empirically, or the candidate abstraction remains research. Source-domain success never automatically confers target-domain competence.

---

## Phase 11+ — Metacognitive Discovery Plane / architectural self-research

Do not implement this before the system has mature reproducible measurements to research against. See `DISCOVERY_PLANE.md`.

### Self-model and architectural uncertainty

- [ ] System graph of VPI-CVM components, versions, dependencies, responsibilities, costs, competence, failures, and change history.
- [ ] Architectural hypothesis/uncertainty registry with supporting/contradicting evidence and next-best experiment.

### Weakness mining and hypothesis generation

- [ ] Cluster failure/surprise/operator/cost/regression evidence into candidate system weaknesses.
- [ ] Attribute suspected component responsibility as a hypothesis, not truth.
- [ ] Generate falsifiable architectural interventions with predictions, competing explanations, experiment designs, falsification conditions, cost/risk, and rollback.

### Open-world ResearchWorld

- [ ] Provenance/trust-aware ingestion of papers, repositories, benchmarks, model/runtime changes, postmortems, algorithms, production incidents, and human challenges.
- [ ] Generate novel pressure beyond tasks already represented in the project graph.

### Architecture search / Meta-Compiler

- [ ] Controlled replacement/removal/topology/routing/representation/verifier/adversary candidate mutations.
- [ ] Explicit system manifest for every architectural challenger.

### System worktrees and shadow laboratory

- [ ] Isolated VPI-CVM system worktree/build per challenger.
- [ ] Champion/control and challengers share matched tasks/budgets/harnesses.
- [ ] Shadow systems cannot mutate accepted production/project truth.
- [ ] Controlled A/B/ablation experiments.
- [ ] Causal/intermediate-metric analysis and confound checks.

### Scientific memory

- [ ] Persist supported/falsified/inconclusive hypotheses, negative results, conditions, interactions/confounds, promotion/rollback history, and unresolved questions.

### Meta-governor

- [ ] Allocate production vs research resources from priority, deadline, incident state, value-of-information, reversibility, idle capacity, and research backlog.
- [ ] Research is cancellable/preemptible and cannot consume safety-critical production capacity.

### Safe recursive improvement governance

- [ ] Champion cannot rewrite itself in place.
- [ ] Architectural candidate -> focused tests -> living arena -> sealed arena -> adversarial/security/recovery checks -> promotion or rejection.
- [ ] Preserve prior champion and tested migration/rollback path.
- [ ] Critical self-modification can require operator approval even when metrics improve.

### Learning-velocity measurement

- [ ] Measure time from surprise/failure to testable hypothesis.
- [ ] Measure time to falsification and validated improvement.
- [ ] Measure human research effort, recurrence of understood failures, and information gained per constrained resource.
- [ ] Do not collapse research quality into one Goodhart-prone scalar.

**Exit:** VPI-CVM can propose and isolate a structural change to itself, test it against a stable champion under reproducible conditions, explain the measured effect and uncertainty, and promote/rollback safely without direct self-rewrite.

---

## Ongoing platform hardening

These workstreams span phases and remain mandatory before strong production claims:

- storage schema migrations and crash/power-loss tests;
- stale-cache/snapshot regression corpus;
- provider outage/rate-limit/drift/surprise fault injection;
- sandbox escape/security regression corpus;
- prompt-injection/trust-boundary regression corpus;
- model behavioral canaries and quarantine;
- adversary calibration canaries;
- skill-regression retirement/rollback tests;
- query/context latency health telemetry and scaling experiments;
- OpenTelemetry/structured event stream;
- cost/value/capability/known-unknown dashboards;
- 24-hour, 7-day, and eventually longer supervised endurance tests;
- reproducible release packaging;
- threat-model review;
- publication/IP policy before autonomous external release.

## Final acceptance doctrine

VPI-CVM does not earn claims such as "autonomous," "self-improving," "economically rational," "cross-domain," "self-discovering," or "world-leading" from architecture diagrams.

Those claims require reproducible evidence from the appropriate arena, holdout, real-world observation, ablation, recovery, security, and failure-mode tests.

The objective is not benchmark victory or local-model purity. It is:

> **maximize verified, goal-correct, reusable capability accumulated per unit of human time, machine compute, and experience while keeping the system falsifiable, recoverable, and under human authority.**
