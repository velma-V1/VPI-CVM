from __future__ import annotations

import argparse
import json
from pathlib import Path

from .kernel import CognitiveKernel
from .models import ProjectPlan
from .ollama import OllamaGenerator, OllamaPlanner
from .sandbox import DockerSandbox
from .store import SQLiteJournal
from .supervisor import Supervisor


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vpi-cvm")
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan", help="Create a schema-validated task DAG from a goal")
    plan.add_argument("--goal", required=True)
    plan.add_argument("--model", required=True)
    plan.add_argument("--output", default="vpi-plan.json")
    plan.add_argument("--ollama-url", default="http://localhost:11434")

    run = sub.add_parser(
        "run",
        help="Execute a persisted plan through deterministic evidence gates",
    )
    run.add_argument("--plan", required=True)
    run.add_argument("--model", required=True)
    run.add_argument("--workspace", default="vpi-workspace")
    run.add_argument("--db", default=".vpi-cvm/state.db")
    run.add_argument("--image", default="vpi-cvm-sandbox:py313")
    run.add_argument("--ollama-url", default="http://localhost:11434")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.command == "plan":
        planner = OllamaPlanner(model=args.model, base_url=args.ollama_url)
        plan = planner.plan(args.goal)
        Path(args.output).write_text(plan.model_dump_json(indent=2), encoding="utf-8")
        print(f"wrote {args.output}")
        return 0

    plan = ProjectPlan.model_validate_json(Path(args.plan).read_text(encoding="utf-8"))
    store = SQLiteJournal(args.db)
    try:
        generator = OllamaGenerator(model=args.model, base_url=args.ollama_url)
        sandbox = DockerSandbox()
        kernel = CognitiveKernel(
            store=store,
            generator=generator,
            sandbox=sandbox,
            workspace=args.workspace,
            sandbox_image=args.image,
        )
        statuses = Supervisor(store=store, kernel=kernel).run(plan.tasks)
        print(
            json.dumps(
                {task_id: status.value for task_id, status in statuses.items()},
                indent=2,
            )
        )
        return 0 if all(status.value == "PASSED" for status in statuses.values()) else 2
    finally:
        store.close()


if __name__ == "__main__":
    raise SystemExit(main())
