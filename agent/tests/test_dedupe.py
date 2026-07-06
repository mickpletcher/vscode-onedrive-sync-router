from __future__ import annotations

from app.database import open_database
from app.models import FileEvent, RuleDecision
from app.queue_service import QueueService


def make_event(tmp_path):
    return FileEvent(
        workspace_root=str(tmp_path),
        file_path=str(tmp_path / "docs" / "note.md"),
        event_type="modify",
        timestamp="2026-06-20T12:00:00Z",
    )


def test_enqueue_deduplicates_identical_events(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    event = make_event(tmp_path)
    decision = RuleDecision(True, "queue-process", 50, "default")

    first = queue.enqueue(event, decision)
    second = queue.enqueue(event, decision)

    assert first.id == second.id
    assert len(queue.list_items()) == 1