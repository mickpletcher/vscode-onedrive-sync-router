from __future__ import annotations

from dataclasses import dataclass

from .models import ConflictSignal


def detect_conflict_from_history(change_count: int, unstable: bool, recent_rewrites: int) -> ConflictSignal:
    if unstable and recent_rewrites >= 2:
        return ConflictSignal(True, "file is still changing after repeated rewrites")
    if change_count >= 5 and recent_rewrites >= 3:
        return ConflictSignal(True, "high churn indicates possible conflict")
    return ConflictSignal(False, "no clear local conflict signal")
