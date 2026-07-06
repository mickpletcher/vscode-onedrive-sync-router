from __future__ import annotations

from app.conflict_detection import detect_conflict_from_history
from app.file_stability import FileStabilityTracker


def test_file_stability_requires_observation(tmp_path):
    tracker = FileStabilityTracker(stable_delay_seconds=0)
    file_path = tmp_path / "docs" / "note.md"

    assert tracker.is_stable(file_path, size=1, mtime_ns=10) is False
    assert tracker.is_stable(file_path, size=1, mtime_ns=10) is True


def test_conflict_detection_flags_high_churn():
    signal = detect_conflict_from_history(change_count=6, unstable=True, recent_rewrites=3)
    assert signal.detected is True
