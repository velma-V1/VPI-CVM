from __future__ import annotations

from pathlib import Path


class Workspace:
    """Filesystem root with canonical containment enforcement."""

    def __init__(self, root: str | Path):
        self.root = Path(root).expanduser().resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def resolve(self, relative_path: str | Path) -> Path:
        candidate = (self.root / relative_path).resolve()
        if candidate == self.root or not candidate.is_relative_to(self.root):
            raise ValueError(f"path escapes workspace: {relative_path}")
        return candidate

    def write_text(self, relative_path: str | Path, content: str) -> Path:
        target = self.resolve(relative_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target
