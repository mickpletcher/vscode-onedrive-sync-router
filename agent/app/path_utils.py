from __future__ import annotations

from pathlib import Path


def normalize_path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def resolve_workspace_root(value: str | Path) -> Path:
    return normalize_path(str(value))


def ensure_within_root(workspace_root: str | Path, candidate_path: str | Path) -> Path:
    root = resolve_workspace_root(workspace_root)
    candidate = normalize_path(str(candidate_path))
    if root == candidate or root in candidate.parents:
        return candidate
    raise ValueError("Path is outside the approved workspace root")
