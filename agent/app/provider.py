from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from .models import ProviderResult, QueueItem


class Provider(Protocol):
    def process(self, item: QueueItem) -> ProviderResult:
        ...


@dataclass(slots=True)
class ProviderRegistry:
    provider_mode: str = "dry-run"
    history: list[ProviderResult] = field(default_factory=list)

    def create(self) -> Provider:
        from .dry_run_provider import DryRunProvider

        return DryRunProvider(history=self.history)

