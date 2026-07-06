from __future__ import annotations

from fastapi.testclient import TestClient

from app.config import AppConfig
from app.main import create_app


def make_client(tmp_path):
    config = AppConfig(database_path=tmp_path / "sync-router.sqlite3")
    app = create_app(config)
    return TestClient(app)


def test_health_endpoint(tmp_path):
    client = make_client(tmp_path)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint_reports_project_name(tmp_path):
    client = make_client(tmp_path)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "vscode-onedrive-sync-router"


def test_post_event_queues_file_activity(tmp_path):
    client = make_client(tmp_path)
    response = client.post(
        "/events",
        json={
            "workspaceRoot": str(tmp_path),
            "filePath": str(tmp_path / "docs" / "note.md"),
            "eventType": "modify",
            "timestamp": "2026-06-20T12:00:00Z",
            "size": 12,
            "mtimeNs": 123,
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["accepted"] is True
    assert payload["queued"] is True


def test_queue_status_endpoint(tmp_path):
    client = make_client(tmp_path)
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()["service"] == "vscode-onedrive-sync-router"