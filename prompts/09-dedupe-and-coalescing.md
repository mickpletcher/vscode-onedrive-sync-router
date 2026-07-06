# 09 Dedupe and Coalescing

## Objective

Add dedupe and coalescing behavior to vscode-onedrive-sync-router so repeated file events collapse into a smaller, more stable queue.

## Files to Create or Modify

- `agent/app/queue_service.py`
- `agent/app/rule_engine.py`
- `agent/tests/test_dedupe.py`
- `agent/tests/test_queue_service.py`

## Requirements

- Detect repeated events for the same file and workspace within a short window.
- Merge redundant updates when the change sequence is clearly superseded.
- Preserve the latest meaningful state for downstream processing.

## Constraints

- Do not drop events without a deterministic rule.
- Do not coalesce across unrelated files or workspaces.
- Do not introduce timing behavior that depends on cloud latency.

## Acceptance Criteria

- Duplicate events collapse predictably.
- The resulting queue is smaller but still accurate for local processing.
- Dedupe behavior is documented through tests.

## Test Expectations

- Add tests for repeated modify events.
- Add tests that separate files are not coalesced together.
