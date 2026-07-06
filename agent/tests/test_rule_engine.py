from __future__ import annotations

from app.models import FileEvent
from app.rule_engine import classify_event


def test_rule_engine_queues_source_files(tmp_path):
    event = FileEvent(
        workspace_root=str(tmp_path),
        file_path=str(tmp_path / "docs" / "note.md"),
        event_type="modify",
        timestamp="2026-06-20T12:00:00Z",
    )

    decision = classify_event(event)

    assert decision.should_queue is True
    assert decision.action == "queue-process"


def test_rule_engine_ignores_infrastructure_paths(tmp_path):
    event = FileEvent(
        workspace_root=str(tmp_path),
        file_path=str(tmp_path / "node_modules" / "pkg" / "index.js"),
        event_type="modify",
        timestamp="2026-06-20T12:00:00Z",
    )

    decision = classify_event(event)

    assert decision.should_queue is False
    assert decision.action == "ignore"