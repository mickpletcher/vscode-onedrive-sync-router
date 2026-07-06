from __future__ import annotations

from app.models import FileEvent
from app.rule_engine import classify_event


def make_event(tmp_path, file_name: str, event_type: str) -> FileEvent:
    return FileEvent(
        workspace_root=str(tmp_path),
        file_path=str(tmp_path / file_name),
        event_type=event_type,
        timestamp="2026-06-20T12:00:00Z",
    )


def test_rule_engine_queues_source_files(tmp_path):
    event = make_event(tmp_path, "docs/note.md", "modify")

    decision = classify_event(event)

    assert decision.should_queue is True
    assert decision.action == "queue-process"


def test_rule_engine_ignores_infrastructure_paths(tmp_path):
    event = make_event(tmp_path, "node_modules/pkg/index.js", "modify")

    decision = classify_event(event)

    assert decision.should_queue is False
    assert decision.action == "ignore"


def test_rule_engine_queues_delete_with_high_priority(tmp_path):
    event = make_event(tmp_path, "docs/note.md", "delete")

    decision = classify_event(event)

    assert decision.should_queue is True
    assert decision.action == "queue-delete"
    assert decision.priority == 90


def test_rule_engine_create_uses_default_conservative_decision(tmp_path):
    event = make_event(tmp_path, "assets/blob.bin", "create")

    decision = classify_event(event)

    assert decision.should_queue is True
    assert decision.action == "queue-process"
    assert decision.priority == 50