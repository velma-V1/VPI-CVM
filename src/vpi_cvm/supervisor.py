from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol

from .models import TaskSpec, TaskStatus
from .planning import TaskGraph
from .store import SQLiteJournal


class KernelProtocol(Protocol):
    def execute(self, task: TaskSpec) -> TaskStatus: ...


class Supervisor:
    """Resumable dependency-aware task dispatcher over persisted task state."""

    def __init__(self, *, store: SQLiteJournal, kernel: KernelProtocol):
        self.store = store
        self.kernel = kernel

    def run(self, tasks: Iterable[TaskSpec]) -> dict[str, TaskStatus]:
        task_list = list(tasks)
        graph = TaskGraph(task_list)
        for task in task_list:
            try:
                self.store.get_status(task.id)
            except KeyError:
                self.store.upsert_task(task)

        while True:
            statuses = self.store.list_statuses()
            ready = graph.ready(statuses)
            if not ready:
                return {task.id: statuses[task.id] for task in task_list}
            for task in ready:
                self.kernel.execute(task)
