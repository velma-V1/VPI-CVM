# ADR 0002 — Generated code executes outside the controller

**Status:** Accepted

## Decision

Never execute generated code with in-process `exec`/`eval`. The initial backend is a disposable Docker container with a read-only project mount and explicit resource/security limits.

## Consequences

- controller survival no longer depends on generated Python behavior
- Docker is not treated as perfect hostile multi-tenant isolation
- stronger gVisor/microVM backends remain compatible with the sandbox protocol
