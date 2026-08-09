# VPI-CVM World-Leading Target Stack

Status: governing target architecture for the competition-grade system. This document does not claim unfinished capabilities are implemented.

## Objective

VPI-CVM is not an autonomous-chat loop and it is not tied to one model. It is a deterministic, evidence-driven software-engineering control plane that compiles project state into minimal neural work, executes candidates in isolated environments, and accepts only machine-verified outcomes.

The optimization target is **verified engineering output per unit of time, cost, and compute**, not raw model elo or token count.

## Non-negotiable invariants

1. Models propose; deterministic evidence accepts or rejects.
2. Workflow topology is deterministic. Neural models operate only at typed leaf nodes.
3. No model is permanently crowned. Routing is determined by sealed VPI-CVM evaluations per task class.
4. No generated code executes in the controller process.
5. Every mutable candidate starts from an immutable accepted Git commit in an isolated worktree/sandbox.
6. Project context is symbol- and graph-derived first; embeddings are secondary and never authoritative for code relationships.
7. Repeated verified neural behavior is eligible for compilation into deterministic skills.
8. Public benchmark claims never substitute for VPI-CVM's private, contamination-resistant evaluation suite.

## 1. Neural compute portfolio

### Frontier deep lane

- **GPT-5.6 Sol (max reasoning)** — initial primary candidate for difficult coding, architecture, repair, and synthesis tasks.
- **Claude Fable 5** — independent frontier candidate/advisor for hard software engineering and long-horizon work.
- **Kimi K3** — independent long-context/repository-scale candidate; use hosted/API inference unless infrastructure makes self-hosting economically justified.

No one of these is the verifier. For high-risk tasks VPI-CVM may request independent candidates from two or more models and let deterministic acceptance gates select the winner.

### Fast / high-throughput frontier lane

- **Gemini 3.5 Flash** — high-speed multimodal and computer-use lane when GUI/visual understanding is genuinely required.
- **MiniMax M3** — low-cost long-context candidate generation and parallel hypothesis lane.

### Local/offline lane

- **Qwen3.5-9B** — fast local typed leaf work on constrained hardware.
- **Qwen3-Coder-Next** — preferred open coding-specialist candidate when adequate multi-GPU or rented inference capacity is available.

The local tier handles bounded operations: classification, failure compression, small patch proposals, test skeletons, symbol summarization, and deterministic-schema transformations. It is not allowed to receive architecture- or security-critical tasks merely to save API cost.

## 2. Empirical model router

Routing has two layers:

### Hard boundaries

Measured task features determine which model classes are eligible:

- files and symbols affected
- dependency radius
- public API changes
- concurrency involvement
- security-boundary crossings
- test/coverage gaps
- migration/state changes
- expected context size
- prior failed attempts

Safety- or architecture-critical work cannot be downgraded below configured capability floors.

### Learned routing inside the boundary

For each `(task_class, model, runtime, reasoning_config)` VPI-CVM records:

- verified pass rate
- hidden/adversarial test pass rate
- regressions introduced
- retries
- wall-clock time
- input/output tokens
- GPU time where applicable
- dollar cost

The router selects from empirical posterior performance rather than vendor ranking. Tournament mode strongly favors exploitation; controlled exploration runs outside critical competition paths.

## 3. Provider layer

Use narrow, typed first-party provider adapters rather than making a third-party multi-provider gateway part of the correctness-critical path.

Required adapters:

- OpenAI Responses API
- Anthropic API
- Google Gemini API
- Moonshot/Kimi API
- MiniMax API
- OpenAI-compatible local endpoint

Common VPI types are intentionally smaller than any provider API. Provider-specific capabilities remain available through capability negotiation rather than being erased by a lowest-common-denominator abstraction.

## 4. Inference runtimes

### Single-GPU / workstation

**llama.cpp** is the primary local runtime: explicit quantization, CUDA offload, KV-cache controls, CPU/GPU hybrid inference, and speculative decoding are directly tunable.

Ollama may remain a convenience adapter for development but is not the reference competition runtime.

### Multi-GPU / server

**SGLang** is the initial primary serving runtime because VPI-CVM benefits directly from prefix caching, continuous batching, structured outputs, speculative decoding, paged attention, and distributed parallelism.

