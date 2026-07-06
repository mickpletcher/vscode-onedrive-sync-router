# 04 Path Security and Root Resolution

## Objective
Implement safe path handling for vscode-onedrive-sync-router so the agent can resolve workspace roots and reject path traversal or unsafe file targets.

## Files to Create or Modify
- `agent/app/path_utils.py`
- `agent/app/security.py`
- `agent/tests/test_path_utils.py`
- `agent/tests/test_security.py`

## Requirements
- Canonicalize incoming file paths before any queue or rule processing.
- Resolve workspace roots explicitly and reject paths outside approved roots.
- Normalize path separators consistently across platforms.

## Constraints
- Do not trust client-supplied paths without validation.
- Do not expose sensitive absolute paths unnecessarily.
- Do not treat path validation as a substitute for provider authorization.

## Acceptance Criteria
- Unsafe paths are rejected before queue insertion.
- Canonical workspace-root resolution is deterministic.
- Path helpers are usable from the API, queue, and rule engine layers.

## Test Expectations
- Add tests for path normalization.
- Add tests for rejecting traversal and out-of-root access.