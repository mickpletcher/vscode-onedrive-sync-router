# 05 Rule Engine

## Objective

Implement the rule engine for vscode-onedrive-sync-router so file events can be classified for queueing, deduping, priority, and dry-run handling.

## Files to Create or Modify

- `agent/app/rule_engine.py`
- `agent/app/models.py`
- `agent/tests/test_rule_engine.py`

## Requirements

- Classify events by file type, path patterns, workspace context, and change type.
- Produce a deterministic action or routing decision for each event.
- Keep the default behavior conservative and local-first.

## Constraints

- Do not call any cloud provider from the rule engine.
- Do not add OneDrive-specific write orchestration.
- Do not rely on undocumented heuristics that cannot be tested.

## Acceptance Criteria

- The rule engine returns stable classifications for representative file events.
- Decisions are explicit enough to feed queue and provider layers.
- The logic is isolated and unit-testable.

## Test Expectations

- Add unit tests for at least create, modify, delete, and ignored-event paths.
- Add a test for a conservative default decision.
