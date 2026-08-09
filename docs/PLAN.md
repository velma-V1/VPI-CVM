# VPI-CVM Implementation Plan

This is the governing build plan. A checked item means the capability exists in the repository; it does **not** imply the entire system is production complete.

The target is now explicitly hybrid: VPI-CVM keeps the industrial execution/verification chassis while adding compounding project intelligence, cache invalidation, failure compilation, and cost-aware model escalation. The system must improve from repeated verified work without becoming dependent on stale neural state or uncontrolled cloud spend.

## Phase 0 — truth boundaries and repository foundation

- [x] Define model as proposal generator, not verifier.
- [x] Define deterministic evidence as acceptance authority.
- [x] Establish validated domain schemas.
- [x] Establish test-first CI foundation.
- [x] Document security posture and non-goals.
- [ ] Define epistemic labels for MEASURED / DERIVED / INFERRED / HEURISTIC / UNKNOWN claims.
- [ ] Reject unsupported calibrated probabilities and benchmark claims at output boundaries.

**Exit condition:** architecture can no longer silently substitute LLM opinion, stale memory, or unsupported probability for verification.

## Phase 1 — durable project truth and provenance

- [x] SQLite WAL journal.
- [x] explicit task state machine.
- [x] evidence persistence.
- [x] dependency DAG validation.
- [x] cycle/unknown-dependency rejection.
- [x] resumable ready-task dispatch.
- [ ] event/outbox table for external observers.
- [ ] schema migrations/version table.
- [ ] evidence/artifact content hashes.
- [ ] immutable accepted-base commit recorded for every task.
- [ ] append-only decision chronicle.
- [ ] project-state lineage across accepted/rejected branches.
- [ ] evidence provenance graph linking task -> context -> candidate -> gate -> result -> commit.

**Exit condition:** restart cannot lose accepted task state, passed tasks cannot be regenerated accidentally, and every accepted output can be traced to its inputs and evidence.

## Phase 2 — safe workspace and execution boundary

- [x] canonical path containment.
- [x] nested target paths preserved.
- [x] Docker execution backend.
- [x] read-only project mount during validation.
- [x] network disabled by default.
- [x] capabilities dropped / no-new-privileges.
- [x] PID/RAM/CPU/wall-time limits.
- [x] timeout kill/remove cleanup.
- [x] no in-process execution of generated code.
- [ ] SWE-ReX execution adapter.
- [ ] disk quota.
- [ ] VPI-CVM-owned seccomp profile.
- [ ] gVisor/runsc backend.
- [ ] Firecracker/microVM high-assurance backend.
- [ ] task-scoped network allowlists.
- [ ] short-lived task-scoped secret injection.

**Exit condition:** generated code cannot execute inside the controller, mutate canonical project state during validation, escape its resource envelope, or receive ambient host credentials.

## Phase 3 — Project Intelligence Fabric

Build exact code intelligence before generic RAG.

- [ ] Tree-sitter incremental syntax ingestion.
- [ ] SCIP ingestion for definitions/references/implementations.
- [ ] language-native compiler/type metadata adapters where stronger than generic parsing.
- [ ] import/package/build-target graph.
- [ ] caller/callee graph.
- [ ] test-to-symbol mapping.
- [ ] dynamic coverage-to-symbol mapping.
- [ ] Git blame/history/recent-diff relationships.
- [ ] failure-history links to symbols and commits.
- [ ] on-demand CodeQL/data-flow relationships.
- [ ] compact per-symbol summaries with source provenance.
- [ ] content-addressed project graph snapshots.
- [ ] incremental invalidation when source/dependencies/tests/configuration change.

**Exit condition:** VPI-CVM can answer which exact symbols, tests, dependencies, recent changes, and historical failures are relevant to a task without asking a model to reconstruct repository relationships from prose.

## Phase 4 — Context Compiler and cache hierarchy

- [ ] bounded task context contract.
- [ ] exact source ranges/signatures/callers/callees/tests included with provenance.
- [ ] token/context budget enforcement.
- [ ] semantic retrieval limited to prose/docs or recall expansion; never authoritative for code relations.
- [ ] context cache keyed by repository/content hash + task contract + toolchain version.
- [ ] model prefix-cache integration where runtime supports it.
- [ ] summary cache invalidation by dependency radius.
- [ ] cognitive result cache for repeated verified task patterns.
- [ ] cache entries carry verification-policy and model/runtime fingerprints.
- [ ] stale cache rejection when any fingerprint changes.

**Exit condition:** repeated work reuses validated project intelligence cheaply, while changed code or policies cannot silently consume stale summaries or neural state.

## Phase 5 — deterministic workflow brain and failure compiler

Workflow topology is code, not model discretion.

