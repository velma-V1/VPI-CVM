import pytest

from vpi_cvm.models import TaskSpec, TaskStatus
from vpi_cvm.planning import TaskGraph


def test_ready_tasks_require_all_dependencies_complete():
    graph = TaskGraph([
        TaskSpec(id="a", objective="A", target_path="a.py"),
        TaskSpec(id="b", objective="B", target_path="b.py", dependencies=["a"]),
    ])
    assert [t.id for t in graph.ready({})] == ["a"]
    assert [t.id for t in graph.ready({"a": TaskStatus.PASSED})] == ["b"]


def test_cycle_is_rejected():
    with pytest.raises(ValueError, match="cycle"):
        TaskGraph([
            TaskSpec(id="a", objective="A", target_path="a.py", dependencies=["b"]),
            TaskSpec(id="b", objective="B", target_path="b.py", dependencies=["a"]),
        ])
