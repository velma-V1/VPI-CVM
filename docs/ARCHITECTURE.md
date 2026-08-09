# VPI-CVM Architecture v1

Status: **governing architecture**. This document defines the target system. Existing code is an executable foundation and does not yet implement every target capability described here.

## System identity

VPI-CVM — **Virtualized Project Intelligence / Cognitive Virtual Machine** — is a resident cognitive production system for designing, planning, building, testing, verifying, publishing, and observing complex projects.

Its durable intelligence lives in **explicit, versioned, evidence-backed state**, not inside any particular model, API, attention cache, or provider.

The system is organized around three equal engines:

1. **UNDERSTAND** — project/world intelligence, human intent, context compilation, history, observations.
2. **CREATE** — deterministic skills, local models, frontier models, tools, isolated execution.
3. **PROVE** — correctness verification, goal-conformance checks, adversarial counterexample search, quality assessment, provenance.

No one engine is sufficient by itself.

## Non-negotiable laws

1. **Models propose; evidence decides.** Neural output never self-certifies correctness.
2. **Durable intelligence is explicit state.** Project graphs, world snapshots, evidence, failure memory, verified skills, capability history, and human intent are authoritative. KV/prefix caches are disposable performance optimizations.
3. **Canonical knowledge is immutable/versioned.** Source-derived intelligence produces new content-addressed snapshots rather than rewriting historical truth. Operational coordination may mutate transactionally but cannot rewrite canonical history.
4. **Arena-first development.** Every substantial mechanism is measured against a baseline and retained only when evidence supports its value.
5. **Dual arena.** Living project-derived evaluation drives surveillance and practice; sealed/rotating holdouts remain independent truth for promotion, regression, and anti-overfitting.
6. **Three epistemic planes.** Correctness, goal conformance, and quality are not interchangeable.
7. **Hard gates require mechanically defensible predicates.** Interpretive judgments cannot silently become binary truth.
8. **Adversarial models discover counterexamples; deterministic arbiters decide whether those counterexamples actually break a candidate.**
9. **Cognition is heterogeneous and replaceable.** Deterministic skill, local model, fast frontier, and deep frontier are selected empirically; no model is permanent king.
10. **Value is measured from realized outcomes before it is optimized from forecasts.** Cost, human time, latency, reuse, recurrence, and capability growth are first-class telemetry.
11. **Compounding must be verified.** Repeated successful work may become deterministic skills only after replay, shadow execution, holdout validation, and rollback support.
12. **Domain abstractions are discovered under pressure.** SoftwareWorld is first; cross-domain transfer remains experimental until at least two mature domain world models exist.
13. **V31M4 and VPI-CVM are independent systems.** Any future bridge is optional, versioned interoperability, never a kernel dependency.

## Minimal core

The target core stays intentionally small. New concepts do not enter the kernel merely because they are useful elsewhere.

```text
core/
  TaskContract
  ArtifactRef
  EvidenceRecord
  ProvenanceRecord
  CapabilityRecord
  PolicyDecision
  WorldSnapshotRef
  ExecutionResult
```

Core responsibilities are stable identity, evidence/provenance semantics, immutable references, capability state, policy decisions, and execution-result envelopes.

Providers, parsers, Git, Tree-sitter, SCIP, sandboxes, agent frameworks, game engines, quality critics, benchmark generators, and model runtimes remain outside the core.

## Resident intelligence

The resident brain is the accumulated explicit state of the project/system:

```text
Project / World Intelligence Snapshots
Human Intent + Value State
Evidence + Provenance History
Failure Memory + Counterexamples
Verified Skills
Capability History
Arena Measurements
Production / Runtime Observations
```

A model may be killed, unloaded, upgraded, or replaced without erasing this intelligence.

## World models

Each domain exposes a read-oriented world model backed by immutable snapshots.

```text
WorldModel
  snapshot()
  entities(query)
  relations(query)
  provenance(id)
  dependencies(id)
  observations(query)
```