- [ ] bugfix FSM: reproduce -> localize -> hypothesize -> patch -> verify -> adversarial verify -> checkpoint.
- [ ] feature FSM: contract -> impact analysis -> failing test -> implementation -> integration verify -> adversarial verify -> checkpoint.
- [ ] refactor FSM: baseline -> dependency map -> transform -> equivalence -> performance gate -> checkpoint.
- [ ] security FSM: boundary map -> reproduce -> patch -> exploit regression -> security/data-flow/dependency gates -> checkpoint.
- [ ] migration FSM with rollback and data-integrity gates.
- [ ] bounded backtracking by failure class.
- [ ] decomposition trigger after repeated localization/repair failure.
- [ ] structured failure compiler that converts raw logs into minimal counterexamples.
- [ ] failure signatures cached and linked to successful repair strategies.

**Exit condition:** models populate typed leaf nodes but cannot skip mandatory stages; repeated failures become structured reusable knowledge instead of repeated prompt text.

## Phase 6 — model portfolio, competence envelope, and budget governor

Do not assume a router can know task difficulty perfectly before execution.

- [x] Ollama structured planner adapter.
- [x] JSON-schema/Pydantic validation.
- [x] Ollama structured artifact generator.
- [x] deterministic temperature setting.
- [x] unload model after request by default.
- [x] prior machine evidence supplied to repair attempts.
- [ ] first-party provider adapter protocol.
- [ ] local llama.cpp adapter.
- [ ] SGLang server adapter.
- [ ] frontier provider adapters behind capability negotiation.
- [ ] model/runtime capability registry.
- [ ] sealed-arena empirical performance table by task class.
- [ ] hard capability floors for security/concurrency/migrations/public-API changes.
- [ ] uncertainty score for every route.
- [ ] cheap-first execution only when confidence and reversibility permit it.
- [ ] automatic escalation after verification failure or unexpected dependency expansion.
- [ ] local/offline fallback lane when providers are unavailable.
- [ ] per-task token, dollar, GPU-time, wall-time, and candidate-count budgets.
- [ ] global session/project budget governor.
- [ ] provider health/rate-limit circuit breakers.

**Exit condition:** routing is empirical and conservative, bad initial routing self-corrects through verification/escalation, and cloud/provider failure cannot collapse the system.

## Phase 7 — adaptive Verification Forge

Verification is tiered by measured risk; the full stack is not run blindly on every candidate.

### Level 0 — envelope / syntax
- [x] Python AST gate.
- [x] sandbox command gate.
- [x] required-gate acceptance policy.
- [ ] schema/patch parser validation.

### Level 1 — fast static checks
- [ ] Ruff gate.
- [ ] Mypy/Pyright gate.
- [ ] compiler/type equivalent gates for other languages.

### Level 2 — targeted behavior
- [ ] pytest evidence parser.
- [ ] independent regression-test author stage.
- [ ] changed-symbol targeted test selection.

### Level 3 — adversarial behavior
- [ ] Hypothesis/property-test gate.
- [ ] boundary/counterexample generation.
- [ ] concurrency-specific checks where applicable.

### Level 4 — robustness/security
- [ ] risk-selected mutation testing.
- [ ] Semgrep gate.
- [ ] CodeQL/data-flow gate.
- [ ] dependency vulnerability audit.
- [ ] exploit-regression tests for security fixes.

### Level 5 — system behavior
- [ ] integration/contract-test gate.
- [ ] migration/data-integrity gate.
- [ ] performance/resource regression gate.

### Level 6 — final acceptance
- [ ] full risk-selected suite.
- [ ] hidden/adversarial acceptance tests.
- [ ] artifact-type gate registry for non-code outputs.

### Adaptive policy
- [ ] deterministic risk classifier from touched files, dependency radius, coverage, concurrency, security boundaries, API/state changes, and prior failures.
- [ ] verification level can only escalate automatically, never silently downgrade after a failure.
- [ ] cheap candidate screening before expensive mutation/CodeQL/full-integration gates.
- [ ] verification-cost telemetry feeds routing and candidate-count decisions.

**Exit condition:** "runs without exception" is insufficient, but simple work does not pay the cost of maximum verification unless risk or evidence requires escalation.

## Phase 8 — candidate isolation, competition, and rollback

- [ ] isolated Git worktree per mutable candidate/task group.
- [ ] atomic accepted-artifact checkpoint.
- [ ] rejected worktree discard.
- [ ] rollback to last accepted checkpoint.
- [ ] provenance manifest attached to commit.
- [ ] merge conflict classifier and escalation path.
- [ ] candidate tournament engine from identical accepted base/context.
- [ ] candidate count chosen from uncertainty and remaining budget, not fixed fan-out.
- [ ] deterministic winner selection from mandatory gates, hidden tests, regressions, mutation/coverage, API/dependency impact, performance, then patch complexity.

