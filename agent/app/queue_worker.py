from __future__ import annotations

from .file_stability import FileStabilityTracker
from .models import ProviderResult
from .provider import Provider
from .queue_service import QueueService


class QueueWorker:
    def __init__(self, queue_service: QueueService, provider: Provider, stability_tracker: FileStabilityTracker) -> None:
        self.queue_service = queue_service
        self.provider = provider
        self.stability_tracker = stability_tracker

    def run_once(self) -> ProviderResult | None:
        item = self.queue_service.claim_next_item()
        if item is None:
            return None

        payload = item.payload.get("event", {})
        file_path = payload.get("file_path", item.file_path)
        size = payload.get("size")
        mtime_ns = payload.get("mtime_ns")

        if not self.stability_tracker.is_stable(file_path, size=size, mtime_ns=mtime_ns):
            self.queue_service.mark_deferred(item.id, 2, "file is still changing")
            return ProviderResult(ok=False, message="deferred until stable")

        result = self.provider.process(item)
        if result.ok:
            self.queue_service.mark_completed(item.id)
        else:
            self.queue_service.mark_failed(item.id, result.message)
        return result
