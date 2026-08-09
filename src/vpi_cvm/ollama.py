from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass
from typing import Any, Protocol, TypeVar

from pydantic import BaseModel

from .models import CandidateArtifact, EvidenceRecord, ProjectPlan, TaskSpec
from .planning import TaskGraph

T = TypeVar("T", bound=BaseModel)


class JsonTransport(Protocol):
    def post_json(
        self,
        url: str,
        payload: dict[str, Any],
        timeout: int,
    ) -> dict[str, Any]: ...


class UrllibJsonTransport:
    def post_json(
        self,
        url: str,
        payload: dict[str, Any],
        timeout: int,
    ) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=body,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))


@dataclass
class OllamaStructuredClient:
    model: str
    base_url: str = "http://localhost:11434"
    timeout_seconds: int = 180
    transport: JsonTransport | None = None

    def __post_init__(self) -> None:
        if self.transport is None:
            self.transport = UrllibJsonTransport()

    def generate(self, *, system: str, prompt: str, schema: type[T]) -> T:
        payload = {
            "model": self.model,
            "system": system,
            "prompt": prompt,
            "stream": False,
            "format": schema.model_json_schema(),
            "keep_alive": 0,
            "options": {"temperature": 0},
        }
        assert self.transport is not None
        response = self.transport.post_json(
            f"{self.base_url.rstrip('/')}/api/generate",
            payload,
            self.timeout_seconds,
        )
        raw = response.get("response")
        if not isinstance(raw, str):
            raise RuntimeError("Ollama response did not contain a string 'response' field")
        return schema.model_validate_json(raw)


class OllamaPlanner:
    def __init__(
        self,
        *,
        model: str,
        base_url: str = "http://localhost:11434",
        transport: JsonTransport | None = None,
    ):
        self.client = OllamaStructuredClient(
            model=model,
            base_url=base_url,
            transport=transport,
        )

    def plan(self, goal: str) -> ProjectPlan:
        plan = self.client.generate(
            system=(
                "You are VPI-CVM's planner. Decompose the goal into atomic "
                "implementation tasks. Each task targets exactly one artifact path, "
                "declares dependencies by task id, and includes a deterministic "
                "validation command. Return only schema-valid JSON."
            ),
            prompt=f"Project goal:\n{goal}",
            schema=ProjectPlan,
        )
        TaskGraph(plan.tasks)
        return plan


class OllamaGenerator:
    def __init__(
        self,
        *,
        model: str,
        base_url: str = "http://localhost:11434",
        transport: JsonTransport | None = None,
    ):
        self.client = OllamaStructuredClient(
            model=model,
            base_url=base_url,
            transport=transport,
        )

    def generate(
        self,
        task: TaskSpec,
        prior_evidence: list[EvidenceRecord],
    ) -> CandidateArtifact:
        evidence_text = "\n".join(
            f"- {item.gate}: {item.status.value}: {item.detail}"
            for item in prior_evidence[-12:]
        ) or "- none"
        return self.client.generate(
            system=(
                "You are VPI-CVM's artifact generator. Produce the complete contents "
                "for exactly the requested target_path. Treat deterministic evidence "
                "from prior attempts as ground truth. Do not change the target path. "
                "Do not emit markdown fences."
            ),
            prompt=(
                f"Task id: {task.id}\n"
                f"Objective: {task.objective}\n"
                f"Target path: {task.target_path}\n"
                f"Validation command: {task.validation_command}\n"
                f"Prior evidence:\n{evidence_text}"
            ),
            schema=CandidateArtifact,
        )
