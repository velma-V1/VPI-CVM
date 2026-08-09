# VPI-CVM Implementation Plan

This is the governing build plan. A checked item means the capability exists in the repository; it does **not** imply the entire system is production complete.

## Phase 0 — truth boundaries and repository foundation

- [x] Define model as proposal generator, not verifier.
- [x] Define deterministic evidence as acceptance authority.
- [x] Establish validated domain schemas.
- [x] Establish test-first CI foundation.
- [x] Document security posture and non-goals.

**Exit condition:** architecture can no longer silently substitute LLM opinion for verification.

## Phase 1 — durable local state and task graph

- [x] SQLite WAL journal.
- [x] explicit task state machine.
- [x] evidence persistence.
- [x] dependency DAG validation.
- [x] cycle/unknown-dependency rejection.
- [x] resumable ready-task dispatch.
- [ ] event/outbox table for external observers.
- [ ] schema migrations/version table.
- [ ] evidence/artifact content hashes.

**Exit condition:** restart cannot lose accepted task state or cause passed tasks to be regenerated.

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
- [ ] disk quota.
- [ ] seccomp profile owned by VPI-CVM.
- [ ] gVisor backend evaluation.
- [ ] microVM backend evaluation.

**Exit condition:** generated code cannot directly execute inside the controller or mutate the host project while being validated.

## Phase 3 — structured cognition

- [x] Ollama structured planner adapter.
- [x] JSON-schema/Pydantic validation.
- [x] Ollama structured artifact generator.
- [x] deterministic temperature setting.
- [x] unload model after request by default.
- [x] prior machine evidence supplied to repair attempts.
- [ ] model capability registry.
- [ ] local/cloud routing adapter.
- [ ] context/repository retrieval interface.
- [ ] token/context budget enforcement.

**Exit condition:** malformed model envelopes cannot enter the execution state machine.

## Phase 4 — verification matrix

- [x] Python AST gate.
- [x] sandbox command gate.
- [x] required-gate acceptance policy.
- [ ] independent test-author stage.
- [ ] pytest evidence parser.
- [ ] Ruff gate.
- [ ] Mypy/Pyright gate.
- [ ] Bandit/Semgrep gate.
- [ ] dependency vulnerability audit.
- [ ] integration-test gate.
- [ ] Hypothesis/property-test gate.
- [ ] fuzz gate.
- [ ] benchmark regression gate.
- [ ] artifact-type gate registry for non-code outputs.

**Exit condition:** “runs without exception” is insufficient for acceptance; behavior must satisfy explicit contracts.

## Phase 5 — project checkpoint and rollback

- [ ] isolated Git worktree per mutable task group.
- [ ] immutable base commit recorded in task metadata.
- [ ] atomic accepted-artifact checkpoint.
- [ ] rejected worktree discard.
- [ ] rollback to last accepted checkpoint.
- [ ] provenance manifest attached to commit.
- [ ] merge conflict classifier and escalation path.

**Exit condition:** a failed task cannot contaminate the last accepted project state.

## Phase 6 — durable long-run orchestration

Do not build a bespoke fake-Temporal scheduler.

- [ ] define workflow backend protocol.
- [ ] implement Temporal adapter.
- [ ] workflow replay/recovery tests.
- [ ] bounded retries by fault class.
- [ ] lifecycle wall-clock budget.
- [ ] global resource/token budget.
- [ ] pause/resume/cancel controls.
- [ ] operator escalation queue.

**Exit condition:** controller process/machine restarts can resume multi-day work from workflow history and persisted project truth.

## Phase 7 — richer execution agents

Do not rebuild a full coding agent if an existing one satisfies the contract.

- [ ] OpenHands agent-server adapter.
- [ ] capability negotiation between direct runner and agent backend.
- [ ] tool permission policy.
- [ ] per-task clean agent context.
- [ ] evidence extraction from agent execution.
- [ ] backend conformance tests.

**Exit condition:** VPI-CVM can supervise a mature agent backend without surrendering acceptance authority to it.

## Phase 8 — hardware health and scheduling

- [x] NVIDIA telemetry probe.
- [x] real temperature threshold policy primitive.
- [ ] integrate thermal guard into inference scheduling.
- [ ] VRAM pressure thresholds.
- [ ] power/temperature history.
- [ ] model unload verification telemetry.
- [ ] CPU/RAM/disk host watchdogs.
- [ ] adaptive cooldown and backpressure.

**Exit condition:** long-run scheduling responds to measured hardware state, not fixed sleeps pretending to be telemetry.

## Phase 9 — observability and operator control

- [ ] structured event stream.
- [ ] task/evidence timeline API.
- [ ] Prometheus/OpenTelemetry exporter.
- [ ] lightweight dashboard.
- [ ] manual approve/reject/retry controls.
- [ ] policy override audit log.
- [ ] alerts for stuck, unsafe or budget-exhausted work.

## Phase 10 — production hardening

- [ ] migration tests.
- [ ] crash/power-loss fault injection.
- [ ] sandbox breakout regression corpus.
- [ ] 24h soak test.
- [ ] 7-day soak test.
- [ ] 30-day supervised endurance test.
- [ ] recovery-time and data-loss measurements.
- [ ] threat-model review.
- [ ] reproducible release packaging.

**Final acceptance:** the system earns long-duration autonomy claims only after endurance and recovery evidence exists.
