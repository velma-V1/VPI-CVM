# Contributing

## Required engineering loop

1. State the behavior/invariant being changed.
2. Add a failing behavioral test.
3. Implement the smallest change that passes it.
4. Run the full verification suite.
5. Update architecture/security documentation when authority boundaries change.

## Non-negotiable invariants

- generated code does not execute in the controller process
- missing deterministic evidence never becomes PASS
- model output never bypasses schema validation
- validation sandboxes do not receive unrestricted network or host filesystem access
- terminal accepted state cannot be silently rewritten
- durability/recovery claims require fault-injection or soak-test evidence