Context compilation is a separate concern so competing context compilers can be evaluated against the same world snapshot.

### SoftwareWorld — first validated domain

Initial evidence sources:

- Git commit/tree state
- parser/AST data
- symbol definitions/references
- import/module relationships
- test-to-source relationships

Candidate additions such as SCIP, dynamic coverage, CodeQL, and failure-history links are promoted only when arena ablations show material benefit.

Future domain implementations may include GameWorld, FilmWorld, InfrastructureWorld, and others. They share contracts, not ontology assumptions.

## Context compiler

The context compiler converts a task plus immutable world snapshot into the **minimum sufficient evidence packet** under an explicit token/entity budget.

Initial inclusion scoring uses observable proxies such as:

- task-text relevance
- dependency distance
- failing-stack proximity
- test association
- changed-file proximity
- reference strength
- historical failure association
- token cost

These scores are not called "utility" until arena data calibrates them against actual task success.

Every packet records what was included, excluded, why, and the fingerprints needed for replay.

## Cognition portfolio

Routing is closed-loop, not a one-shot difficulty guess.

```text
verified deterministic skill
        |
        v when insufficient
local model
        |
        v when insufficient or economically inferior
fast frontier model
        |
        v when insufficient
frontier deep model
```

The order is policy, not ideology. A frontier call is correct when it yields more verified value than cheaper alternatives. A local or compiled route is correct when it does the same work with lower cost/latency/risk.

Every route is fingerprinted by provider/model/runtime/configuration/prompt/tool-schema versions. Behavioral drift triggers quarantine and replay before critical routing resumes.

## Adversarial Verification Fabric

Adversarial search is a foundational product capability, but not kernel authority.

```text
Generator -> Candidate -> Counterexample Search -> Deterministic Arbiter
                                              |
                                      counterexample valid?
                                      /                 \
                                    yes                 no
                                     |                   |
                              Failure Compiler       discard attack
```

Software adversaries may generate hostile inputs, property violations, mutations, concurrency schedules, exploit attempts, and edge cases. Future domain adversaries may search for soft-locks, degenerate strategies, continuity failures, or other domain-specific weaknesses.

The adversary discovers attacks. Existing deterministic gates and explicit contracts remain independent truth sources.

## Three epistemic planes

### Plane 1 — Correctness

Hard PASS/FAIL only when machine-defensible.

Examples: syntax, schema validity, types, tests, mutation/property violations, security rules, resource limits, integration contracts, performance thresholds.

### Plane 2 — Goal conformance

Split internally:

- **mechanical constraints** — hard PASS/FAIL where a predicate is objectively checkable;
- **interpretive constraints** — advisory assessment with evidence when requirements such as tone, pacing, elegance, or feel cannot be reduced defensibly to a mechanical predicate.

### Plane 3 — Quality estimate

Subjective or outcome-oriented quality is probabilistic and advisory until calibrated against human or real-world outcomes.

Quality systems must report calibration status, evidence, disagreement/conflict, and whether human review is required. They may compare valid variants; they do not override failed correctness gates.

## Dual arena

### Living Arena

Continuously derives bounded tasks and checks from current project intelligence. It is used for:

- regression surveillance
- blind-spot discovery
- practice
- synthetic counterexample generation
- capability monitoring
- skill shadow validation

Living tasks are labeled synthetic/project-derived and cannot alone crown champions or permanently promote capabilities.

### Sealed / rotating arena

Independent evaluation provides promotion truth:

- held-out tasks
- hidden acceptance conditions
- rotating repositories/data/time periods
- contamination controls
- identical harness/context/tool/budget conditions for challengers

It protects VPI-CVM from overfitting its own living task generator and optimization metrics.

### Trial reproducibility

Every trial records at minimum:

