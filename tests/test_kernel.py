from pathlib import Path

from vpi_cvm.kernel import CognitiveKernel
from vpi_cvm.models import (
    CandidateArtifact,
    GateStatus,
    SandboxResult,
    TaskSpec,
    TaskStatus,
)
from vpi_cvm.store import SQLiteJournal


class SequenceGenerator:
    def __init__(self):
        self.calls = 0

    def generate(self, task, prior_evidence):
        self.calls += 1
        if self.calls == 1:
            return CandidateArtifact(
                target_path=task.target_path,
                content="def broken(:\n",
            )
        return CandidateArtifact(
            target_path=task.target_path,
            content="def answer():\n    return 42\n",
        )


class PassingSandbox:
    def run(self, spec):
        return SandboxResult(
            exit_code=0,
            stdout="1 passed",
            stderr="",
            timed_out=False,
            duration_ms=5,
        )


def test_kernel_repairs_after_deterministic_gate_failure(tmp_path: Path):
    store = SQLiteJournal(tmp_path / "state.db")
    task = TaskSpec(
        id="t1",
        objective="return 42",
        target_path="src/answer.py",
        max_attempts=2,
    )
    store.upsert_task(task)
    kernel = CognitiveKernel(
        store=store,
        generator=SequenceGenerator(),
        sandbox=PassingSandbox(),
        workspace=tmp_path / "work",
    )

    status = kernel.execute(task)

    assert status == TaskStatus.PASSED
    assert store.get_status("t1") == TaskStatus.PASSED
    evidence = store.list_evidence("t1")
    assert any(e.gate == "ast" and e.status == GateStatus.FAIL for e in evidence)
    assert any(e.gate == "tests" and e.status == GateStatus.PASS for e in evidence)
    assert (
        tmp_path / "work" / "src" / "answer.py"
    ).read_text() == "def answer():\n    return 42\n"
