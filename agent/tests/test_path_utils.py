from __future__ import annotations

import pytest

from app.path_utils import ensure_within_root, resolve_workspace_root


def test_resolve_workspace_root(tmp_path):
    resolved = resolve_workspace_root(tmp_path)
    assert resolved == tmp_path.resolve()


def test_ensure_within_root_accepts_child_path(tmp_path):
    child = tmp_path / "docs" / "note.md"
    assert ensure_within_root(tmp_path, child) == child.resolve()


def test_ensure_within_root_rejects_escape(tmp_path):
    outside = tmp_path.parent / "outside.txt"
    with pytest.raises(ValueError):
        ensure_within_root(tmp_path, outside)