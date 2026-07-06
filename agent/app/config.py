from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class AppConfig:
    host: str = "127.0.0.1"
    port: int = 8765
    database_path: Path = Path(".state/sync-router.sqlite3")
    workspace_root: Path | None = None
    provider_mode: str = "dry-run"
    shared_secret: str = ""
    stable_delay_seconds: int = 2
    dedupe_window_seconds: int = 15


def load_config(config_path: str | Path | None = None) -> AppConfig:
    raw: dict[str, object] = {}
    path_value = config_path or os.environ.get("SYNC_ROUTER_CONFIG")
    if path_value:
        path = Path(path_value)
        if path.exists():
            raw.update(json.loads(path.read_text(encoding="utf-8")))

    host = os.environ.get("SYNC_ROUTER_HOST", str(raw.get("host", "127.0.0.1")))
    port = int(os.environ.get("SYNC_ROUTER_PORT", raw.get("port", 8765)))
    database_path = Path(os.environ.get("SYNC_ROUTER_DATABASE_PATH", str(raw.get("database_path", ".state/sync-router.sqlite3"))))
    workspace_root_raw = os.environ.get("SYNC_ROUTER_WORKSPACE_ROOT", raw.get("workspace_root"))
    workspace_root = Path(workspace_root_raw) if workspace_root_raw else None
    provider_mode = os.environ.get("SYNC_ROUTER_PROVIDER_MODE", str(raw.get("provider_mode", "dry-run")))
    shared_secret = os.environ.get("SYNC_ROUTER_SHARED_SECRET", str(raw.get("shared_secret", "")))
    stable_delay_seconds = int(os.environ.get("SYNC_ROUTER_STABLE_DELAY_SECONDS", raw.get("stable_delay_seconds", 2)))
    dedupe_window_seconds = int(os.environ.get("SYNC_ROUTER_DEDUPE_WINDOW_SECONDS", raw.get("dedupe_window_seconds", 15)))

    return AppConfig(
        host=host,
        port=port,
        database_path=database_path,
        workspace_root=workspace_root,
        provider_mode=provider_mode,
        shared_secret=shared_secret,
        stable_delay_seconds=stable_delay_seconds,
        dedupe_window_seconds=dedupe_window_seconds,
    )
