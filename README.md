# VPI-CVM

**Virtualized Project Intelligence — Cognitive Virtual Machine**

VPI-CVM is a resident, evidence-driven cognitive production system. Its target is to **understand, create, and prove** complex project work while accumulating reusable capability from verified experience.

Its durable intelligence is explicit and reproducible — project/world snapshots, evidence, provenance, decision history, failure memory, verified skills, capability/known-unknown history, human intent, and measured outcomes — rather than hidden inside any particular model, provider, or attention cache.

> **Status:** executable foundation / frozen Architecture v1 migration. Architecture v1 is the best current starting hypothesis, not a claim of optimality or completion. The current Python control loop is real and tested; the full Operational Control Plane, resident intelligence, dual arena, adversarial fabric, value ledger, skill compiler, and Discovery Plane are not claimed implemented.

## Governing documents

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — frozen Architecture v1.
- [`docs/OPERATIONAL_CONTROL_PLANE.md`](docs/OPERATIONAL_CONTROL_PLANE.md) — governing Phase 0 survival/control specification.
- [`docs/PLAN.md`](docs/PLAN.md) — governing implementation sequence.
- [`docs/SECURITY.md`](docs/SECURITY.md) — threat model.
- [`docs/DISCOVERY_PLANE.md`](docs/DISCOVERY_PLANE.md) — post-v1 metacognitive/self-research roadmap.

Older doctrine documents are retained as architecture history only and are superseded wherever they conflict with the governing documents above.

## Governing doctrine

```text
UNDERSTAND
  project/world intelligence
  human intent/value
  context compilation
        |
        v
CREATE
  deterministic skill / local model / frontier model
  isolated tools and candidate execution
        |
        v
PROVE
  correctness
  mechanical goal conformance
  adversarial counterexample search
  advisory quality assessment
        |
        v
VERIFIED OUTCOME
        |
        +--> decision + failure memory
        +--> realized value
        +--> capability / known-unknown history
        +--> verified skills
        +--> living arena
        +--> production/world observations
```

A sealed/rotating arena remains outside that learning loop as independent promotion and anti-overfitting truth.

## Architecture laws

- Models propose; machine evidence decides correctness.
- Canonical knowledge is immutable/versioned; operational state may mutate transactionally without rewriting history.
- The resident brain is explicit verified state, not persistent KV cache.
- Living evaluation drives surveillance/practice; sealed and rotating holdouts govern promotion/generalization.
- Correctness, goal conformance, and subjective quality are separate epistemic planes.
- Adversarial models search for counterexamples; deterministic arbiters decide whether they are valid; adversaries themselves are calibrated.
- Local and frontier models are permanent replaceable tools selected empirically.
- Realized value is measured before forecast value is optimized.
- Capability includes strengths, known failure regions, contradictory evidence, and unknowns.
- Consequential decisions leave structured provenance that `explain` can query.
- Repeated verified work may compile into deterministic skills only after replay/holdout validation, and skills can be quarantined/retired when they degrade.
- Operational survival — security, recovery, termination, resource scheduling, operator control, storage health, drift/surprise handling — is a prerequisite for autonomy claims.
- SoftwareWorld is the first validated domain; cross-domain transfer is experimental until multiple real domains create evidence for it.
- Architectural self-modification is post-v1 controlled research through isolated shadow systems, not direct self-rewrite.
- V31M4 and VPI-CVM are independent systems; any future bridge is optional interoperability only.

## What exists now

The repository currently provides an executable software-engineering foundation:

- SQLite WAL task/evidence journal with explicit state transitions.
- Validated acyclic task graph and dependency-aware supervisor.
- Canonical filesystem containment.
- Structured Ollama planner/generator using JSON Schema and Pydantic validation.
- Hardened Docker execution boundary with deny-by-default network, read-only project validation, dropped capabilities, no-new-privileges, resource limits, non-root execution, and timeout cleanup.
- Python AST gate and sandbox-command evidence gate.
- Evidence-based acceptance policy.
- Bounded repair loop that feeds deterministic failures back to candidate generation.
- NVIDIA telemetry/thermal policy primitive.
- CLI for planning and resuming persisted work.
- Unit/regression tests and GitHub Actions CI.

These are foundation components, not a claim that Architecture v1 is already implemented.

## Build direction

### Phase 0 — Operational Control Plane

Before intelligence-heavy work, establish the contracts for:

- trust-aware context and security;
- idempotency/recovery/circuit breakers;
- typed operator control;
- day-zero bootstrap;
- termination/satisficing;
- CPU/RAM/disk/GPU resource scheduling;
- storage/retention/query-health policy;
- model/runtime fingerprinting, drift, and surprise detection;
- known-unknown/negative competence handling;
- structured decision provenance/explanation.

