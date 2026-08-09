from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .models import EvidenceRecord, GateStatus, TaskSpec, TaskStatus

_ALLOWED_TRANSITIONS: dict[TaskStatus, set[TaskStatus]] = {
    TaskStatus.PENDING: {
        TaskStatus.RUNNING,
        TaskStatus.BLOCKED,
        TaskStatus.FAILED,
        TaskStatus.PASSED,
    },
    TaskStatus.RUNNING: {
        TaskStatus.BLOCKED,
        TaskStatus.PASSED,
        TaskStatus.FAILED,
    },
    TaskStatus.BLOCKED: {TaskStatus.RUNNING, TaskStatus.FAILED},
    TaskStatus.FAILED: {TaskStatus.RUNNING},
    TaskStatus.PASSED: set(),
}


class SQLiteJournal:
    """Small local journal. WAL makes task/evidence state durable across process restarts."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA synchronous=FULL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self._migrate()

    def _migrate(self) -> None:
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    objective TEXT NOT NULL,
                    target_path TEXT NOT NULL,
                    dependencies_json TEXT NOT NULL,
                    validation_command_json TEXT NOT NULL,
                    status TEXT NOT NULL,
                    max_attempts INTEGER NOT NULL,
                    attempts INTEGER NOT NULL DEFAULT 0,
                    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS evidence (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL,
                    gate TEXT NOT NULL,
                    status TEXT NOT NULL,
                    detail TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(task_id) REFERENCES tasks(id)
                )
                """
            )
            self.conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_evidence_task "
                "ON evidence(task_id, id)"
            )

    def close(self) -> None:
        self.conn.close()

    def journal_mode(self) -> str:
        row = self.conn.execute("PRAGMA journal_mode").fetchone()
        return str(row[0])

    def upsert_task(self, task: TaskSpec) -> None:
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO tasks (
                    id, objective, target_path, dependencies_json, validation_command_json,
                    status, max_attempts
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    objective=excluded.objective,
                    target_path=excluded.target_path,
                    dependencies_json=excluded.dependencies_json,
                    validation_command_json=excluded.validation_command_json,
                    max_attempts=excluded.max_attempts,
                    updated_at=CURRENT_TIMESTAMP
                """,
                (
                    task.id,
                    task.objective,
                    task.target_path,
                    json.dumps(task.dependencies),
                    json.dumps(task.validation_command),
                    TaskStatus.PENDING.value,
                    task.max_attempts,
                ),
            )

    def get_status(self, task_id: str) -> TaskStatus:
        row = self.conn.execute(
            "SELECT status FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()
        if row is None:
            raise KeyError(task_id)
        return TaskStatus(row["status"])

    def list_statuses(self) -> dict[str, TaskStatus]:
        rows = self.conn.execute("SELECT id, status FROM tasks ORDER BY id").fetchall()
        return {row["id"]: TaskStatus(row["status"]) for row in rows}

    def transition(self, task_id: str, new_status: TaskStatus) -> None:
        current = self.get_status(task_id)
        if new_status == current:
            return
        if new_status not in _ALLOWED_TRANSITIONS[current]:
            raise ValueError(f"invalid transition: {current.value} -> {new_status.value}")
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                (new_status.value, task_id),
            )

    def increment_attempts(self, task_id: str) -> None:
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET attempts = attempts + 1, "
                "updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                (task_id,),
            )

    def record_evidence(self, evidence: EvidenceRecord) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO evidence (task_id, gate, status, detail) VALUES (?, ?, ?, ?)",
                (evidence.task_id, evidence.gate, evidence.status.value, evidence.detail),
            )

    def list_evidence(self, task_id: str) -> list[EvidenceRecord]:
        rows = self.conn.execute(
            "SELECT task_id, gate, status, detail FROM evidence "
            "WHERE task_id = ? ORDER BY id",
            (task_id,),
        ).fetchall()
        return [
            EvidenceRecord(
                task_id=row["task_id"],
                gate=row["gate"],
                status=GateStatus(row["status"]),
                detail=row["detail"],
            )
            for row in rows
        ]
