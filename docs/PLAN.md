# VPI-CVM Implementation Plan

Status: **governing build plan for Architecture v1**.

A checked item means the capability exists in the repository. It does **not** imply the target system is complete. The current Python code is an executable foundation; Architecture v1 adds a resident, self-measuring, adversarially tested intelligence layer without falsely claiming unfinished capabilities.

## Development laws

1. **Arena first.** Substantial mechanisms require a baseline, challenger measurement, and explicit retain/reject/inconclusive decision.
2. **Canonical knowledge is immutable/versioned.** New source/project intelligence produces new snapshots and hashes. Ephemeral operational state may mutate transactionally but never rewrites historical truth.
3. **Three epistemic planes.** Correctness is hard where mechanically defensible; goal conformance is hard only for mechanical predicates; subjective quality remains advisory until calibrated.
4. **Explicit state is the resident brain.** KV/prefix caches may accelerate inference but are never authoritative memory.
5. **Models are replaceable resources.** Local and frontier models remain permanent eligible lanes selected by evidence and value, not ideology.
6. **Living evaluation does not judge itself.** Synthetic/living tasks drive surveillance/practice; sealed and rotating holdouts govern promotion/generalization.
7. **Adversaries discover counterexamples; deterministic arbiters decide whether they break a candidate.**
8. **Measure realized value before optimizing forecast value.** Human time, failure recurrence, reuse, cost, compute, and latency all matter.
9. **No arbitrary architectural numerology.** Fixed task counts, p-values, token savings, or promotion thresholds are experiment parameters, not universal laws.
10. **Cross-domain abstractions are discovered, not invented.** SoftwareWorld is first; Meta-World transfer waits for multiple mature domains.
11. **V31M4 is independent.** Any bridge is optional interoperability and cannot become a VPI-CVM kernel dependency.

---

## Phase 0 — preserve and harden the executable foundation

Existing foundation:

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
- [ ] Schema migration/version table for durable storage.
- [ ] Content hashes for evidence and produced artifacts.
- [ ] Immutable accepted-base commit recorded for every mutable candidate.
- [ ] Append-only decision/provenance record.
- [ ] Reproducibility fingerprint envelope for model/runtime/prompt/verifier/toolchain configuration.
- [ ] Epistemic labels for MEASURED / DERIVED / INFERRED / HEURISTIC / UNKNOWN claims where the system emits quantitative assertions.

**Exit:** existing tested behavior remains usable, but every future Architecture v1 experiment can be reproduced and traced to immutable inputs and evidence.

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

Do not promote Mission/Job/Checkpoint/provider/parser/engine concepts into the minimal core merely for future-proofing.

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

Do **not** add SCIP, CodeQL, dynamic coverage, or failure history yet unless their later ablations justify them.

### Minimal dual arena

- [ ] Trial recorder.
- [ ] Stable sealed task set.
- [ ] Living/project-derived task stream recorder.
- [ ] Rotating external/unseen task slot.
- [ ] Trial fingerprints: repo commit, world snapshot, context, model/runtime/config, prompt/tool schema, verifier/policy, result, timing/cost/tokens/human intervention.
- [ ] Baseline reports for verified pass rate, localization precision/recall, context size, wall time, cost, and human intervention.

**Primary gate:** given a real repository plus known bug/localization tasks with known relevant and irrelevant symbols, SoftwareWorld produces reproducible snapshots and measurable localization precision/recall; the arena can replay the same trial from fingerprints.

---

## Phase 2 — independent Context Compiler + ground-truth localization experiment

- [ ] Context Compiler separate from `WorldModel`.
- [ ] Explicit token/entity budget.
- [ ] Inclusion scoring trace using measurable proxies rather than claiming calibrated utility.
- [ ] Initial proxies: task relevance, dependency distance, failing-stack proximity, test association, changed-file proximity, reference strength, historical association when available, token cost.
- [ ] Record included/excluded entities and reasons.
- [ ] Raw-repository baseline.
- [ ] Compiled-context challenger.
- [ ] Paired arena comparison.

Promotion uses a predefined primary metric, practical effect size, uncertainty, and safety/non-regression guardrails. If evidence is inconclusive, gather more trials rather than forcing a verdict.

Candidate additions after the baseline exists:

- [ ] SCIP challenger — only retain if it improves measured localization/solution outcomes.
- [ ] dynamic coverage mapping challenger.
- [ ] CodeQL/data-flow challenger for task classes where deep data flow is relevant.
- [ ] Git-history/failure-history relationships.

**Exit:** project intelligence demonstrates measurable localization/context value over simpler retrieval baselines, or the representation is revised before more architecture is layered on it.