**TensorRT-LLM** and **vLLM** are retained as benchmarked alternatives. VPI-CVM chooses the runtime per model/hardware combination from measured TTFT, tokens/sec, memory use, reliability, and structured-output correctness. Runtime choice is not ideological.

## 5. Project Intelligence Fabric

The context system is not generic vector RAG.

### Syntax layer

- Tree-sitter incremental parsing
- language-specific AST/type extraction where stronger native tooling exists

### Semantic code-intelligence layer

- SCIP indexes for definitions, references, and implementations across supported languages
- Git history/blame/diff relationships
- test-to-symbol mapping from static references and dynamic coverage
- import/dependency graph
- build targets and package boundaries

### Deep analysis layer

- CodeQL data-flow/taint analysis on demand
- language type checkers and compiler metadata

### Storage

Keep control-plane truth in SQLite WAL. Store project graph nodes/edges and FTS indexes in embedded indexed tables until measurements prove a dedicated graph database is necessary.

### Context compiler

For every task it produces a bounded context contract containing exact symbols, source ranges, signatures, callers/callees, relevant tests, recent changes, failure evidence, and provenance. Semantic embeddings may help retrieve prose/docs, but cannot invent code relationships.

## 6. Deterministic workflow brain

Workflow selection is deterministic by task class.

Examples:

- bugfix: reproduce -> localize -> hypothesize -> patch -> verify -> adversarial verify -> checkpoint
- feature: contract -> impact analysis -> failing test -> implementation -> integration verify -> adversarial verify -> checkpoint
- refactor: baseline -> dependency map -> transform -> behavioral equivalence -> performance gate -> checkpoint
- security: boundary map -> reproduce -> patch -> exploit regression -> static/data-flow/dependency gates -> checkpoint

Models can populate typed nodes (hypotheses, patches, tests, summaries); they do not skip or reorder mandatory gates.

## 7. Execution fabric

Do not expand VPI-CVM into a bespoke remote-shell platform.

- **SWE-ReX**: primary execution-environment abstraction for local/remote/parallel shell sessions.
- **gVisor/runsc**: default high-isolation container runtime for untrusted candidate execution where compatibility permits.
- **Firecracker microVM**: higher-assurance isolation tier for high-risk/final acceptance workloads on native Linux/KVM infrastructure.
- **OpenHands Software Agent SDK/Agent Server**: optional rich coding-agent backend when a task genuinely needs a mature interactive agent. VPI-CVM retains planning policy, budgets, project truth, and final acceptance authority.

Network is deny-by-default; exceptions use explicit allowlists. Secrets are short-lived and task-scoped. The controller never exposes its host Docker socket or unrestricted host filesystem to generated code.

## 8. Verification Forge

Verification is the main engine, not the last stage.

Python reference gate stack:

1. syntax/AST/compile
2. Ruff lint/format check
3. Pyright type check
4. existing pytest suite
5. independently generated regression tests
6. Hypothesis property-based tests when contracts expose useful invariants
7. mutation testing (Mutmut) for risk-selected changed code
8. Semgrep and/or CodeQL security/data-flow gates by risk class
9. OSV-Scanner dependency vulnerability gate
10. integration/contract tests
11. performance/resource regression gates where relevant

Other languages implement equivalent compiler/linter/type/test/security plugins.

Failures become structured counterexamples: exact test, expected/actual behavior, changed path, stack/data-flow evidence, surviving mutants, and repair constraints. Models receive this evidence rather than vague "try again" prompts.

## 9. Candidate tournament engine

High-uncertainty tasks can create independent candidate worktrees from the same accepted base commit.

Candidate selection uses deterministic evidence in this order:

1. mandatory correctness/security gates
2. hidden/adversarial test performance
3. behavioral regression count
4. mutation score/coverage delta
5. public API/dependency impact
6. performance/resource impact
7. patch complexity/changed LOC as a final tie-breaker

An LLM may explain the evidence but never overrides failed mandatory gates.

## 10. Verified Skill Compiler

Successful operations are fingerprinted by task pattern, AST/context signature, transformation, and verification evidence.

Promotion stages:

`NEURAL -> REPEATED_VERIFIED -> SHADOW_DETERMINISTIC -> VALIDATED_SKILL -> DETERMINISTIC`

A promotion must replay successfully against historical examples and a held-out adversarial set. Suitable compiled forms include ast-grep/tree-sitter rewrites, deterministic scripts, templates, and specialized analyzers.

