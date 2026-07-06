from __future__ import annotations

from pathlib import Path

from .models import FileEvent, RuleDecision

IGNORED_MARKERS = {".git", "node_modules", "dist", "out", "__pycache__"}
IGNORED_EXTENSIONS = {".log", ".tmp", ".swp"}


def classify_event(event: FileEvent) -> RuleDecision:
    candidate_path = Path(event.file_path)
    if any(marker in candidate_path.parts for marker in IGNORED_MARKERS):
        return RuleDecision(False, "ignore", 0, "ignored infrastructure path")

    if candidate_path.suffix.lower() in IGNORED_EXTENSIONS:
        return RuleDecision(False, "ignore", 0, "ignored file extension")

    if event.event_type == "delete":
        return RuleDecision(True, "queue-delete", 90, "delete events are queued for review")

    if event.event_type == "rename":
        return RuleDecision(True, "queue-rename", 80, "rename events are queued for review")

    if candidate_path.suffix.lower() in {".md", ".json", ".ts", ".py", ".yml", ".yaml"}:
        return RuleDecision(True, "queue-process", 70, "tracked source or configuration file")

    return RuleDecision(True, "queue-process", 50, "default local-first processing")
