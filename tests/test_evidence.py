from vpi_cvm.evidence import AcceptancePolicy, AstGate
from vpi_cvm.models import EvidenceRecord, GateStatus


def test_ast_gate_rejects_invalid_python():
    result = AstGate().evaluate("def broken(:\n    pass\n")
    assert result.status == GateStatus.FAIL
    assert "SyntaxError" in result.detail


def test_acceptance_requires_every_required_gate_to_pass():
    policy = AcceptancePolicy(required_gates={"ast", "tests"})
    evidence = [
        EvidenceRecord(task_id="t", gate="ast", status=GateStatus.PASS, detail="ok"),
        EvidenceRecord(task_id="t", gate="tests", status=GateStatus.FAIL, detail="1 failed"),
    ]
    assert policy.accept(evidence) is False


def test_acceptance_rejects_missing_required_gate():
    policy = AcceptancePolicy(required_gates={"ast", "tests"})
    evidence = [EvidenceRecord(task_id="t", gate="ast", status=GateStatus.PASS, detail="ok")]
    assert policy.accept(evidence) is False
