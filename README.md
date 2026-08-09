# VPI-CVM

**Virtualized Project Intelligence — Cognitive Virtual Machine**

VPI-CVM is a resident, evidence-driven cognitive production system. Its target is to **understand, create, and prove** complex project work while accumulating reusable capability from verified experience.

Its durable intelligence is explicit and reproducible — project/world snapshots, evidence, provenance, failure memory, verified skills, capability history, human intent, and measured outcomes — rather than hidden inside any particular model, provider, or attention cache.

> **Status:** executable foundation / Architecture v1 migration. The current Python control loop is real and tested. The resident intelligence, dual arena, adversarial verification, value ledger, skill compiler, and multi-domain capabilities in the target architecture are not claimed complete.

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
        +--> failure memory
        +--> realized value
        +--> capability history
        +--> verified skills
        +--> living arena
        +--> production/world observations
```

A sealed/rotating arena remains outside that learning loop as independent promotion and anti-overfitting truth.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the governing Architecture v1 and [`docs/PLAN.md`](docs/PLAN.md) for the implementation sequence.

## Architecture laws

- Models propose; machine evidence decides correctness.
- Canonical knowledge is immutable/versioned; operational state may mutate transactionally without rewriting history.
- The resident brain is explicit verified state, not persistent KV cache.
- Living evaluation drives surveillance/practice; sealed and rotating holdouts govern promotion/generalization.
- Correctness, goal conformance, and subjective quality are separate epistemic planes.
- Adversarial models search for counterexamples; deterministic arbiters decide whether they are valid.
- Local and frontier models are permanent replaceable tools selected empirically.
- Realized value is measured before forecast value is optimized.
- Repeated verified work may compile into deterministic skills only after replay and holdout validation.
- SoftwareWorld is the first validated domain; cross-domain transfer is experimental until multiple real domains create evidence for it.
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

## Architecture v1 build direction

The implementation plan now prioritizes:

1. minimal stable contracts, immutable SoftwareWorld snapshots, and a dual arena;
2. an independent measured Context Compiler;
3. a local model plus frontier challenger under one contract;
4. adaptive correctness verification plus adversarial counterexample search;
5. a structured Failure Compiler;
6. empirical capability routing plus a Realized Value Ledger;
7. a Verified Skill Compiler plus Living Benchmark generation;
8. human intent/value state, mechanical goal conformance, and calibrated advisory quality assessment;
9. one complete SoftwareWorld lifecycle from intent through publish and observation;
10. a second domain followed by evidence-backed cross-domain transfer research.

Nothing is promoted because it sounds advanced. Mechanisms are retained, rejected, or left inconclusive based on reproducible arena evidence.

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
docs/             governing architecture, plan, security, ADRs, research history
```

## Development

```bash
python -m pytest -q
python -m compileall -q src tests
ruff check src tests
```

## Security position

Docker is a meaningful process/filesystem/resource boundary for local single-user execution, but it shares the host kernel and is not treated as a perfect hostile multi-tenant hypervisor. Stronger isolation, worktree candidate separation, task-scoped credentials, and durable workflow recovery remain target work in [`docs/PLAN.md`](docs/PLAN.md).

## Historical architecture notes

`docs/HYBRID_DOCTRINE.md`, `docs/ADAPTIVE_INSTITUTION.md`, and `docs/WORLD_LEAD_STACK.md` are retained only as architecture history. They are superseded wherever they conflict with Architecture v1.
