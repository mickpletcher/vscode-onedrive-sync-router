from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timedelta, timezone
from dataclasses import asdict
from typing import Iterable

from .models import FileEvent, QueueItem, QueueStatus, RuleDecision


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _to_queue_item(row: sqlite3.Row) -> QueueItem:
    return QueueItem(
        id=row["id"],
        workspace_root=row["workspace_root"],
        file_path=row["file_path"],
        event_type=row["event_type"],
        status=row["status"],
        dedupe_key=row["dedupe_key"],
        payload=json.loads(row["payload_json"]),
        created_at=row["created_at"],
        updated_at=row["updated_at"],
        attempts=row["attempts"],
        available_at=row["available_at"],
        last_error=row["last_error"],
    )


class QueueService:
    def __init__(self, connection: sqlite3.Connection, dedupe_window_seconds: int = 15) -> None:
        self.connection = connection
        self.dedupe_window_seconds = dedupe_window_seconds

    def build_dedupe_key(self, event: FileEvent, decision: RuleDecision) -> str:
        return "|".join((event.workspace_root, event.file_path, event.event_type, decision.action))

    def enqueue(self, event: FileEvent, decision: RuleDecision) -> QueueItem:
        dedupe_key = self.build_dedupe_key(event, decision)
        existing = self.get_by_dedupe_key(dedupe_key)
        payload = json.dumps({"event": asdict(event), "decision": asdict(decision)}, sort_keys=True)
        timestamp = _now()
        if existing:
            self.connection.execute(
                """
                UPDATE queue_items
                SET payload_json = ?, status = ?, updated_at = ?, available_at = NULL, last_error = NULL
                WHERE id = ?
                """,
                (payload, QueueStatus.pending.value, timestamp, existing.id),
            )
            self.connection.commit()
            return self.get_item(existing.id)

        cursor = self.connection.execute(
            """
            INSERT INTO queue_items (
                workspace_root, file_path, event_type, status, dedupe_key,
                payload_json, created_at, updated_at, available_at, attempts, last_error
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, 0, NULL)
            """,
            (
                event.workspace_root,
                event.file_path,
                event.event_type,
                QueueStatus.pending.value,
                dedupe_key,
                payload,
                timestamp,
                timestamp,
            ),
        )
        self.connection.commit()
        return self.get_item(cursor.lastrowid)

    def list_items(self, limit: int = 50) -> list[QueueItem]:
        rows = self.connection.execute(
            "SELECT * FROM queue_items ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [_to_queue_item(row) for row in rows]

    def get_item(self, item_id: int) -> QueueItem:
        row = self.connection.execute("SELECT * FROM queue_items WHERE id = ?", (item_id,)).fetchone()
        if row is None:
            raise KeyError(f"Queue item {item_id} not found")
        return _to_queue_item(row)

    def get_by_dedupe_key(self, dedupe_key: str) -> QueueItem | None:
        row = self.connection.execute("SELECT * FROM queue_items WHERE dedupe_key = ?", (dedupe_key,)).fetchone()
        return _to_queue_item(row) if row else None

    def claim_next_item(self) -> QueueItem | None:
        row = self.connection.execute(
            """
            SELECT * FROM queue_items
            WHERE status IN (?, ?)
              AND (available_at IS NULL OR available_at <= ?)
            ORDER BY id ASC
            LIMIT 1
            """,
            (QueueStatus.pending.value, QueueStatus.deferred.value, _now()),
        ).fetchone()
        if row is None:
            return None
        self.connection.execute(
            "UPDATE queue_items SET status = ?, attempts = attempts + 1, updated_at = ? WHERE id = ?",
            (QueueStatus.processing.value, _now(), row["id"]),
        )
        self.connection.commit()
        return self.get_item(row["id"])

    def mark_completed(self, item_id: int) -> QueueItem:
        self.connection.execute(
            "UPDATE queue_items SET status = ?, updated_at = ?, available_at = NULL, last_error = NULL WHERE id = ?",
            (QueueStatus.completed.value, _now(), item_id),
        )
        self.connection.commit()
        return self.get_item(item_id)

    def mark_failed(self, item_id: int, error_message: str) -> QueueItem:
        self.connection.execute(
            "UPDATE queue_items SET status = ?, updated_at = ?, last_error = ? WHERE id = ?",
            (QueueStatus.failed.value, _now(), error_message, item_id),
        )
        self.connection.commit()
        return self.get_item(item_id)

    def mark_deferred(self, item_id: int, delay_seconds: int, reason: str) -> QueueItem:
        available_at = (datetime.now(timezone.utc) + timedelta(seconds=delay_seconds)).isoformat()
        self.connection.execute(
            "UPDATE queue_items SET status = ?, updated_at = ?, available_at = ?, last_error = ? WHERE id = ?",
            (QueueStatus.deferred.value, _now(), available_at, reason, item_id),
        )
        self.connection.commit()
        return self.get_item(item_id)

    def counts_by_status(self) -> dict[str, int]:
        rows = self.connection.execute(
            "SELECT status, COUNT(*) AS count FROM queue_items GROUP BY status",
        ).fetchall()
        return {row["status"]: row["count"] for row in rows}


def queue_items_from_iterable(items: Iterable[QueueItem]) -> list[dict[str, object]]:
    return [
        {
            "id": item.id,
            "workspace_root": item.workspace_root,
            "file_path": item.file_path,
            "event_type": item.event_type,
            "status": item.status,
            "dedupe_key": item.dedupe_key,
            "payload": item.payload,
            "created_at": item.created_at,
            "updated_at": item.updated_at,
            "attempts": item.attempts,
            "available_at": item.available_at,
            "last_error": item.last_error,
        }
        for item in items
    ]
