from __future__ import annotations

from app.config import load_config


def test_load_config_uses_safe_defaults(tmp_path, monkeypatch):
    monkeypatch.delenv("SYNC_ROUTER_CONFIG", raising=False)
    monkeypatch.delenv("SYNC_ROUTER_HOST", raising=False)
    monkeypatch.delenv("SYNC_ROUTER_PORT", raising=False)

    config = load_config(tmp_path / "missing.json")

    assert config.host == "127.0.0.1"
    assert config.port == 8765
    assert config.provider_mode == "dry-run"