from __future__ import annotations

from dataclasses import dataclass, field

from .models import ProviderResult, QueueItem


@dataclass(slots=True)
class DryRunProvider:
    history: list[ProviderResult] = field(default_factory=list)

    def process(self, item: QueueItem) -> ProviderResult:
        result = ProviderResult(
            ok=True,
            message="dry-run complete",
            details={
                "queue_item_id": item.id,
                "file_path": item.file_path,
                "event_type": item.event_type,
            },
        )
        self.history.append(result)
        return result
