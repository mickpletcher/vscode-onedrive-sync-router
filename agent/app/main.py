from __future__ import annotations

from pathlib import Path
from dataclasses import asdict

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field

from .config import AppConfig, load_config
from .database import open_database
from .logging_config import configure_logging
from .models import FileEvent
from .path_utils import ensure_within_root
from .provider import ProviderRegistry
from .queue_service import QueueService, queue_items_from_iterable
from .rule_engine import classify_event
from .security import require_authorized_request


class FileEventPayload(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    workspace_root: str = Field(alias="workspaceRoot")
    file_path: str = Field(alias="filePath")
    event_type: str = Field(alias="eventType")
    timestamp: str = Field(alias="timestamp")
    revision: str | None = Field(default=None, alias="revision")
    size: int | None = Field(default=None, alias="size")
    mtime_ns: int | None = Field(default=None, alias="mtimeNs")
    metadata: dict[str, object] = Field(default_factory=dict, alias="metadata")


def create_app(config: AppConfig | None = None) -> FastAPI:
    configure_logging()
    config = config or load_config()
    connection = open_database(config.database_path)
    queue_service = QueueService(connection, dedupe_window_seconds=config.dedupe_window_seconds)
    provider = ProviderRegistry(provider_mode=config.provider_mode).create()

    app = FastAPI(title="vscode-onedrive-sync-router")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://127.0.0.1", "http://localhost"],
        allow_credentials=False,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    app.state.config = config
    app.state.connection = connection
    app.state.queue_service = queue_service
    app.state.provider = provider

    def get_queue_service() -> QueueService:
        return app.state.queue_service

    def get_config() -> AppConfig:
        return app.state.config

    @app.get("/")
    def root() -> dict[str, object]:
        return {
            "name": "vscode-onedrive-sync-router",
            "status": "ok",
            "mode": config.provider_mode,
        }

    @app.get("/health")
    def health() -> dict[str, object]:
        return {"status": "healthy", "database": str(config.database_path), "provider": config.provider_mode}

    @app.post("/events")
    def post_event(payload: FileEventPayload, request: Request, queue: QueueService = Depends(get_queue_service), app_config: AppConfig = Depends(get_config)) -> JSONResponse:
        require_authorized_request(request, app_config.shared_secret)
        try:
            candidate_path = ensure_within_root(payload.workspace_root, payload.file_path)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        event = FileEvent(
            workspace_root=str(Path(payload.workspace_root).expanduser().resolve()),
            file_path=str(candidate_path),
            event_type=payload.event_type,
            timestamp=payload.timestamp,
            revision=payload.revision,
            size=payload.size,
            mtime_ns=payload.mtime_ns,
            metadata=payload.metadata,
        )
        decision = classify_event(event)
        if not decision.should_queue:
            return JSONResponse({"accepted": True, "queued": False, "decision": asdict(decision)})
        item = queue.enqueue(event, decision)
        return JSONResponse({"accepted": True, "queued": True, "queue_item": asdict(item), "decision": asdict(decision)})

    @app.get("/status")
    def status(queue: QueueService = Depends(get_queue_service)) -> dict[str, object]:
        return {"service": "vscode-onedrive-sync-router", "queue": queue.counts_by_status(), "mode": config.provider_mode}

    @app.get("/queue")
    def queue_items(queue: QueueService = Depends(get_queue_service)) -> dict[str, object]:
        items = queue.list_items()
        return {"items": queue_items_from_iterable(items), "count": len(items)}

    @app.get("/queue/{item_id}")
    def queue_item(item_id: int, queue: QueueService = Depends(get_queue_service)) -> dict[str, object]:
        try:
            item = queue.get_item(item_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return asdict(item)

    return app


app = create_app()


def run() -> None:
    import uvicorn

    config = load_config()
    uvicorn.run("app.main:create_app", factory=True, host=config.host, port=config.port, reload=False)
