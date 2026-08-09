from pathlib import Path

import pytest

from vpi_cvm.workspace import Workspace


def test_resolve_preserves_nested_path(tmp_path: Path):
    ws = Workspace(tmp_path)
    target = ws.resolve("src/infrastructure/db/provider.py")
    assert target == tmp_path / "src" / "infrastructure" / "db" / "provider.py"


def test_resolve_rejects_parent_traversal(tmp_path: Path):
    ws = Workspace(tmp_path)
    with pytest.raises(ValueError):
        ws.resolve("../escape.py")


def test_resolve_rejects_sibling_prefix_escape(tmp_path: Path):
    ws = Workspace(tmp_path / "jail")
    with pytest.raises(ValueError):
        ws.resolve("../jail_evil/payload.py")
