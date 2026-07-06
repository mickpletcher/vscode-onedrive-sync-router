from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class EventType(StrEnum):
    create = "create"
    modify = "modify"
    delete = "delete"
    rename = "rename"
    unknown = "unknown"


class QueueStatus(StrEnum):
    pending = "pending"
    processing = "processing"
    deferred = "deferred"
    completed = "completed"
    failed = "failed"


@dataclass(slots=True)
class FileEvent:
    workspace_root: str
    file_path: str
    event_type: str
    timestamp: str
    revision: str | None = None
    size: int | None = None
    mtime_ns: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class QueueItem:
    id: int
    workspace_root: str
    file_path: str
    event_type: str
    status: str
    dedupe_key: str
    payload: dict[str, Any]
    created_at: str
    updated_at: str
    attempts: int = 0
    available_at: str | None = None
    last_error: str | None = None


@dataclass(slots=True)
class RuleDecision:
    should_queue: bool
    action: str
    priority: int
    reason: str


@dataclass(slots=True)
class ProviderResult:
    ok: bool
    message: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ConflictSignal:
    detected: bool
    reason: str
