# VPI-CVM

**Virtualized Project Intelligence — Cognitive Virtual Machine**

VPI-CVM is an evidence-driven supervisory control plane for long-running autonomous project work. It treats language models as **proposal generators**, not authorities. A task is accepted only after deterministic gates produce machine evidence.

> Status: **foundation implementation / v0.1**. The core loop is executable and tested; the full long-duration production system described in `docs/PLAN.md` is intentionally not claimed complete yet.

## Core invariant

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

## What exists now

- SQLite WAL task/evidence journal with explicit state transitions.
- Validated acyclic task graph and dependency-aware supervisor.
- Canonical filesystem containment; no basename flattening and no sibling-prefix escape.
- Structured Ollama planner/generator using JSON Schema and Pydantic validation.
- Docker execution boundary with:
  - no network by default
  - read-only root filesystem
  - read-only project bind mount during validation
  - all Linux capabilities dropped
  - `no-new-privileges`
  - PID, RAM, CPU and wall-clock limits
  - non-root container user
  - timeout kill/remove cleanup
- Python AST gate before sandbox execution.
- Evidence-based acceptance policy.
- Bounded repair loop that feeds deterministic failure evidence back to the generator.
- NVIDIA telemetry probe and real temperature policy primitive.
- CLI for planning and running persisted plans.
- Unit/regression test suite and GitHub Actions CI.

## What is intentionally not faked

The following are **planned**, not silently represented as complete:

- Temporal-backed multi-day durable orchestration.
- OpenHands agent-server backend.
- independent generated acceptance-test author/verifier split.
- Ruff/Mypy/Bandit/Semgrep policy gates as first-class gate plugins.
- integration/fuzz/property-testing matrix.
- Git worktree checkpoint/rollback backend.
- artifact provenance hashes and signed evidence manifests.
- network allow-list proxy for tasks that genuinely require internet access.
- gVisor / microVM isolation backend for stronger hostile-code boundaries.
- dashboard and operator approval queue.

See [`docs/PLAN.md`](docs/PLAN.md).

## Quick start

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

Use any local Ollama model that is sufficiently reliable at structured coding tasks:

```bash
vpi-cvm plan \
  --goal "Build a tested Python service with a health endpoint" \
  --model qwen3:8b \
  --output vpi-plan.json
```

Inspect the plan before execution. A plan is data, not an implicit permission grant.

### Execute/resume

```bash
vpi-cvm run \
  --plan vpi-plan.json \
  --model qwen3:8b \
  --workspace ./vpi-workspace \
  --db ./.vpi-cvm/state.db
```

Re-running the same command resumes from persisted task state; tasks already in `PASSED` are not regenerated.

## Why not just build another agent framework?

VPI-CVM is deliberately narrower. Mature systems already solve large portions of agent execution and durable workflow orchestration. The long-term architecture therefore uses adapters rather than reimplementing everything:

- **OpenHands**: candidate agent/runtime backend.
- **Temporal**: production durable workflow backend.
- **Docker now; gVisor/microVM later**: execution isolation backends.

VPI-CVM owns the **project-level truth model**: task DAG, policy, evidence, acceptance, provenance, repair budget, checkpoints, and operator escalation.

## Repository map

```text
src/vpi_cvm/
  cli.py          operator entrypoint
  models.py       validated domain schemas
  planning.py     DAG validation/readiness
  store.py        SQLite WAL state/evidence journal
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
docs/             architecture, threat model, roadmap, ADRs
```

## Development

```bash
python -m pytest -q
python -m compileall -q src tests
ruff check src tests
```

## Security position

Docker is a meaningful process/filesystem/resource boundary for local single-user execution, but it shares the host kernel and is not treated as a perfect hostile multi-tenant hypervisor. VPI-CVM's threat model and escalation path are documented in [`docs/SECURITY.md`](docs/SECURITY.md).
