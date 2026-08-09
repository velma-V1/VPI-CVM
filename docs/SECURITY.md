# Security and Threat Model

## Security objective

Assume generated project content can be malformed, destructive, resource-exhausting or intentionally hostile. The controller must not trust generated code merely because it was produced by a local model.

## Current protections

### Host filesystem

- all artifact writes pass through canonical workspace containment
- parent traversal is rejected
- sibling-prefix path escapes are rejected
- validation containers see the project bind mount as read-only

### Process execution

- generated code is never executed with Python `exec()` inside the controller
- commands are passed as argument arrays; `shell=True` is not used
- validation occurs in a named disposable container
- timeout handling kills and force-removes the container

### Container controls

- network disabled by default
- root filesystem read-only
- all capabilities dropped
- no-new-privileges enabled
- process count limited
- RAM limited
- CPU limited
- non-root execution user
- temporary writes restricted to tmpfs

### Model authority

- structured outputs are schema validated
- model output cannot mark a task passed
- acceptance is derived from deterministic evidence

## What Docker does not solve

Docker containers share the host kernel. A kernel/container-runtime vulnerability can cross the boundary. Docker is therefore treated as a strong local development boundary, **not** as proof of hostile multi-tenant isolation.

For stronger threat profiles the planned backends are:

1. gVisor-style user-space kernel isolation where compatible
2. disposable microVM execution where hardware/runtime support justifies it
3. remote sacrificial runners for genuinely untrusted workloads

## Network policy

Default: `none`.

Future internet-enabled tasks must use an explicit allow-list proxy. Direct unrestricted network access will not be enabled by a model request alone.

## Docker socket

The Docker socket must never be mounted into a generated-code validation container. Access to the Docker daemon is controller-only.

## Secrets

No host secret directories or broad home-directory mounts are part of the sandbox contract. Future secret access must be capability-scoped, short-lived and policy approved.

## Denial-of-service limits

Current sandbox limits wall time, memory, CPU and process count. Future work adds disk quotas, I/O budgets, total project budgets and GPU job scheduling.

## GPU execution

GPU access is not granted to validation containers in v0. Model inference occurs through Ollama outside the untrusted validation container. `nvidia-smi` telemetry can inform pause/resume policy without exposing CUDA devices to generated code.
