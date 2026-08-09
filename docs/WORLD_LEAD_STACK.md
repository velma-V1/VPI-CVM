# VPI-CVM World-Leading Target Stack — Historical Research Note

Status: **historical / non-governing**.

This document captured the competition-framed research pass that compared frontier models, local runtimes, execution backends, project-intelligence components, verification tools, and benchmark infrastructure.

The tournament framing was useful because it forced evidence, falsifiability, same-harness comparison, and resistance to model/vendor hype. It is no longer the purpose of VPI-CVM.

The governing architecture is now [`ARCHITECTURE.md`](ARCHITECTURE.md), and the build sequence is [`PLAN.md`](PLAN.md).

## Research conclusions retained

- no model is permanent authority or permanent winner;
- local and frontier models remain eligible compute lanes selected empirically;
- exact project intelligence precedes generic vector retrieval for code relationships;
- Tree-sitter/SCIP/coverage/CodeQL and similar components are challengers whose value must be measured rather than assumed;
- generated code executes outside the controller in isolated candidate environments;
- worktree isolation, gVisor/microVM tiers, SWE-ReX-style execution abstraction, and durable workflow backends remain valid implementation candidates;
- adaptive verification, hidden/rotating evaluation, and reproducible same-harness measurement remain mandatory;
- repeated verified neural operations may compile into deterministic skills;
- public/vendor benchmark claims never substitute for VPI-CVM's own measured outcomes.

## Research conclusions corrected later

Architecture v1 no longer optimizes for tournament victory or treats software-engineering benchmarks as the system purpose. It now optimizes for accumulated **verified, goal-correct, reusable capability per unit of human time, machine compute, and experience**.

The current architecture also adds mechanisms not fully represented in this earlier stack note:

- explicit resident intelligence independent of model/KV state;
- immutable world snapshots;
- Living Arena plus sealed/rotating truth;
- adversarial counterexample search with deterministic arbitration;
- realized-value accounting;
- separate correctness / goal-conformance / quality epistemic planes;
- human intent/value state;
- domain-specific world models;
- evidence-backed cross-domain transfer research.

Specific model names, prices, benchmark results, and runtime rankings in the original research pass were time-sensitive and should be re-measured before implementation decisions. The full historical version remains available in Git history.
