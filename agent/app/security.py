from __future__ import annotations

from fastapi import HTTPException, Request, status

LOCAL_HOSTS = {"127.0.0.1", "::1", "localhost", "testclient"}
TOKEN_HEADER = "X-Sync-Router-Token"


def is_local_request(request: Request) -> bool:
    client = request.client.host if request.client else None
    return client in LOCAL_HOSTS


def require_authorized_request(request: Request, shared_secret: str | None) -> None:
    if not is_local_request(request):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Local access only")

    if shared_secret:
        token = request.headers.get(TOKEN_HEADER)
        if token != shared_secret:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token")
