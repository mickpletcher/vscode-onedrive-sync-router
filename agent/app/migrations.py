from __future__ import annotations

SCHEMA_VERSION = 1

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queue_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workspace_root TEXT NOT NULL,
    file_path TEXT NOT NULL,
    event_type TEXT NOT NULL,
    status TEXT NOT NULL,
    dedupe_key TEXT NOT NULL UNIQUE,
    payload_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    available_at TEXT,
    attempts INTEGER NOT NULL DEFAULT 0,
    last_error TEXT
);

CREATE TABLE IF NOT EXISTS file_observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workspace_root TEXT NOT NULL,
    file_path TEXT NOT NULL,
    size INTEGER,
    mtime_ns INTEGER,
    observed_at TEXT NOT NULL
);
"""
