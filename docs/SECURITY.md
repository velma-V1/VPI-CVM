# Security and Threat Model

Status: governing threat model for the executable foundation and Architecture v1 migration.

## Security objective

Assume repository/project content, dependencies, generated artifacts, model outputs, external tools, benchmark inputs, and telemetry may be malformed, misleading, hostile, poisoned, privacy-sensitive, or resource-exhausting.

The controller must not trust generated code merely because it was produced by a local model, and it must not trust text inside project files merely because the model can read it.

Security authority remains deterministic policy/evidence, not model judgment.

## Current protections

### Host filesystem

- all artifact writes pass through canonical workspace containment;
- parent traversal is rejected;
- sibling-prefix path escapes are rejected;
- validation containers see the project bind mount as read-only.

### Process execution

- generated code is never executed with Python `exec()` inside the controller;
- commands are passed as argument arrays; `shell=True` is not used;
- validation occurs in a named disposable container;
- timeout handling kills and force-removes the container.

### Container controls

- network disabled by default;
- root filesystem read-only;
- all capabilities dropped;
- no-new-privileges enabled;
- process count limited;
- RAM limited;
- CPU limited;
- non-root execution user;
- temporary writes restricted to tmpfs.

### Model authority

- structured outputs are schema validated;
- model output cannot mark a task passed;
- acceptance is derived from deterministic evidence.

## Threat classes that Architecture v1 must address

### 1. Prompt/context injection from project data

Repository files, comments, docs, issue text, dependency metadata, generated logs, and retrieved web/research content are **untrusted data**.

Required direction:

- preserve trust/provenance labels in context packets;
- structurally separate system/operator policy from project/retrieved content;
- do not interpret instructions found inside untrusted context as authority;
- constrain model tool permissions independently of textual instructions;
- log trust-boundary violations/suspicious instruction-like content for analysis without assuming a sanitizer can make arbitrary text safe.

Input sanitization alone is not considered a sufficient defense.

### 2. Training, skill, and memory poisoning

Accepted output is not automatically safe training data.

Any dataset used for fine-tuning, adapters, routing calibration, quality calibration, failure memory, or deterministic skill compilation must retain:

- source provenance;
- verification evidence;
- contamination/quarantine state;
- model/runtime/toolchain fingerprints where relevant;
- holdout separation.

Poisoned or disputed examples must be removable without rewriting canonical accepted project history.

### 3. Dependency and plugin supply chain

Dependencies, plugins, foundry components, model weights, containers, and tools can be compromised.

Required direction:

- pin/version dependencies where feasible;
- record content hashes/digests for critical artifacts and images;
- maintain provenance for externally acquired plugins/tools/assets;
- apply allowlists/policy to executable plugins;
- treat signature/hash verification as evidence, not proof that upstream is trustworthy;
- sandbox third-party execution according to risk.

### 4. Adversarial/resource-exhausting artifacts

Generated or retrieved artifacts can exploit parsers/runtimes or exhaust resources.

Examples include archive/zip bombs, pathological images/media, shader or compute workloads, huge generated files, recursive data, malformed binary formats, and resource-amplifying inputs.

Required direction:

- maximum size/expansion/depth/resource policies;
- parser/runtime timeouts;
- disk/I/O quotas;
- GPU scheduling and workload budgets;
- fail-closed handling when resource requirements cannot be established safely.

### 5. Arena/telemetry privacy and contamination

Synthetic task generation must not accidentally expose secrets, credentials, personal data, proprietary artifacts, or hidden evaluation material.

Required direction:

- source-aware redaction/exclusion policy before model/synthetic-task exposure;
- privacy labels on telemetry/evidence;
- hidden/sealed evaluation isolation from candidate-generation contexts;
- contamination events recorded and affected trials invalidated.

### 6. Model/runtime drift as a security concern

A model, quantization, runtime, prompt/tool schema, verifier, or dependency update can change behavior without changing the project task.

Critical configurations require reproducibility fingerprints, canary/sealed replay, and quarantine when behavior moves outside supported operating envelopes.

## What Docker does not solve

Docker containers share the host kernel. A kernel/container-runtime vulnerability can cross the boundary. Docker is therefore treated as a strong local development boundary, **not** as proof of hostile multi-tenant isolation.

For stronger threat profiles the planned backends are:

1. gVisor-style user-space kernel isolation where compatible;
2. disposable microVM execution where hardware/runtime support justifies it;
3. remote sacrificial runners for genuinely untrusted workloads.

## Network policy

Default: `none`.

Future internet-enabled tasks must use an explicit allow-list/proxy or equivalent policy-controlled capability. Direct unrestricted network access will not be enabled by a model request alone.

Egress policy applies to generated code, third-party plugins, foundry workloads, and research/automation components according to their trust class.

## Docker socket

The Docker socket must never be mounted into a generated-code validation container. Access to the Docker daemon is controller-only.

## Secrets

No host secret directories or broad home-directory mounts are part of the sandbox contract.

Future secret access must be:

- least privilege;
- task-scoped;
- short-lived;
- policy approved;
- auditable;
- revoked on task completion/cancellation where feasible.

Secrets must not be copied into living-arena synthetic tasks, quality-calibration datasets, or training/skill datasets by default.

## Denial-of-service and resource limits

Current sandbox limits wall time, memory, CPU and process count.

Planned operational controls add:

- disk/I/O quotas;
- total project/run budgets;
- GPU/VRAM scheduling;
- provider/API concurrency limits;
- artifact size/expansion limits;
- cancellation/preemption;
- circuit breakers for repeated resource failures.

Resource exhaustion must fail the workload and preserve accepted state rather than crash the control plane whenever the host/runtime permits graceful handling.

## GPU execution

GPU access is not granted to validation containers in v0. Model inference occurs through Ollama outside the untrusted validation container. `nvidia-smi` telemetry can inform pause/resume policy without exposing CUDA devices to generated code.

Architecture v1 requires a measured resource scheduler before concurrent local model/foundry workloads are treated as safe. Static VRAM partition assumptions are not security evidence.

## Self-modification boundary

The future Discovery Plane does not receive permission to mutate the running champion directly.

Architectural changes must occur in isolated system candidates and pass focused tests, living/sealed evaluation, adversarial/security checks, recovery tests, and explicit promotion policy. A recoverable prior champion must remain available.

## Security review rule

Every new execution backend, provider/tool capability, telemetry source, training/skill pipeline, research ingestion path, or self-modification mechanism updates this threat model or explicitly demonstrates that existing controls cover it.

See `OPERATIONAL_CONTROL_PLANE.md` for Phase 0 operational requirements and `DISCOVERY_PLANE.md` for the post-v1 self-research boundary.