---

## Phase 3 — heterogeneous cognition: local model + frontier challenger

### Provider/runtime protocol

- [ ] Narrow provider-neutral model request/result envelope.
- [ ] Provider/model/runtime/configuration fingerprinting.
- [ ] Behavioral canary suite for drift detection.

### Initial lanes

- [x] Ollama development adapter exists.
- [ ] Local reference adapter (`llama.cpp` initially).
- [ ] One frontier challenger adapter (initial provider chosen by current evidence/cost/availability).
- [ ] Structured-output conformance tests.
- [ ] Provider health/rate-limit circuit breaker.
- [ ] Local/offline fallback.

### Routing baseline

- [ ] Deterministic eligibility/capability floors.
- [ ] No permanent model winner.
- [ ] Closed-loop escalation after verification failure or discovered dependency/risk expansion.
- [ ] Sealed-arena model comparison under identical task/context/tool/verifier conditions.

**Exit:** at least one local and one frontier lane can produce verifiable candidates through the same contracts, and their relative strengths are measured rather than assumed.

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
- [ ] Hostile input generator.
- [ ] Boundary/edge-case generator.
- [ ] Property-violation search.
- [ ] Mutation survivor targeting.
- [ ] Concurrency/race schedule search when applicable.
- [ ] Security/exploit adversary when applicable.
- [ ] Deterministic arbiter that proves whether a proposed counterexample violates a contract.
- [ ] Adversary and generator separation where useful.

Adversarial search is a **counterexample discovery engine**, not an independent truth authority.

**Exit:** counterexample search demonstrably discovers valid failures missed by the baseline verification path on at least one measured task class without replacing deterministic acceptance authority.

---

## Phase 5 — Failure Compiler + reusable counterexample memory

- [ ] Structured `FailureSignature`.
- [ ] Violated contract/gate.
- [ ] Affected symbols/entities.
- [ ] Minimal reproducer/counterexample when available.
- [ ] Expected vs actual behavior.
- [ ] Dependency radius estimate.
- [ ] Environment/toolchain/model/runtime fingerprints.
- [ ] Prior matching failures.
- [ ] Prior successful repairs.
- [ ] Link failure signatures to regression fixtures and project/world snapshots.
- [ ] Feed signatures to repair/context/routing without dumping raw logs unnecessarily.

**Exit:** paired arena trials show the Failure Compiler improves repair success, root-cause localization, or time-to-verified-repair over raw-log feedback without hiding critical evidence.

---

## Phase 6 — capability routing + Realized Value Ledger

### Realized value recorder

Record before optimizing:

- [ ] verified task success/failure.
- [ ] dollars/API cost.
- [ ] GPU/compute consumption.
- [ ] wall-clock time.
- [ ] human intervention/time.
- [ ] future reuse actually observed.
- [ ] recurrence of known failures.
- [ ] capability gained/lost/quarantined.

### Forecast value

- [ ] Forecast records separated from realized records.
- [ ] Assumptions attached to every forecast.
- [ ] Calibration status attached to forecast models.
- [ ] No false-precision NPV claims from uncalibrated estimates.

### Capability router

- [ ] Capability history by task class and fingerprinted lane.
- [ ] Route on empirical competence + risk + reversibility + current budget.
- [ ] Use expected value only after realized history is sufficient to calibrate it.
- [ ] Escalate when observed evidence invalidates the initial route.

**Exit:** VPI-CVM can explain a route in terms of measured capability, risk, resource budget, and realized history rather than model prestige or simplistic $/token minimization.

---

## Phase 7 — Verified Skill Compiler + Living Benchmark generator

### Skill compiler

- [ ] Fingerprint repeated verified operations.
- [ ] `NEURAL -> REPEATED_VERIFIED -> SHADOW_DETERMINISTIC -> VALIDATED_SKILL -> DETERMINISTIC` lifecycle.
- [ ] Historical replay.
- [ ] Sealed/rotating holdout replay.
- [ ] Adversarial replay using known counterexamples.
- [ ] Toolchain/project-contract invalidation.
- [ ] Health checks and regression sampling.
- [ ] Rollback/quarantine.

### Living benchmark

- [ ] Generate bounded synthetic tasks from current project graph/world snapshots.
- [ ] Generate changed-symbol regression probes.
- [ ] Generate test-gap and dependency-impact probes.
- [ ] Generate adversarial practice tasks where a deterministic fitness function exists.
- [ ] Background budgets and cancellation.
- [ ] No mutation of accepted state from background practice.
- [ ] Living-task provenance label prevents synthetic tasks from independently promoting champions.

