# VPI-CVM Adaptive Institution Layer

Status: governing architecture addendum. This document separates universal system requirements from optional domain extensions. It does not claim the listed capabilities are implemented.

## Decision

VPI-CVM must not stop at being an evidence-driven software-engineering pipeline. A world-leading project system needs to operate as an **adaptive institution**: it must understand human intent, bootstrap from zero structure, distinguish correctness from value, resist metric gaming, learn from production reality, survive component failure, make economically rational decisions, and detect model drift.

The core remains deterministic and evidence-driven. Creative, social, and cross-modal capabilities are added through explicit extension planes rather than contaminating the correctness-critical kernel.

## Universal core requirements

### 1. Intent and value contract

The human is a source of authority, not a terminal failure state.

Every project/task may carry an `IntentContract` containing:

- explicit objective;
- non-goals;
- hard constraints;
- reversible vs irreversible decisions;
- quality/taste criteria;
- examples of accepted/rejected outcomes;
- unresolved ambiguities;
- human authority boundaries;
- acceptance owner(s).

The system must distinguish:

- **missing information that can be inferred safely**;
- **ambiguity that can be resolved empirically**;
- **preference/taste questions that require human authority**;
- **safety/security/financial boundaries that require explicit approval**.

Human overrides become first-class provenance events and can update preference models only after explicit or repeated evidence. They never silently rewrite technical truth.

### 2. Day-zero bootstrap mode

VPI-CVM must work when there is no useful repository history, coverage, test graph, failure history, or compiled skill library.

Bootstrap workflow:

`intent -> constraints -> project skeleton -> first contracts -> first tests/benchmarks -> initial symbol/project graph -> baseline verification -> normal closed loop`

Cold-start rules:

- infer as little as possible;
- generate explicit hypotheses rather than invented project facts;
- establish the first executable acceptance tests before optimization;
- create baseline architecture and dependency boundaries before high-volume generation;
- record every bootstrap assumption so later evidence can invalidate it.

The Project Intelligence Fabric must therefore expose confidence/freshness, not merely presence/absence of graph data.

### 3. Dual-axis acceptance: correctness and value

Passing tests is necessary but not sufficient.

Every task declares which objective classes apply:

- correctness;
- security;
- reliability;
- performance;
- maintainability;
- usability;
- human preference/taste;
- business/product value;
- domain-specific quality.

Machine-verifiable objectives remain hard gates. Subjective objectives use calibrated human preference, domain-specific evaluators, pairwise comparisons, or real-world outcome evidence. Subjective scores can rank otherwise-valid candidates but cannot override failed hard safety/correctness gates.

### 4. Anti-Goodhart meta-evaluation

VPI-CVM must treat every optimization metric as a proxy that can be gamed.

Required mechanisms:

- metric portfolio rather than one scalar objective;
- rotating and hidden evaluation tasks;
- held-out test generators/evaluators separated from candidate-generation prompts;
- periodic human blind review of sampled accepted outputs;
- proxy/reality divergence tracking;
- evaluator disagreement tracking;
- anti-overfitting holdouts by repository/domain/time period;
- metric versioning and provenance;
- ablation checks before promoting new optimizer/routing/skill behavior.

A `MetricDivergenceEvent` is raised when benchmark improvement is accompanied by degradation in independent outcomes such as production failures, user preference, maintainability, or hidden-test robustness.

### 5. World-grounding plane

Repository state is not reality.

VPI-CVM needs a typed telemetry ingestion boundary for:

- runtime logs and traces;
- crash/error reports;
- latency/resource telemetry;
- production incidents;
- user/player behavior;
- experiment results;
- support feedback/sentiment where authorized;
- deployment/environment metadata.

Grounding evidence is versioned, privacy-scoped, and linked back to project symbols/commits/releases. Production observations can create tasks, invalidate assumptions, alter risk models, and become regression fixtures.

No telemetry source is accepted as unquestioned truth; instrumentation can itself be wrong or biased.

### 6. Survival and limp modes

The system must have degradation depth, not a single fallback.

Minimum operating modes:

1. **FULL** — project graph, frontier/local models, all execution/verification backends available.
2. **DEGRADED** — provider/runtime failures; continue with cached project intelligence, local model lanes, reduced optional analysis.
3. **SAFE_LOCAL** — no cloud/network dependency; deterministic skills, local inference, local verification, no risky autonomous mutation.
4. **RECOVERY** — rebuild derived state from canonical sources: Git, artifact hashes, journal, telemetry archives, workflow history.
5. **READ_ONLY** — when integrity cannot be established, permit inspection/export but no project mutation.

Derived indexes, caches, model-routing tables, and skill registries are rebuildable. Canonical project state and provenance are not.

Every compiled skill has health checks, freshness fingerprints, shadow evaluation sampling, and automatic quarantine on unexplained regression.

### 7. Asynchronous speculative cognition

The system may exploit idle time, but only under explicit utility and cancellation rules.

Allowed background work includes:

- cache/index refresh;
- symbol/test graph recomputation;
- likely-context prefetch;
- sandboxed test generation;
- mutation/property testing on changed high-risk code;
- benchmark replay;
- deterministic skill shadow validation;
- production telemetry clustering;
- bounded design-space exploration when an executable fitness function exists.

Forbidden by default:

- uncontrolled model generation because the system is idle;
- mutations to accepted project state without an active task contract;
- spend without a background budget;
- speculative external side effects.

