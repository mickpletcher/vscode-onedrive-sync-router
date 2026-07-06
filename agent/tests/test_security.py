from __future__ import annotations

from fastapi import HTTPException
from starlette.requests import Request

from app.security import is_local_request, require_authorized_request


def make_request(client_host: str = "127.0.0.1", headers: dict[str, str] | None = None) -> Request:
    raw_headers = []
    for key, value in (headers or {}).items():
        raw_headers.append((key.lower().encode("utf-8"), value.encode("utf-8")))
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/",
        "headers": raw_headers,
        "client": (client_host, 1234),
        "scheme": "http",
        "server": ("127.0.0.1", 8765),
    }
    return Request(scope)


def test_local_request_is_allowed_without_secret():
    request = make_request()
    assert is_local_request(request) is True
    require_authorized_request(request, "")


def test_shared_secret_is_enforced():
    request = make_request(headers={"X-Sync-Router-Token": "expected"})
    require_authorized_request(request, "expected")


def test_non_local_request_is_rejected():
    request = make_request(client_host="10.0.0.2")
    try:
        require_authorized_request(request, "")
    except HTTPException as exc:
        assert exc.status_code == 403
    else:
        raise AssertionError("Expected local-only rejection")


def test_testclient_host_rejected_outside_pytest_context(monkeypatch):
    monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)
    request = make_request(client_host="testclient")
    try:
        require_authorized_request(request, "")
    except HTTPException as exc:
        assert exc.status_code == 403
    else:
        raise AssertionError("Expected local-only rejection")