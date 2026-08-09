import json
from pathlib import Path

from vpi_cvm.models import ProjectPlan, TaskSpec


def test_plan_command_writes_validated_plan(tmp_path: Path, monkeypatch):
    import vpi_cvm.cli as cli

    class FakePlanner:
        def __init__(self, **kwargs):
            pass

        def plan(self, goal):
            assert goal == "build demo"
            return ProjectPlan(
                project_name="demo",
                tasks=[TaskSpec(id="a", objective="A", target_path="a.py")],
            )

    monkeypatch.setattr(cli, "OllamaPlanner", FakePlanner)
    output = tmp_path / "plan.json"
    code = cli.main(
        [
            "plan",
            "--goal",
            "build demo",
            "--model",
            "qwen3:8b",
            "--output",
            str(output),
        ]
    )
    assert code == 0
    data = json.loads(output.read_text())
    assert data["project_name"] == "demo"
    assert data["tasks"][0]["id"] == "a"


def test_run_command_loads_plan_and_reports_status(tmp_path: Path, monkeypatch, capsys):
    import vpi_cvm.cli as cli

    plan_path = tmp_path / "plan.json"
    plan_path.write_text(
        ProjectPlan(
            project_name="demo",
            tasks=[TaskSpec(id="a", objective="A", target_path="a.py")],
        ).model_dump_json()
    )

    class FakeStore:
        def __init__(self, path):
            self.path = path

        def close(self):
            pass

    class Dummy:
        def __init__(self, **kwargs):
            pass

    class FakeSupervisor:
        def __init__(self, **kwargs):
            pass

        def run(self, tasks):
            from vpi_cvm.models import TaskStatus

            return {"a": TaskStatus.PASSED}

    monkeypatch.setattr(cli, "SQLiteJournal", FakeStore)
    monkeypatch.setattr(cli, "OllamaGenerator", Dummy)
    monkeypatch.setattr(cli, "DockerSandbox", Dummy)
    monkeypatch.setattr(cli, "CognitiveKernel", Dummy)
    monkeypatch.setattr(cli, "Supervisor", FakeSupervisor)

    code = cli.main(
        [
            "run",
            "--plan",
            str(plan_path),
            "--model",
            "qwen3:8b",
            "--workspace",
            str(tmp_path / "work"),
            "--db",
            str(tmp_path / "state.db"),
        ]
    )
    assert code == 0
    assert '"a": "PASSED"' in capsys.readouterr().out