**Exit condition:** failed candidates cannot contaminate accepted state, and expensive multi-model competition happens only when expected value exceeds cost.

## Phase 9 — Verified Skill Compiler and compounding intelligence

- [ ] fingerprint verified operations by task pattern + AST/context signature + transformation + evidence.
- [ ] skill registry lifecycle: NEURAL -> REPEATED_VERIFIED -> SHADOW_DETERMINISTIC -> VALIDATED_SKILL -> DETERMINISTIC.
- [ ] replay against historical examples before promotion.
- [ ] held-out adversarial validation before promotion.
- [ ] deterministic skill forms: ast-grep/tree-sitter rewrite, script, template, analyzer, test generator.
- [ ] automatic invalidation when language/toolchain/project contract changes.
- [ ] failure-to-skill linkage: known counterexamples become permanent regression guards.
- [ ] usage statistics and rollback for degraded skills.

**Exit condition:** repeated verified work reduces future neural calls and latency without turning unverified model outputs into permanent automation.

## Phase 10 — sealed arena and continuous empirical routing

- [ ] private task corpus from real repositories plus SWE-smith-style generated tasks.
- [ ] hidden tests inaccessible to candidate models.
- [ ] contamination controls and rotating repositories.
- [ ] same context/tools/time/budget/verifier across competing models.
- [ ] ablation runs for project graph, cache, skill compiler, router, and verification tiers.
- [ ] metrics: verified pass@1, hidden-test pass, regressions, time, cost, tokens, GPU time, retries, context size, operator intervention.
- [ ] champion/challenger promotion rules for models, runtimes, retrieval methods, and verification policies.
- [ ] no component promoted on vendor/public benchmark alone.

**Exit condition:** "best" is a measured local property of a task class under VPI-CVM's exact harness, not a permanent vendor/model claim.

## Phase 11 — durable long-run orchestration

Do not build a bespoke fake-Temporal scheduler.

- [ ] define workflow backend protocol.
- [ ] implement Temporal adapter.
- [ ] workflow replay/recovery tests.
- [ ] bounded retries by fault class.
- [ ] lifecycle wall-clock budget.
- [ ] global resource/token/cost budget integration.
- [ ] pause/resume/cancel controls.
- [ ] operator escalation queue.

**Exit condition:** controller process or machine restarts can resume multi-day work from workflow history and persisted project truth.

## Phase 12 — richer execution agents

Do not rebuild a full coding agent if an existing one satisfies the contract.

- [ ] OpenHands agent-server adapter.
- [ ] capability negotiation between direct runner and agent backend.
- [ ] tool permission policy.
- [ ] per-task clean agent context.
- [ ] evidence extraction from agent execution.
- [ ] backend conformance tests.

**Exit condition:** VPI-CVM can supervise a mature agent backend without surrendering planning policy, budgets, project truth, or final acceptance authority.

## Phase 13 — hardware health and scheduling

- [x] NVIDIA telemetry probe.
- [x] real temperature threshold policy primitive.
- [ ] integrate thermal guard into inference scheduling.
- [ ] VRAM pressure thresholds.
- [ ] power/temperature history.
- [ ] model unload verification telemetry.
- [ ] CPU/RAM/disk host watchdogs.
- [ ] adaptive cooldown and backpressure.
- [ ] runtime auto-benchmarking for llama.cpp/SGLang/vLLM/TensorRT-LLM where applicable.

**Exit condition:** long-run scheduling responds to measured hardware state and runtime performance, not fixed sleeps or static assumptions.

## Phase 14 — observability and operator control

- [ ] structured event stream.
- [ ] task/evidence/timeline API.
- [ ] Prometheus/OpenTelemetry exporter.
- [ ] lightweight dashboard.
- [ ] manual approve/reject/retry controls.
- [ ] policy override audit log.
- [ ] alerts for stuck, unsafe, provider-degraded, or budget-exhausted work.
- [ ] live cost/latency/model-route/verification-level telemetry.

## Phase 15 — production hardening and endurance

- [ ] migration tests.
- [ ] crash/power-loss fault injection.
- [ ] provider outage/rate-limit fault injection.
- [ ] stale-cache/invalidation regression corpus.
- [ ] sandbox breakout regression corpus.
- [ ] skill-regression rollback tests.
- [ ] 24h soak test.
- [ ] 7-day soak test.
- [ ] 30-day supervised endurance test.
- [ ] recovery-time and data-loss measurements.
- [ ] threat-model review.
- [ ] reproducible release packaging.

**Final acceptance:** VPI-CVM earns long-duration or world-leading claims only after sealed-arena, ablation, endurance, recovery, cost, and failure-mode evidence exists.
