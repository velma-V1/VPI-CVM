from pathlib import Path

from vpi_cvm.models import EvidenceRecord, GateStatus, TaskSpec, TaskStatus
from vpi_cvm.store import SQLiteJournal


def test_journal_persists_task_state_and_evidence(tmp_path: Path):
    db = SQLiteJournal(tmp_path / "state.db")
    task = TaskSpec(id="t1", objective="build", target_path="src/x.py")
    db.upsert_task(task)
    db.transition("t1", TaskStatus.RUNNING)
    db.record_evidence(EvidenceRecord(task_id="t1", gate="ast", status=GateStatus.PASS, detail="ok"))
    db.close()

    reopened = SQLiteJournal(tmp_path / "state.db")
    assert reopened.get_status("t1") == TaskStatus.RUNNING
    assert reopened.list_evidence("t1")[0].gate == "ast"
    assert reopened.journal_mode().lower() == "wal"
    reopened.close()


def test_transition_rejects_invalid_state_change(tmp_path: Path):
    db = SQLiteJournal(tmp_path / "state.db")
    db.upsert_task(TaskSpec(id="t1", objective="build", target_path="x.py"))
    db.transition("t1", TaskStatus.PASSED)
    try:
        db.transition("t1", TaskStatus.RUNNING)
    except ValueError as exc:
        assert "invalid transition" in str(exc).lower()
    else:
        raise AssertionError("terminal PASSED state must not return to RUNNING")
