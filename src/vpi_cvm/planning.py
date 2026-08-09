from __future__ import annotations

from collections.abc import Iterable, Mapping

from .models import TaskSpec, TaskStatus


class TaskGraph:
    """Validated dependency graph for atomic project tasks."""

    def __init__(self, tasks: Iterable[TaskSpec]):
        self.tasks = {task.id: task for task in tasks}
        if not self.tasks:
            raise ValueError("task graph cannot be empty")
        self._validate_dependencies()
        self._validate_acyclic()

    def _validate_dependencies(self) -> None:
        for task in self.tasks.values():
            unknown = [dep for dep in task.dependencies if dep not in self.tasks]
            if unknown:
                raise ValueError(f"task {task.id} has unknown dependencies: {unknown}")
            if task.id in task.dependencies:
                raise ValueError(f"task graph contains cycle at {task.id}")

    def _validate_acyclic(self) -> None:
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(task_id: str) -> None:
            if task_id in visiting:
                raise ValueError(f"task graph contains cycle at {task_id}")
            if task_id in visited:
                return
            visiting.add(task_id)
            for dep in self.tasks[task_id].dependencies:
                visit(dep)
            visiting.remove(task_id)
            visited.add(task_id)

        for task_id in self.tasks:
            visit(task_id)

    def ready(self, statuses: Mapping[str, TaskStatus]) -> list[TaskSpec]:
        ready: list[TaskSpec] = []
        for task in self.tasks.values():
            status = statuses.get(task.id, TaskStatus.PENDING)
            if status != TaskStatus.PENDING:
                continue
            if all(statuses.get(dep) == TaskStatus.PASSED for dep in task.dependencies):
                ready.append(task)
        return ready
