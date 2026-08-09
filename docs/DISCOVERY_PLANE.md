# VPI-CVM Metacognitive Discovery Plane

Status: **post-v1 research roadmap / extension plane**.

Architecture v1 is the best current starting hypothesis, not a claim of optimality. This document defines the later machinery required for VPI-CVM to research and improve its own architecture without turning production into uncontrolled self-modification.

The Discovery Plane is intentionally outside the minimal core. It cannot rewrite the champion system directly. All proposed changes are hypotheses until shadow implementation, controlled experiment, sealed evaluation, and explicit promotion.

## Objective

Turn VPI-CVM from a system that improves through verified use into a system that can conduct structured research on how to build better VPI-CVM-like systems.

```text
OBSERVE
  -> SELF-MODEL
  -> WEAKNESS / SURPRISE
  -> HYPOTHESIS
  -> ARCHITECTURE CANDIDATE
  -> SHADOW SYSTEM
  -> CONTROLLED EXPERIMENT
  -> CAUSAL / ABLATION ANALYSIS
  -> REJECT / RETAIN / PROMOTE
  -> SCIENTIFIC MEMORY
  -> OBSERVE
```

## 1. Metacognitive self-model

VPI-CVM eventually needs a world model of VPI-CVM itself.

The self-model should represent:

- components/services and versions;
- dependencies and responsibilities;
- contracts/interfaces;
- current champion/challenger implementations;
- measured competence and known failure regions;
- costs/latencies/resource demands;
- failure attribution history;
- architectural changes and supporting evidence;
- unresolved architectural questions;
- surprise/anomaly history.

This allows queries such as:

- Which component most often correlates with cross-module localization failure?
- What evidence justified the current context compiler?
- Which architectural assumptions are weakly supported?
- Which components became slower or less reliable after a toolchain/model/runtime change?

## 2. Architectural uncertainty registry

The system must be able to represent that its own architecture is a hypothesis.

Example record:

```text
claim: graph-derived context is superior to neural retrieval for task class X
status: UNKNOWN / SUPPORTED / UNSUPPORTED / CONTRADICTORY
supporting_evidence: ...
contradicting_evidence: ...
conditions: ...
next_best_experiment: ...
```

Architectural uncertainty is distinct from artifact quality uncertainty and model-routing uncertainty.

## 3. Weakness mining and failure attribution

The discovery loop needs to move from "tasks fail" to "this system organ is probably responsible under these conditions."

Inputs include:

- failure signatures;
- negative competence regions;
- surprise events;
- arena regressions;
- cost/latency/resource outliers;
- operator intervention clusters;
- stale/retired skill events;
- adversary blind spots;
- production telemetry.

Outputs are candidate bottlenecks and research questions with evidence, not post-hoc blame asserted as truth.

## 4. Hypothesis generation

A generative hypothesis engine proposes testable architectural interventions from real evidence.

Sources may include:

- clustered failures;
- counterfactual reasoning;
- frontier/local model proposals;
- research literature/repositories;
- cross-domain analogies;
- alternative data structures/algorithms;
- removal/simplification of existing mechanisms.

Every hypothesis declares:

- observation;
- suspected mechanism;
- proposed intervention;
- predicted measurable effect;
- competing explanations;
- experiment design;
- falsification condition;
- expected cost/risk;
- required rollback.

The engine does not promote its own ideas.

## 5. Open-world ResearchWorld

Living project-derived benchmarks are closed over what the system already knows. Discovery therefore needs an external research world that can introduce novel pressure.

Potential sources:

- papers and technical reports;
- new/open repositories;
- benchmark/task families;
- model/runtime releases;
- engineering postmortems;
- algorithms/data structures from adjacent disciplines;
- production incidents and unexpected user behavior;
- explicit human challenges.

External claims retain provenance/trust labels. ResearchWorld is evidence input, not authority.

## 6. Architecture search / Meta-Compiler

The architecture search engine creates controlled candidate changes such as:

- replace a component;
- remove a component;
- alter topology/workflow;
- change routing policy;
- change representation/indexing;
- change verifier/adversary composition;
- recombine mechanisms;
- simplify a mechanism.

The Meta-Compiler operates on an explicit system model and implementation contracts. It must not mutate the production champion in place.

## 7. System worktrees and shadow systems

Architectural experiments run in isolated system candidates built from the same accepted VPI-CVM base.

```text
CHAMPION
  |-- control
  |-- challenger A
  |-- challenger B
  `-- challenger C