### Phases 1–10 — Architecture v1

1. minimal stable contracts, immutable SoftwareWorld snapshots, and a dual arena;
2. measured Context Compiler plus empirical competence/known-unknown model;
3. local + frontier cognition under one drift-aware contract;
4. correctness verification plus calibrated adversarial counterexample search;
5. structured Failure Compiler;
6. empirical routing plus a Realized Value Ledger;
7. Verified Skill Compiler with retirement/revalidation plus Living Benchmark generation;
8. human intent/value state, mechanical goal conformance, and evidence-calibrated advisory quality;
9. one complete SoftwareWorld lifecycle from intent through publish/observe with bounded termination and rollback;
10. a second domain followed by evidence-backed cross-domain transfer research.

### Phase 11+ — Metacognitive Discovery Plane

Only after VPI-CVM has mature reproducible measurements:

- model VPI-CVM itself as a system;
- represent architectural uncertainty;
- mine weaknesses and surprises;
- generate falsifiable architectural hypotheses;
- ingest open-world research pressure;
- create isolated system worktrees/shadow architectures;
- run controlled A/B/ablation experiments;
- retain scientific memory including failed ideas;
- allocate production vs self-research resources through a meta-governor;
- promote/rollback architectural challengers safely.

Nothing is promoted because it sounds advanced. Mechanisms are retained, rejected, or left inconclusive based on reproducible evidence.

## Current core loop

The existing implementation currently follows this narrower loop:

```text
GOAL
  -> schema-constrained planner
  -> validated dependency DAG
  -> proposal generator
  -> canonical workspace write
  -> deterministic gates
  -> disposable sandbox execution
  -> evidence journal
  -> PASS: persist terminal state
  -> FAIL: bounded repair using evidence
  -> resume from persisted state
```

The system deliberately does **not** use an LLM to grade its own output.

## Quick start for the current foundation

### Requirements

- Python 3.11+
- Ollama reachable at `http://localhost:11434`
- Docker Engine / Docker Desktop reachable from the environment running VPI-CVM
- optional: NVIDIA `nvidia-smi` for GPU telemetry

### Install

```bash
python -m pip install -e ".[dev]"
docker build -t vpi-cvm-sandbox:py313 sandbox/
```

### Create a plan

```bash
vpi-cvm plan \
  --goal "Build a tested Python service with a health endpoint" \
  --model qwen3:8b \
  --output vpi-plan.json
```

### Execute/resume

```bash
vpi-cvm run \
  --plan vpi-plan.json \
  --model qwen3:8b \
  --workspace ./vpi-workspace \
  --db ./.vpi-cvm/state.db
```

Re-running the same command resumes from persisted task state; tasks already in `PASSED` are not regenerated.

## Repository map — current implementation

```text
src/vpi_cvm/
  cli.py          operator entrypoint
  models.py       validated schemas
  planning.py     DAG validation/readiness
  store.py        SQLite WAL task/evidence journal
  workspace.py    canonical path containment
  ollama.py       structured planner/generator adapter
  sandbox.py      hardened Docker execution backend
  evidence.py     deterministic gates + acceptance policy
  kernel.py       bounded generate/evaluate/repair loop
  supervisor.py   dependency-aware resumable dispatcher
  thermal.py      NVIDIA telemetry + thermal policy

tests/            behavioral/regression tests
sandbox/          disposable validation image
examples/         sample plan data
docs/             governing architecture, operational control, discovery roadmap, security, ADRs, history
```

## Development

```bash
python -m pytest -q
python -m compileall -q src tests
ruff check src tests
```

## Security position

Docker is a meaningful process/filesystem/resource boundary for local single-user execution, but it shares the host kernel and is not treated as a perfect hostile multi-tenant hypervisor. Prompt/context injection, training/skill poisoning, dependency/plugin supply chain, resource-exhausting artifacts, arena privacy/contamination, stronger isolation, task-scoped credentials, and durable recovery are explicitly tracked in [`docs/SECURITY.md`](docs/SECURITY.md) and [`docs/OPERATIONAL_CONTROL_PLANE.md`](docs/OPERATIONAL_CONTROL_PLANE.md).

## Historical architecture notes

`docs/HYBRID_DOCTRINE.md`, `docs/ADAPTIVE_INSTITUTION.md`, and `docs/WORLD_LEAD_STACK.md` are retained only as architecture history. They are superseded wherever they conflict with Architecture v1 or the governing companion specs.
