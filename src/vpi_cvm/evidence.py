from __future__ import annotations

import ast
from dataclasses import dataclass

from .models import EvidenceRecord, GateStatus


@dataclass(frozen=True)
class AstGate:
    name: str = "ast"

    def evaluate(self, source: str, task_id: str = "") -> EvidenceRecord:
        try:
            ast.parse(source)
        except SyntaxError as exc:
            location = f"line {exc.lineno}, column {exc.offset}"
            return EvidenceRecord(
                task_id=task_id,
                gate=self.name,
                status=GateStatus.FAIL,
                detail=f"SyntaxError at {location}: {exc.msg}",
            )
        return EvidenceRecord(
            task_id=task_id,
            gate=self.name,
            status=GateStatus.PASS,
            detail="AST parse passed",
        )


@dataclass(frozen=True)
class AcceptancePolicy:
    required_gates: set[str]

    def accept(self, evidence: list[EvidenceRecord]) -> bool:
        latest: dict[str, GateStatus] = {}
        for record in evidence:
            latest[record.gate] = record.status
        return all(latest.get(gate) == GateStatus.PASS for gate in self.required_gates)
