from __future__ import annotations

import subprocess
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path

from .models import SandboxResult


@dataclass(frozen=True)
class SandboxSpec:
    workspace: Path
    image: str
    command: list[str]
    timeout_seconds: int = 120
    memory: str = "2g"
    cpus: str = "2.0"
    pids_limit: int = 256
    user: str = "65534:65534"
    environment: dict[str, str] = field(default_factory=dict)


class DockerSandbox:
    """Disposable Docker execution boundary. It never uses shell=True or privileged mode."""

    def build_command(self, spec: SandboxSpec, *, container_name: str | None = None) -> list[str]:
        workspace = spec.workspace.resolve()
        command = [
            "docker",
            "run",
            "--rm",
        ]
        if container_name:
            command.extend(["--name", container_name])
        command.extend(
            [
                "--network",
                "none",
                "--read-only",
                "--cap-drop",
                "ALL",
                "--security-opt",
                "no-new-privileges",
                "--pids-limit",
                str(spec.pids_limit),
                "--memory",
                spec.memory,
                "--cpus",
                spec.cpus,
                "--user",
                spec.user,
                "--tmpfs",
                "/tmp:rw,noexec,nosuid,size=256m",
                "--mount",
                f"type=bind,src={workspace},dst=/workspace,ro",
                "--workdir",
                "/workspace",
                "--env",
                "PYTHONDONTWRITEBYTECODE=1",
                "--env",
                "TMPDIR=/tmp",
            ]
        )
        for key, value in sorted(spec.environment.items()):
            command.extend(["--env", f"{key}={value}"])
        command.append(spec.image)
        command.extend(spec.command)
        return command

    def run(self, spec: SandboxSpec) -> SandboxResult:
        started = time.monotonic_ns()
        container_name = f"vpi-cvm-{uuid.uuid4().hex[:12]}"
        try:
            result = subprocess.run(
                self.build_command(spec, container_name=container_name),
                capture_output=True,
                text=True,
                timeout=spec.timeout_seconds,
                check=False,
            )
            duration_ms = (time.monotonic_ns() - started) // 1_000_000
            return SandboxResult(
                exit_code=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr,
                timed_out=False,
                duration_ms=duration_ms,
            )
        except subprocess.TimeoutExpired as exc:
            subprocess.run(
                ["docker", "kill", container_name],
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            subprocess.run(
                ["docker", "rm", "-f", container_name],
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            duration_ms = (time.monotonic_ns() - started) // 1_000_000
            stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            return SandboxResult(
                exit_code=None,
                stdout=stdout,
                stderr=stderr,
                timed_out=True,
                duration_ms=duration_ms,
            )