The objective is that VPI-CVM gradually stops spending inference on operations it has empirically mastered.

## 11. Durable orchestration

**Temporal** owns crash-resumable multi-day workflow execution. VPI-CVM owns domain state and evidence; Temporal owns durable workflow history, retries, timers, pause/resume/cancel, and recovery after controller/machine failure.

Do not build another home-grown long-running scheduler.

## 12. Benchmark and training arena

A component cannot be called "best" until it wins under the same VPI-CVM contract.

Public external checks:

- SWE-bench Verified / relevant SWE-bench variants
- Terminal-Bench
- CodeClash for goal-oriented development

Private evaluation:

- use SWE-smith to turn selected repositories into executable software-engineering gyms
- synthesize private repair/localization/refactor tasks
- maintain hidden tests that no candidate model sees
- include security, concurrency, migration, performance, and stale-context failures
- rotate repositories and task generation to reduce contamination

Measure at minimum:

- verified pass@1
- hidden-test pass rate
- regressions
- time-to-verified-solution
- cost-to-verified-solution
- tokens and GPU time
- retries/backtracks
- context bytes/tokens
- operator interventions

### Project-specialized model improvement

Do not fine-tune first. First accumulate verified VPI-CVM trajectories and SWE-smith tasks. Once the dataset is large and diverse enough, train/LoRA/RL an open coding model such as Qwen3-Coder-Next and require it to beat its base model on the sealed suite before promotion.

Only machine-verified successful trajectories are eligible for the high-quality training corpus; failures may be retained separately for preference/counterexample learning.

## 13. Hardware and host strategy

Competition infrastructure should be native Linux because KVM/Firecracker, gVisor, high-performance inference runtimes, and software-engineering evaluation infrastructure are Linux-first.

A small local GPU remains useful for low-latency leaf inference and development. Frontier models should normally be consumed through APIs unless tournament rules require offline execution. Self-hosting multi-trillion-parameter open models is a datacenter decision, not a workstation optimization.

When local frontier-scale inference is required, provision/rent modern multi-GPU capacity and benchmark SGLang, TensorRT-LLM, and vLLM on the exact model rather than selecting hardware/runtime from marketing specifications.

## 14. Build order

### Sprint A — measurement before mythology

1. sealed benchmark arena and metrics schema
2. model/provider adapter protocol
3. same-harness model shootout
4. baseline cost/latency/correctness dashboard

### Sprint B — project brain

5. Tree-sitter ingestion
6. SCIP ingestion
7. Git/test/coverage graph
8. bounded context compiler
9. context provenance tests

### Sprint C — verification and isolation

10. SWE-ReX adapter
11. gVisor backend
12. Git worktree candidate isolation
13. complete verification plugin matrix
14. structured counterexample feedback

### Sprint D — competition intelligence

15. deterministic workflow FSMs
16. empirical capability router
17. multi-candidate tournament engine
18. runtime auto-benchmarking (llama.cpp/SGLang/TensorRT-LLM/vLLM)

### Sprint E — compounding advantage

19. verified skill registry/compiler
20. SWE-smith private task generation
21. verified trajectory corpus
22. optional project-specialized Qwen training

### Sprint F — endurance

23. Temporal workflow backend
24. optional OpenHands backend
25. fault injection
26. 24-hour soak
27. 7-day soak
28. 30-day supervised endurance test

## Evidence sources reviewed for this target

- OpenAI GPT-5.6 release and engineering notes
- Anthropic Claude Fable 5 / Mythos 5 release material
- Moonshot Kimi K3 model card
- MiniMax M3 release material
- Google Gemini 3.5 release material
- Qwen3-Coder-Next and Qwen3.5 model cards
- SGLang, vLLM, llama.cpp, TensorRT-LLM documentation
- Tree-sitter, SCIP, CodeQL documentation
- SWE-bench, SWE-smith, SWE-ReX, CodeClash
- gVisor, Firecracker, Temporal, OpenHands documentation
- Ruff, Pyright, Hypothesis, Mutmut, OSV-Scanner documentation

## Final acceptance rule

VPI-CVM earns a "world-leading" claim only if the sealed evaluation shows it. Architecture quality, vendor benchmarks, model size, and rhetoric are hypotheses until the same-harness evidence says otherwise.