**Exit:** repeated verified work produces at least one shadowed deterministic capability whose promotion preserves quality/correctness under historical and sealed replay, while the Living Arena detects at least one real regression/blind spot without becoming its own judge.

---

## Phase 8 — human intent/value state + goal conformance + quality calibration

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

### Quality assessment

- [ ] Advisory `QualityAssessment` interface.
- [ ] Calibration status: UNCALIBRATED / WEAK / CALIBRATED.
- [ ] Evidence/conflict reporting.
- [ ] Human review/variant-comparison recommendation.
- [ ] Human-rating calibration loop.
- [ ] No confidence intervals or numeric probability precision until calibration supports them.

**Exit:** VPI-CVM can preserve and enforce human intent without conflating subjective taste with machine-defensible correctness.

---

## Phase 9 — full SoftwareWorld lifecycle: intent -> observe

Lifecycle stages:

1. **Design** — resolve intent/constraints and define acceptance evidence.
2. **Plan** — deterministic task/dependency decomposition with impact analysis.
3. **Build** — context-compiled neural/deterministic leaf execution in isolated candidate workspaces.
4. **Test** — targeted and generated behavioral evidence.
5. **Verify** — correctness, mechanical goal conformance, adversarial counterexamples, advisory quality where applicable.
6. **Publish** — immutable artifact promotion/deployment with rollback plan.
7. **Observe** — ingest runtime telemetry, incidents, feedback, and environment data back into project intelligence.

Required infrastructure:

- [ ] Isolated Git worktree per candidate/task group.
- [ ] Atomic accepted checkpoint and rejected-worktree discard.
- [ ] Rollback to last accepted checkpoint.
- [ ] SWE-ReX or equivalent execution interface.
- [ ] gVisor/runsc default hardened backend where compatible.
- [ ] Firecracker/microVM high-assurance tier where infrastructure permits.
- [ ] Task-scoped network allowlists and short-lived secrets.
- [ ] Durable long-run workflow backend protocol.
- [ ] Temporal adapter or evidence-backed equivalent rather than a bespoke fake scheduler.
- [ ] Typed world/production telemetry ingestion.
- [ ] Survival modes: FULL / DEGRADED / SAFE_LOCAL / RECOVERY / READ_ONLY.
- [ ] Operator approval/escalation only where policy/authority requires it.

**Exit:** one real software project can move from intent through published/observed artifact with reproducible evidence, rollback, and post-deployment feedback. This is the first full-domain acceptance milestone.

---

## Phase 10 — second domain + cross-domain transfer research

Do not build a Meta-World transfer engine before domain pressure exists.

### Second domain

- [ ] Select GameWorld or another domain based on actual project goals.
- [ ] Implement its own ontology/world model rather than renaming software symbols.
- [ ] Define domain-specific correctness signals.
- [ ] Define mechanical goal-conformance checks.
- [ ] Define advisory quality signals and human calibration path.
- [ ] Define domain-specific adversaries/simulators only where their outputs can be evaluated defensibly.

### Meta-World research seam

- [ ] Mine structural pattern **candidates** from at least two mature domains.
- [ ] Record source-domain evidence and target-domain assumptions.
- [ ] Transfer only in shadow mode.
- [ ] Validate under target-domain verification and arena.
- [ ] Detect negative transfer.
- [ ] Promote reusable cross-domain abstractions only after repeated target-domain evidence.

**Exit:** cross-domain transfer is demonstrated empirically, or the candidate abstraction remains research. Source-domain success never automatically confers target-domain competence.

---

## Ongoing platform hardening

These workstreams span phases and remain mandatory before strong production claims:

- storage schema migrations and crash/power-loss tests;
- stale-cache/snapshot regression corpus;
- provider outage/rate-limit/drift fault injection;
- sandbox escape/security regression corpus;
- model behavioral canaries and quarantine;
- skill-regression rollback tests;
- OpenTelemetry/structured event stream;
- cost/value/capability dashboards;
- 24-hour, 7-day, and eventually longer supervised endurance tests;
- reproducible release packaging;
- threat-model review.

## Final acceptance doctrine

VPI-CVM does not earn claims such as "autonomous," "self-improving," "economically rational," "cross-domain," or "world-leading" from architecture diagrams.

Those claims require reproducible evidence from the appropriate arena, holdout, real-world observation, ablation, recovery, and failure-mode tests.

The objective is not benchmark victory or local-model purity. It is:

> **maximize verified, goal-correct, reusable capability accumulated per unit of human time, machine compute, and experience.**
