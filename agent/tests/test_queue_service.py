from __future__ import annotations

from app.database import open_database
from app.models import FileEvent, QueueStatus, RuleDecision
from app.queue_service import QueueService


def make_event(tmp_path):
    return FileEvent(
        workspace_root=str(tmp_path),
        file_path=str(tmp_path / "docs" / "note.md"),
        event_type="modify",
        timestamp="2026-06-20T12:00:00Z",
    )


def test_queue_service_enqueue_and_list(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    event = make_event(tmp_path)
    decision = RuleDecision(True, "queue-process", 50, "default")

    item = queue.enqueue(event, decision)

    assert item.status == QueueStatus.pending.value
    assert len(queue.list_items()) == 1
    assert queue.counts_by_status()[QueueStatus.pending.value] == 1


def test_queue_service_claim_complete_and_fail(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    event = make_event(tmp_path)
    decision = RuleDecision(True, "queue-process", 50, "default")

    queue.enqueue(event, decision)
    claimed = queue.claim_next_item()
    assert claimed is not None
    assert claimed.status == QueueStatus.processing.value

    completed = queue.mark_completed(claimed.id)
    assert completed.status == QueueStatus.completed.value

    queued_again = queue.enqueue(event, decision)
    failed = queue.mark_failed(queued_again.id, "example failure")
    assert failed.status == QueueStatus.failed.value