```

A system candidate carries:

- source commit/tree;
- architecture/config manifest;
- dependency/toolchain/runtime fingerprints;
- migration/recovery plan;
- experiment ID and hypothesis link.

Shadow candidates cannot mutate accepted production/project truth.

## 8. Experimental laboratory

The lab runs paired/controlled experiments under matched conditions and records:

- task set and contamination status;
- world/context inputs;
- cognition/provider/runtime;
- verifier/adversary policy;
- resource budgets;
- success/failure evidence;
- cost/time/human intervention;
- intermediate mechanism metrics.

Experiment outcomes are `SUPPORTED`, `FALSIFIED`, or `INCONCLUSIVE`; inconclusive results trigger additional evidence or abandonment, not forced promotion.

## 9. Causal and ablation analysis

The arena can show that performance changed. The discovery plane must investigate why.

Required methods include:

- component ablations;
- paired control/challenger trials;
- mediation/intermediate metric tracking;
- distribution-sliced analysis;
- regression/confound checks;
- rollback/replay.

Causal claims remain scoped to the experiment conditions and evidence. The system must not turn correlation into a permanent architectural story.

## 10. Automated abstraction mining

After multiple mature domain world models exist, the discovery plane may mine structural pattern candidates across them.

Examples include dependency propagation, continuity maintenance, verification expansion, resource contention, or state-transition patterns.

Transfer workflow:

```text
source-domain pattern
  -> abstraction candidate
  -> target-domain shadow application
  -> target-domain verification
  -> negative-transfer detection
  -> retain/reject
```

Commonality is discovered from evidence rather than declared from analogy.

## 11. Insight search, not magical invention

Do not define an "insight generator" that labels its own output novel.

Instead combine:

- real failure/weakness data;
- self-model;
- ResearchWorld;
- frontier/local models;
- cross-domain analogy;
- counterfactual search;
- architecture mutation;
- experiment results.

This produces **candidate insights**. Novelty/value are established only after the lab demonstrates a previously unavailable useful mechanism or capability.

## 12. Scientific memory

Discovery requires durable memory of research, including rejected ideas.

Record:

- hypotheses;
- experiments;
- architectural candidates;
- supported/falsified/inconclusive outcomes;
- measured effect sizes/conditions;
- negative results;
- known interactions/confounds;
- unresolved questions;
- promotion/rollback history.

This prevents repeated rediscovery of disproven changes and gives models empirical context unavailable from generic training data.

## 13. Meta-governor / research economy

Self-improvement competes with production for finite resources. A meta-governor allocates CPU/GPU/API spend, wall time, storage, and operator attention between production and research.

Allocation considers:

- production deadlines/priority;
- current incidents/regressions;
- expected value of information;
- cost/risk/reversibility;
- idle capacity;
- research backlog;
- uncertainty severity.

No fixed percentage is architectural law. Research must be cancellable/preemptible and may never consume resources required to keep the production control plane safe.

## 14. Safe recursive improvement governance

The champion cannot directly rewrite itself.

```text
CURRENT CHAMPION
  -> research proposal
  -> isolated system candidate
  -> focused tests
  -> living arena
  -> sealed/rotating evaluation
  -> adversarial/security/recovery checks
  -> promotion decision
  -> NEW CHAMPION or REJECT
```

Promotion must preserve a recoverable prior champion and migration/rollback path. Critical self-modification may require explicit operator approval even if arena metrics improve.

## 15. Learning-velocity metrics

The Discovery Plane should measure research efficiency, not only artifact productivity.

Candidate metrics:

- time from failure/surprise to testable hypothesis;
- experiments per constrained resource unit;
- fraction of hypotheses producing useful information;
- time to falsification;
- validated improvements per period;
- recurrence of previously understood failures;
- performance/value gain per experiment;
- human research time per validated improvement.

These are measurement candidates, not a single Goodhart-prone scalar objective.

## Promotion boundary

No Discovery Plane mechanism is accepted merely because it sounds more intelligent.

Each mechanism must demonstrate measurable benefit in research velocity, verified system capability, robustness, cost, recovery, or operator burden without compromising sealed evaluation, security, reproducibility, or human authority.

## Sequencing

Architecture v1 + Operational Control Plane comes first.

The Discovery Plane is introduced only after SoftwareWorld, the dual arena, verification, failure memory, capability measurements, and reproducible system builds are mature enough to provide real experimental substrate.

The seam belongs in the roadmap now; the implementation must be earned later.
