from __future__ import annotations

from pathlib import Path

from .evidence import AcceptancePolicy, AstGate
from .models import CandidateGenerator, EvidenceRecord, GateStatus, SandboxRunner, TaskSpec, TaskStatus
from .sandbox import SandboxSpec
from .store import SQLiteJournal
from .workspace import Workspace


class CognitiveKernel:
    """Bounded generate -> deterministic evidence -> repair control loop."""

    def __init__(
        self,
        *,
        store: SQLiteJournal,
        generator: CandidateGenerator,
        sandbox: SandboxRunner,
        workspace: str | Path,
        sandbox_image: str = "vpi-cvm-sandbox:py313",
    ):
        self.store = store
        self.generator = generator
        self.sandbox = sandbox
        self.workspace = Workspace(workspace)
        self.sandbox_image = sandbox_image
        self.ast_gate = AstGate()
        self.policy = AcceptancePolicy(required_gates={"ast", "tests"})

    def execute(self, task: TaskSpec) -> TaskStatus:
        try:
            current = self.store.get_status(task.id)
        except KeyError:
            self.store.upsert_task(task)
            current = TaskStatus.PENDING

        if current == TaskStatus.PASSED:
            return current
        if current != TaskStatus.RUNNING:
            self.store.transition(task.id, TaskStatus.RUNNING)

        for _ in range(task.max_attempts):
            self.store.increment_attempts(task.id)
            prior = self.store.list_evidence(task.id)
            candidate = self.generator.generate(task, prior)

            if candidate.target_path != task.target_path:
                self.store.record_evidence(
                    EvidenceRecord(
                        task_id=task.id,
                        gate="target_path",
                        status=GateStatus.FAIL,
                        detail=f"candidate targeted {candidate.target_path}; expected {task.target_path}",
                    )
                )
                continue

            self.workspace.write_text(candidate.target_path, candidate.content)
            ast_result = self.ast_gate.evaluate(candidate.content, task_id=task.id)
            self.store.record_evidence(ast_result)
            if ast_result.status != GateStatus.PASS:
                continue

            sandbox_result = self.sandbox.run(
                SandboxSpec(
                    workspace=self.workspace.root,
                    image=self.sandbox_image,
                    command=task.validation_command,
                )
            )
            test_status = GateStatus.PASS if sandbox_result.exit_code == 0 and not sandbox_result.timed_out else GateStatus.FAIL
            detail = (
                f"exit={sandbox_result.exit_code} timeout={sandbox_result.timed_out} "
                f"duration_ms={sandbox_result.duration_ms}\nstdout:\n{sandbox_result.stdout}\nstderr:\n{sandbox_result.stderr}"
            )
            self.store.record_evidence(
                EvidenceRecord(task_id=task.id, gate="tests", status=test_status, detail=detail)
            )

            if self.policy.accept(self.store.list_evidence(task.id)):
                self.store.transition(task.id, TaskStatus.PASSED)
                return TaskStatus.PASSED

        self.store.transition(task.id, TaskStatus.FAILED)
        return TaskStatus.FAILED
