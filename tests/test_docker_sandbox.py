from pathlib import Path

from vpi_cvm.sandbox import DockerSandbox, SandboxSpec


def test_docker_command_has_mandatory_isolation_controls(tmp_path: Path):
    spec = SandboxSpec(
        workspace=tmp_path,
        image="python:3.13-slim",
        command=["pytest", "-q"],
    )
    cmd = DockerSandbox().build_command(spec)
    joined = " ".join(cmd)
    assert "--network none" in joined
    assert "--read-only" in cmd
    assert "--cap-drop ALL" in joined
    assert "--security-opt no-new-privileges" in joined
    assert "--pids-limit" in cmd
    assert "--memory" in cmd
    assert "--cpus" in cmd
    assert "--rm" in cmd
    assert str(tmp_path.resolve()) in joined


def test_docker_command_never_uses_privileged(tmp_path: Path):
    spec = SandboxSpec(
        workspace=tmp_path,
        image="python:3.13-slim",
        command=["python", "x.py"],
    )
    cmd = DockerSandbox().build_command(spec)
    assert "--privileged" not in cmd


def test_workspace_is_mounted_read_only(tmp_path: Path):
    spec = SandboxSpec(
        workspace=tmp_path,
        image="python:3.13-slim",
        command=["python", "x.py"],
    )
    cmd = DockerSandbox().build_command(spec, container_name="vpi-test")
    mount = cmd[cmd.index("--mount") + 1]
    assert mount.endswith(",ro")


def test_timeout_kills_and_removes_container(tmp_path: Path, monkeypatch):
    import subprocess

    import vpi_cvm.sandbox as sandbox_module

    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        if len(calls) == 1:
            raise subprocess.TimeoutExpired(
                cmd=cmd,
                timeout=1,
                output="",
                stderr="hung",
            )
        return subprocess.CompletedProcess(cmd, 0, "", "")

    monkeypatch.setattr(sandbox_module.subprocess, "run", fake_run)
    spec = SandboxSpec(
        workspace=tmp_path,
        image="python:3.13-slim",
        command=["python", "x.py"],
        timeout_seconds=1,
    )
    result = DockerSandbox().run(spec)

    name = calls[0][calls[0].index("--name") + 1]
    assert calls[1] == ["docker", "kill", name]
    assert calls[2] == ["docker", "rm", "-f", name]
    assert result.timed_out is True
