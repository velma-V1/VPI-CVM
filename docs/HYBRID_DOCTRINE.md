# VPI-CVM Hybrid Doctrine

## Decision

VPI-CVM remains the base architecture because its industrial execution, verification, project-intelligence, and benchmarking choices are implementable with current components. It now explicitly absorbs the strongest compounding-intelligence ideas from the SCVI/KAIROS critique without importing the speculative parts.

The design target is:

> **VPI-CVM chassis + persistent compiled project intelligence + adaptive verification + failure compilation + verified skill accumulation.**

This is not a compromise between two architectures. It is a selection process: keep mechanisms that can be tested now; reject abstractions that cannot earn their place in the sealed arena.

## What the critique correctly exposed

### 1. A static model router is insufficient

Task difficulty is partially latent. A seemingly small change can reveal a wider dependency, race, migration hazard, or security boundary only after reproduction or verification.

Therefore routing is not a one-shot classification. It is a **closed-loop policy**:

1. establish hard capability floors from observable risk;
2. select the cheapest eligible lane with adequate empirical confidence;
3. execute and verify;
4. escalate immediately when evidence reveals larger scope or the candidate fails;
5. record the result back into the arena routing table.

The router is allowed to be wrong. The architecture is not allowed to remain wrong after evidence arrives.

### 2. Cost and latency are first-class correctness constraints

Calling multiple frontier models on every task is forbidden by design.

Every task has explicit budgets for:

- dollars;
- tokens;
- GPU time;
- wall time;
- candidate count;
- verification depth.

Multi-model candidate tournaments are reserved for high uncertainty, high consequence, or poor historical confidence. Most bounded tasks should use one local/cheap candidate and deterministic verification before escalation.

### 3. Verification must be adaptive

A fixed maximum verification waterfall is wasteful. A weak verification path is unsafe.

VPI-CVM therefore uses a **monotonic risk-tiered verification ladder**. Cheap gates screen candidates first. Expensive mutation, CodeQL, full integration, and performance checks are activated by changed-code risk, coverage gaps, security boundaries, concurrency, migrations, public API impact, prior failures, or final-acceptance policy.

After a candidate exposes new risk, verification may escalate but cannot silently downgrade.

### 4. Cloud capability must not become cloud dependence

Frontier APIs are powerful components, not foundations of system survival.

VPI-CVM requires:

- provider health and rate-limit circuit breakers;
- local/offline inference lane;
- provider-neutral task contracts;
- graceful degradation rules;
- cached arena results rather than live multi-provider shootouts on every task.

Provider failure should reduce available capability, not destroy project truth or workflow state.

### 5. The system must compound intelligence

Without reuse, VPI-CVM would remain an expensive orchestration harness.

Compounding happens at four levels:

1. **Project graph:** exact code/test/history relationships persist and update incrementally.
2. **Context/cache hierarchy:** validated summaries and context assemblies are reused until their content fingerprints invalidate them.
3. **Failure compiler:** raw failures become structured counterexamples and reusable failure signatures.
4. **Verified Skill Compiler:** repeated successful neural transformations are shadowed, replayed, adversarially validated, and eventually promoted into deterministic skills.

The desired long-run behavior is fewer neural calls per verified unit of engineering work.

## What we explicitly reject

### Cognitive bytecode as a governing abstraction

Typed operations such as `HYPOTHESIZE`, `COMPARE`, or `SYNTHESIZE` are not accepted as a runtime ISA merely because they sound compiler-like. Workflow control remains deterministic task FSMs with typed neural leaves until a competing abstraction proves superior in the sealed arena.

### Unbounded epistemic hypergraphs

VPI-CVM stores the evidence/provenance relationships necessary for correctness, debugging, replay, and benchmarking. It does not create ontology complexity without measurable retrieval, verification, or routing benefit.

### Blind persistent neural state

Raw KV state, cached reasoning, summaries, adapters, or neural outputs may become stale when any of the following changes:

- repository content;
- dependency graph;
- task contract;
- model weights/version;
- system prompt/schema;
- inference runtime;
- toolchain;
- verification policy.

Reusable neural/context state must therefore be keyed by immutable fingerprints and invalidated by dependency changes. Persistent intelligence is valuable only when freshness can be proven.

### Automatic online LoRA from every accepted decision

Accepted outputs are not automatically good training examples. Online weight updates can amplify local mistakes, style drift, benchmark overfitting, or correlated verifier blind spots.

VPI-CVM first accumulates machine-verified trajectories, counterexamples, and held-out evaluation data. Adapter/fine-tuning experiments are promoted only when sealed-arena evaluation beats the unchanged base model without regressions.

### Background 'dreaming' without measurable objective functions

Idle-time search is permitted only where the system has executable simulators, property tests, benchmarks, or other defensible fitness functions. Open-ended background generation does not count as improvement.

## Closed-loop architecture

```text
TASK
  |
  v
CONTRACT + RISK FEATURES
  |
  v
PROJECT INTELLIGENCE GRAPH
  |
  v
CONTENT-ADDRESSED CONTEXT COMPILER
  |
  v
COMPETENCE ENVELOPE + BUDGET GOVERNOR
  |
  v
CHEAPEST ELIGIBLE NEURAL LANE
  |
  v
ISOLATED CANDIDATE
  |
  v
ADAPTIVE VERIFICATION LADDER
  |                    |
 PASS                 FAIL
  |                    |
  v                    v
CHECKPOINT        FAILURE COMPILER
  |                    |
  v                    +--> ESCALATE / DECOMPOSE / REPAIR
SKILL REGISTRY
  |
  +--> repeated verified pattern
            |
            v
   SHADOW DETERMINISTIC SKILL
            |
            v
   HISTORICAL + HELD-OUT REPLAY
            |
            v
      PROMOTE OR REJECT
```

## Competitive moat

The moat is not access to a particular model. Competitors can buy the same API.

The moat is the accumulated combination of:

- exact project intelligence;
- verified failure history;
- task-specific routing evidence;
- reusable context artifacts;
- deterministic workflow recipes;
- private hidden evaluations;
- verified skills compiled from repeated successful work;
- provenance tying every accepted result to machine evidence.

A model update can be swapped into this system and immediately inherit the institution. A standalone model starts each project with far less compiled knowledge.

## Promotion rule

Every ambitious mechanism is a hypothesis until it wins an ablation under the same harness.

Examples:

- project graph vs raw repository retrieval;
- cached context vs fresh compilation;
- adaptive verification vs fixed verification;
- local-first escalation vs frontier-first;
- skill compiler enabled vs disabled;
- specialized adapter vs base model;
- one candidate vs candidate tournament.

Only measurable improvements in verified success, hidden-test robustness, time, cost, or operator burden become permanent architecture.

## Final doctrine

VPI-CVM should become cheaper and more competent as project history grows.

If repeated work does not reduce uncertainty, context cost, inference cost, verification effort, or failure recurrence, the system is storing history rather than learning.

The design objective is therefore not persistent memory by itself. It is **persistent, invalidatable, machine-verified advantage**.