All speculative artifacts are disposable until attached to an explicit task and revalidated against current fingerprints.

### 8. Economic value-of-information governor

Cost is part of the control policy, not reporting after the fact.

For each optional action, estimate:

- expected probability of changing the decision;
- expected loss avoided if the action changes the decision;
- monetary/API cost;
- GPU/compute cost;
- wall-clock delay;
- expected human-time cost;
- reversibility of proceeding without more information.

Conceptually:

`VOI = expected decision improvement - total acquisition cost`

VPI-CVM does not need a perfect economic model. It needs explicit estimates, calibration from historical outcomes, and the rule that expensive analysis/fan-out/escalation must justify itself against the task's consequence and reversibility.

### 9. Model behavioral contracts and drift control

Provider names are not stable behavioral identities.

Every model/runtime configuration has a fingerprint including:

- provider/model identifier;
- reported version when available;
- system/tool schema version;
- reasoning configuration;
- runtime/quantization configuration;
- sampled behavioral signature on a fixed canary suite.

Drift workflow:

`detect -> quarantine from critical routing -> replay sealed canaries -> compare champion/challenger -> recalibrate router -> promote or rollback`

Silent provider updates are treated as possible new model versions when canary behavior moves outside configured bounds.

Cached competence measurements expire by time, drift evidence, or configuration fingerprint changes.

## Optional extension planes

These are valuable, but they are not universal requirements for the software-engineering kernel.

### A. Cross-modal coherence plane

For games, film, design, robotics, and multimodal products, add a `ProjectAssetGraph` with typed relationships across code, image, audio, animation, narrative, UI, spatial assets, performance budgets, and design contracts.

The initial implementation should use explicit typed relationships and domain-specific validators. Learned shared embedding/projection spaces are experimental retrieval/ranking aids until they beat explicit baselines under ablation.

A change may emit propagated obligations such as:

`mechanic change -> tutorial update + haptic update + AI behavior tests + difficulty telemetry review`

This is a dependency/contract system first, not mystical cross-modal latent causality.

### B. Collaborative governance plane

For multi-user projects, add:

- actor/role/authority identities;
- attribution for every decision and override;
- proposal/review/approval states;
- branchable preference/intent views;
- conflict records rather than forced fake consensus;
- policy for decisions requiring unanimity, owner authority, majority, or designated domain expert;
- merge semantics for technical state separate from unresolved creative disagreement.

The project can contain multiple valid human perspectives without declaring one epistemic state universally true.

### C. Domain quality evaluators

Examples:

- games: engagement telemetry, progression/failure curves, exploit/soft-lock detection, accessibility, player preference;
- narrative: continuity, pacing, character consistency, human preference panels;
- visual design: design-system compliance, perceptual metrics, accessibility, human pairwise preference;
- systems architecture: complexity, coupling, operability, failure-domain containment, benchmark behavior, expert review.

These evaluators rank technically valid candidates. They do not replace domain experts where quality is inherently judgmental.

## Revised control loop

```text
HUMAN / PROJECT INTENT
        |
        v
INTENT + VALUE CONTRACT
        |
        +--> DAY-ZERO BOOTSTRAP if structure is weak
        |
        v
PROJECT INTELLIGENCE + WORLD TELEMETRY
        |
        v
RISK + UNCERTAINTY + ECONOMIC VOI
        |
        v
CHEAPEST ELIGIBLE ACTION / MODEL / TOOL
        |
        v
ISOLATED CANDIDATE
        |
        v
ADAPTIVE CORRECTNESS VERIFICATION
        |
        +--- FAIL ---> FAILURE COMPILER / ESCALATE / DECOMPOSE
        |
        v
VALUE / QUALITY EVALUATION (when applicable)
        |
        v
ANTI-GOODHART META-CHECK
        |
        v
HUMAN AUTHORITY GATE (only where contract requires)
        |
        v
CHECKPOINT + PROVENANCE
        |
        +--> SKILL / CACHE / ROUTER LEARNING
        +--> PRODUCTION OBSERVATION
                    |
                    +--> invalidate / recalibrate / create new task
```

## Architecture boundary rule

The correctness-critical kernel stays small:

- project truth and provenance;
- deterministic workflows;
- risk/budget/VOI control;
- isolation;
- verification;
- failure recovery;
- model/runtime contracts;
- reproducibility.

Human preference, collaboration, cross-modal coherence, and domain-quality evaluators plug into typed interfaces around that kernel. This prevents a world-leading design from turning into an untestable monolith.

## Promotion rule

Nothing in this addendum is accepted because it sounds intelligent.

Every mechanism must show measurable benefit in one or more of:

- verified task success;
- hidden/adversarial robustness;
- production failure reduction;
- human acceptance/preference;
- lower time/cost/operator burden;
- faster recovery;
- lower recurrence of known failure classes.

If an extension increases architectural complexity without improving those outcomes, remove it.

## Final target

VPI-CVM should behave less like an agent pipeline and more like a resilient engineering institution:

- it knows what the human is actually trying to achieve;
- it can start from nothing;
- it separates correctness from value;
- it distrusts its own metrics;
- it observes the world after deployment;
- it survives provider, cache, index, model, and runtime failures;
- it spends compute only when expected value justifies it;
- it detects when its models change;
- it accumulates only invalidatable, evidence-backed advantage.

That is the boundary required before claims of world-leading project intelligence are defensible.