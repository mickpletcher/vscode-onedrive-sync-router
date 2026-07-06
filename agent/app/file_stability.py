from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(slots=True)
class FileObservation:
    path: Path
    size: int | None
    mtime_ns: int | None
    observed_at: datetime


class FileStabilityTracker:
    def __init__(self, stable_delay_seconds: int = 2) -> None:
        self.stable_delay_seconds = stable_delay_seconds
        self._observations: dict[str, FileObservation] = {}

    def observe(self, path: str | Path, size: int | None = None, mtime_ns: int | None = None) -> FileObservation:
        normalized = Path(path).expanduser().resolve()
        observation = FileObservation(
            path=normalized,
            size=size,
            mtime_ns=mtime_ns,
            observed_at=datetime.now(timezone.utc),
        )
        self._observations[str(normalized)] = observation
        return observation

    def is_stable(self, path: str | Path, size: int | None = None, mtime_ns: int | None = None) -> bool:
        normalized = Path(path).expanduser().resolve()
        key = str(normalized)
        previous = self._observations.get(key)
        current = self.observe(normalized, size=size, mtime_ns=mtime_ns)
        if previous is None:
            return False
        if previous.size != current.size or previous.mtime_ns != current.mtime_ns:
            return False
        elapsed = (current.observed_at - previous.observed_at).total_seconds()
        return elapsed >= self.stable_delay_seconds
