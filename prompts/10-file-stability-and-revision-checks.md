# 10 File Stability and Revision Checks

## Objective

Implement file stability checks for vscode-onedrive-sync-router so queued items are only processed after the file state is stable enough for safe classification.

## Files to Create or Modify

- `agent/app/file_stability.py`
- `agent/app/conflict_detection.py`
- `agent/tests/test_file_stability.py`

## Requirements

- Confirm that a file has stopped changing before processing when possible.
- Track revision or timestamp observations in a local-safe way.
- Surface unstable files as deferred rather than completed.

## Constraints

- Do not touch native OneDrive sync controls.
- Do not require filesystem watchers that need privileged drivers.
- Do not depend on cloud revision APIs for the MVP.

## Acceptance Criteria

- Stability checks can distinguish stable from still-changing files.
- The worker can defer unstable items without losing queue state.
- Conflict-related observations are available for later reporting.

## Test Expectations

- Add tests for stable and unstable file transitions.
- Add tests for revision or timestamp comparisons.
