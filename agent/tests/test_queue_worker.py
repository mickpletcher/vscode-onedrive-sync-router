from __future__ import annotations

from app.database import open_database
from app.file_stability import FileStabilityTracker
from app.models import FileEvent, ProviderResult, QueueStatus, RuleDecision
from app.queue_service import QueueService
from app.queue_worker import QueueWorker


class StubProvider:
    def __init__(self, ok: bool) -> None:
        self.ok = ok

    def process(self, item) -> ProviderResult:
        return ProviderResult(ok=self.ok, message="ok" if self.ok else "provider failure")


def make_event(tmp_path) -> FileEvent:
    return FileEvent(
        workspace_root=str(tmp_path),
        file_path=str(tmp_path / "docs" / "note.md"),
        event_type="modify",
        timestamp="2026-06-20T12:00:00Z",
        size=10,
        mtime_ns=123,
    )


def test_queue_worker_returns_none_when_queue_empty(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    worker = QueueWorker(queue, StubProvider(ok=True), FileStabilityTracker(stable_delay_seconds=0))

    assert worker.run_once() is None


def test_queue_worker_defers_unstable_item(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    event = make_event(tmp_path)
    decision = RuleDecision(True, "queue-process", 50, "default")
    queued = queue.enqueue(event, decision)

    worker = QueueWorker(queue, StubProvider(ok=True), FileStabilityTracker(stable_delay_seconds=0))
    result = worker.run_once()

    assert result is not None
    assert result.ok is False
    updated = queue.get_item(queued.id)
    assert updated.status == QueueStatus.deferred.value


def test_queue_worker_completes_stable_item(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    event = make_event(tmp_path)
    decision = RuleDecision(True, "queue-process", 50, "default")
    queued = queue.enqueue(event, decision)

    tracker = FileStabilityTracker(stable_delay_seconds=0)
    tracker.observe(event.file_path, size=event.size, mtime_ns=event.mtime_ns)
    worker = QueueWorker(queue, StubProvider(ok=True), tracker)
    result = worker.run_once()

    assert result is not None
    assert result.ok is True
    updated = queue.get_item(queued.id)
    assert updated.status == QueueStatus.completed.value


def test_queue_worker_marks_failed_when_provider_fails(tmp_path):
    connection = open_database(tmp_path / "sync-router.sqlite3")
    queue = QueueService(connection)
    event = make_event(tmp_path)
    decision = RuleDecision(True, "queue-process", 50, "default")
    queued = queue.enqueue(event, decision)

    tracker = FileStabilityTracker(stable_delay_seconds=0)
    tracker.observe(event.file_path, size=event.size, mtime_ns=event.mtime_ns)
    worker = QueueWorker(queue, StubProvider(ok=False), tracker)
    result = worker.run_once()

    assert result is not None
    assert result.ok is False
    updated = queue.get_item(queued.id)
    assert updated.status == QueueStatus.failed.value