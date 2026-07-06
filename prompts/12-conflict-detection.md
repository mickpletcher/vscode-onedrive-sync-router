# 12 Conflict Detection

## Objective

Add local conflict detection logic for vscode-onedrive-sync-router so queued items can be marked when file state suggests a likely sync conflict or manual review case.

## Files to Create or Modify

- `agent/app/conflict_detection.py`
- `agent/app/file_stability.py`
- `agent/tests/test_file_stability.py`
- `agent/tests/test_api.py`

## Requirements

- Detect obvious local conflict signals such as unstable revisions, repeated churn, or suspicious timing patterns.
- Return a clear status that the worker and API can surface.
- Keep the detection logic conservative and explainable.

## Constraints

- Do not claim this can prevent OneDrive from syncing.
- Do not attempt remote conflict resolution in the MVP.
- Do not make conflict detection depend on cloud writes.

## Acceptance Criteria

- Likely conflict cases are flagged locally.
- Non-conflict cases are not over-marked.
- The logic can be reused by status endpoints later.

## Test Expectations

- Add tests for conflict-like and non-conflict-like file histories.
- Add tests that the output is stable for identical inputs.
