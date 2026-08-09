# Architecture

## System role

VPI-CVM is a **supervisory cognitive control plane**, not a monolithic agent. It separates nondeterministic reasoning from deterministic authority.

### Authority boundary

The model may propose:

- task decompositions
- artifact contents
- targeted repairs
- explanations

The model may not unilaterally declare:

- task completion
- test success
- security compliance
- filesystem safety
- resource safety
- checkpoint validity

Those claims require machine evidence.

## Control loop

```text
                           +----------------------+
                           |   durable task state  |
                           | SQLite now / Temporal |
                           +-----------+----------+
                                       |
                                       v
+------+    +---------+    +-----------+-----------+
| goal | -> | planner | -> | validated dependency  |
+------+    +---------+    | DAG + acceptance data |
                           +-----------+-----------+
                                       |
                                       v
                           +-----------+-----------+
                           | candidate generator   |
                           +-----------+-----------+
                                       |
                                       v
                           +-----------+-----------+
                           | canonical workspace   |
                           | controller writes only|
                           +-----------+-----------+
                                       |
                                       v
                    +------------------+------------------+
                    | deterministic evidence pipeline     |
                    | AST -> sandbox -> tests -> policies |
                    +------------------+------------------+
                                       |
                        +--------------+--------------+
                        |                             |
                      PASS                           FAIL
                        |                             |
                        v                             v
               checkpoint/provenance       classify + bounded repair
                        |                             |
                        +--------------+--------------+
                                       |
                                       v
                                 next ready task
```

## Current components

### Domain schemas

Pydantic models validate plan/task/candidate payloads. Structured model output is rejected if it does not conform to the schema.

### Task graph

`TaskGraph` rejects unknown dependencies, self-dependencies and cycles. Only `PENDING` tasks whose dependencies are all `PASSED` are dispatchable.

### Journal

`SQLiteJournal` uses WAL mode and `synchronous=FULL`. It stores task state and ordered evidence. State transitions are explicit rather than arbitrary string mutation.

SQLite is the local v0 backend. The target production adapter is Temporal for multi-day workflow replay/recovery while retaining the VPI evidence model.

### Workspace

The controller resolves every requested target beneath one canonical workspace root using resolved-path containment. Generated code is written by the controller; validation containers receive the project as read-only.

### Sandbox

Current backend: Docker.

Mandatory default controls:

- `--network none`
- `--read-only`
- project bind mount `ro`
- `--cap-drop ALL`
- `--security-opt no-new-privileges`
- PID, memory and CPU limits
- non-root UID/GID
- writable tmpfs only for `/tmp`
- wall-clock timeout
- explicit container kill/remove on timeout

### Evidence

Current deterministic gates:

- Python AST syntax gate
- sandbox validation command exit status

Acceptance requires every required gate to be present and `PASS`. Latest evidence for a gate is authoritative for the current repair sequence.

### Kernel

`CognitiveKernel` performs bounded attempts. Every failed deterministic gate becomes input evidence for the next candidate generation. A task transitions to `PASSED` only through acceptance policy; exhausting the repair budget transitions it to `FAILED`.

### Supervisor

`Supervisor` repeatedly recomputes ready tasks from persisted state. Restarting the process does not cause already-passed tasks to be regenerated.

## Target production boundaries

### Planner layer

- global goal decomposition
- explicit acceptance contract per task
- dependency and resource budget generation
- human approval gate for high-impact plans

### Execution backend layer

Adapters:

1. direct VPI Docker runner for small deterministic tasks
2. OpenHands agent-server for richer coding/tool-use sessions
3. future gVisor/microVM backend for stronger isolation

### Evidence matrix

Pluggable gates by artifact type:

- compile / AST
- unit tests
- integration tests
- Ruff
- Mypy/Pyright
- Bandit/Semgrep
- dependency audit
- property tests
- fuzz tests
- benchmark regression
- artifact-specific validators

### Provenance

Every accepted task will record:

- input task hash
- parent project checkpoint
- model/provider identity
- candidate artifact hash
- gate versions and commands
- exact evidence hashes
- resulting Git commit
- timestamps and resource usage

### Recovery

Production recovery is layered:

1. model-generation retry for transient inference faults
2. bounded candidate repair for deterministic failures
3. task replan when the acceptance contract is unattainable
4. Git rollback/worktree discard
5. operator escalation when policy or budget is exhausted
