import json

from vpi_cvm.models import CandidateArtifact, TaskSpec
from vpi_cvm.ollama import OllamaGenerator, OllamaPlanner


class FakeTransport:
    def __init__(self, response):
        self.response = response
        self.payloads = []

    def post_json(self, url, payload, timeout):
        self.payloads.append((url, payload, timeout))
        return self.response


def test_generator_uses_schema_constrained_output_and_unloads_model():
    transport = FakeTransport({"response": json.dumps({"target_path": "src/x.py", "content": "x = 1\n"})})
    generator = OllamaGenerator(model="qwen3:8b", transport=transport)
    result = generator.generate(TaskSpec(id="t", objective="make x", target_path="src/x.py"), [])
    assert result == CandidateArtifact(target_path="src/x.py", content="x = 1\n")
    payload = transport.payloads[0][1]
    assert payload["format"]["type"] == "object"
    assert payload["keep_alive"] == 0
    assert payload["stream"] is False
    assert payload["options"]["temperature"] == 0


def test_planner_returns_validated_task_graph():
    response = {"response": json.dumps({"project_name": "demo", "tasks": [
        {"id": "a", "objective": "A", "target_path": "a.py", "dependencies": []},
        {"id": "b", "objective": "B", "target_path": "b.py", "dependencies": ["a"]},
    ]})}
    planner = OllamaPlanner(model="qwen3:8b", transport=FakeTransport(response))
    plan = planner.plan("build demo")
    assert [task.id for task in plan.tasks] == ["a", "b"]
