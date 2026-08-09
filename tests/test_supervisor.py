from pathlib import Path

from vpi_cvm.models import TaskSpec, TaskStatus
from vpi_cvm.supervisor import Supervisor
from vpi_cvm.store import SQLiteJournal


class RecordingKernel:
    def __init__(self, store):
        self.store = store
        self.order = []

    def execute(self, task):
        self.order.append(task.id)
        self.store.transition(task.id, TaskStatus.RUNNING)
        self.store.transition(task.id, TaskStatus.PASSED)
        return TaskStatus.PASSED


def test_supervisor_executes_dependency_order_and_resumes(tmp_path: Path):
    store = SQLiteJournal(tmp_path / "state.db")
    tasks = [
        TaskSpec(id="a", objective="A", target_path="a.py"),
        TaskSpec(id="b", objective="B", target_path="b.py", dependencies=["a"]),
    ]
    for task in tasks:
        store.upsert_task(task)
    kernel = RecordingKernel(store)
    result = Supervisor(store=store, kernel=kernel).run(tasks)
    assert result == {"a": TaskStatus.PASSED, "b": TaskStatus.PASSED}
    assert kernel.order == ["a", "b"]

    resumed_kernel = RecordingKernel(store)
    result = Supervisor(store=store, kernel=resumed_kernel).run(tasks)
    assert result == {"a": TaskStatus.PASSED, "b": TaskStatus.PASSED}
    assert resumed_kernel.order == []
