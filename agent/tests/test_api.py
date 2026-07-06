from __future__ import annotations

from fastapi.testclient import TestClient

from app.config import AppConfig
from app.main import create_app


def make_client(tmp_path):
    config = AppConfig(database_path=tmp_path / "sync-router.sqlite3", enable_worker=False)
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


def test_queue_list_and_detail_endpoints(tmp_path):
    client = make_client(tmp_path)
    queued = client.post(
        "/events",
        json={
            "workspaceRoot": str(tmp_path),
            "filePath": str(tmp_path / "docs" / "note.md"),
            "eventType": "modify",
            "timestamp": "2026-06-20T12:00:00Z",
        },
    )
    assert queued.status_code == 200
    queue_item_id = queued.json()["queue_item"]["id"]

    list_response = client.get("/queue")
    assert list_response.status_code == 200
    list_payload = list_response.json()
    assert list_payload["count"] == 1
    assert list_payload["items"][0]["id"] == queue_item_id

    detail_response = client.get(f"/queue/{queue_item_id}")
    assert detail_response.status_code == 200
    assert detail_response.json()["id"] == queue_item_id


def test_queue_detail_404_for_missing_item(tmp_path):
    client = make_client(tmp_path)
    response = client.get("/queue/9999")
    assert response.status_code == 404