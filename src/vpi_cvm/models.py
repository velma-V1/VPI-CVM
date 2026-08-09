from __future__ import annotations

from enum import StrEnum
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from .sandbox import SandboxSpec


class TaskStatus(StrEnum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    BLOCKED = "BLOCKED"
    PASSED = "PASSED"
    FAILED = "FAILED"


class GateStatus(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"


class TaskSpec(BaseModel):
    id: str = Field(min_length=1)
    objective: str = Field(min_length=1)
    target_path: str = Field(min_length=1)
    dependencies: list[str] = Field(default_factory=list)
    validation_command: list[str] = Field(
        default_factory=lambda: ["python", "-m", "pytest", "-q"]
    )
    max_attempts: int = Field(default=3, ge=1, le=20)


class ProjectPlan(BaseModel):
    project_name: str = Field(min_length=1)
    tasks: list[TaskSpec] = Field(min_length=1)


class CandidateArtifact(BaseModel):
    target_path: str = Field(min_length=1)
    content: str


class EvidenceRecord(BaseModel):
    task_id: str
    gate: str
    status: GateStatus
    detail: str = ""


class SandboxResult(BaseModel):
    exit_code: int | None
    stdout: str
    stderr: str
    timed_out: bool
    duration_ms: int


class CandidateGenerator(Protocol):
    def generate(
        self,
        task: TaskSpec,
        prior_evidence: list[EvidenceRecord],
    ) -> CandidateArtifact: ...


class SandboxRunner(Protocol):
    def run(self, spec: SandboxSpec) -> SandboxResult: ...


class SandboxSpecProtocol(Protocol):
    workspace: Path