- task and acceptance contract
- repository/source commit
- world snapshot hash
- context packet/fingerprint
- model/provider/version/configuration
- prompt/tool-schema fingerprint
- runtime/sandbox fingerprint
- verifier/policy version
- result/evidence
- wall time, cost, tokens/GPU time where applicable
- human intervention

Promotion decisions use paired comparisons, practical effect sizes, uncertainty, and safety/non-regression guardrails. Fixed sample counts or p-value thresholds are not architectural truth.

## Failure compiler

Raw failures become structured reusable evidence rather than prompt noise.

A failure signature should identify, where available:

- violated contract/gate
- affected entities/symbols
- minimal reproducer or counterexample
- expected vs actual behavior
- suspected dependency radius
- prior matching failures
- successful prior repairs
- environment and fingerprint metadata

Failure signatures feed repair, routing, regression tests, project intelligence, and skill promotion guards.

## Realized-value ledger

The system records value before trying to forecast it.

Measured dimensions include:

- verified task success
- monetary/API cost
- GPU/compute use
- wall-clock time
- human time/intervention
- future reuse actually observed
- failure recurrence avoided or observed
- capability unlocked/retired

Forecast value is always labeled as forecast and carries assumptions/calibration status. The compute governor eventually learns expected value from realized history instead of inventing pseudo-financial precision on day one.

## Verified Skill Compiler

Repeated verified neural behavior may be converted into deterministic capability:

```text
NEURAL
 -> REPEATED_VERIFIED
 -> SHADOW_DETERMINISTIC
 -> HISTORICAL_REPLAY
 -> SEALED/ADVERSARIAL_REPLAY
 -> VALIDATED_SKILL
 -> DETERMINISTIC
```

Skills carry fingerprints, known counterexamples, health checks, usage telemetry, invalidation rules, and rollback/quarantine paths.

## Cross-domain transfer / Meta-World research

The architecture preserves a seam for transfer learning but does not invent a universal ontology prematurely.

When at least two domain world models are mature, VPI-CVM may mine structural pattern candidates such as dependency propagation or verification expansion. Transfer happens only in shadow mode and must be revalidated under the target domain's own correctness/goal/quality rules.

A source-domain skill is never automatically promoted as a target-domain skill.

## Understand -> Create -> Prove loop

```text
HUMAN INTENT / ACTIVE TASK
        |
        v
UNDERSTAND
  World Snapshot
  Project Intelligence
  Human Intent / Value
  Context Compiler
        |
        v
CREATE
  Deterministic Skill / Local / Frontier
  Tool + Isolated Execution
        |
        v
PROVE
  Correctness Gates
  Goal Conformance
  Adversarial Counterexample Search
  Quality Assessment when applicable
        |
        +---- FAIL ----> Failure Compiler -> repair / escalate / decompose
        |
       PASS
        v
ACCEPTED ARTIFACT + PROVENANCE
        |
        +--> Realized Value Ledger
        +--> Capability History
        +--> Skill Compiler
        +--> World / Production Observation
        +--> Living Arena
                    |
                    +--------------------> UNDERSTAND
```

The sealed arena remains outside this learning loop as independent promotion truth.

## Current executable foundation

The repository currently implements an earlier software-engineering foundation in Python:

- schema-constrained task/candidate models
- validated dependency DAG
- SQLite WAL task/evidence journal
- canonical workspace containment
- Ollama structured planning/generation adapter
- hardened Docker validation boundary
- Python AST and sandbox-command evidence gates
- bounded evidence-fed repair loop
- resumable supervisor
- NVIDIA telemetry primitive

These components are real and tested. They are **not** evidence that the target Architecture v1 capabilities above are already complete.

The implementation plan in `PLAN.md` governs migration/expansion from this executable foundation without rewriting functioning components unnecessarily.

## Final doctrine

VPI-CVM is a **resident, self-measuring, adversarially tested, economically rational cognitive production system whose durable intelligence lives in explicit verified state and whose capability compounds through verified experience**.
