# 15 Status and Queue Endpoints

## Objective
Expose status and queue inspection endpoints for vscode-onedrive-sync-router so the VS Code extension can display local agent state.

## Files to Create or Modify
- `agent/app/main.py`
- `agent/app/queue_service.py`
- `agent/app/models.py`
- `agent/tests/test_api.py`

## Requirements
- Add endpoints for queue counts, item listing, item detail, and worker status.
- Include enough status information for the extension to show healthy, busy, warning, and error states.
- Keep responses compact and local-first.

## Constraints
- Do not expose secret material in status endpoints.
- Do not rely on cloud telemetry.
- Do not turn status checks into a write path.

## Acceptance Criteria
- The extension can query useful local status.
- Queue endpoints return consistent summaries.
- The API remains safe to call repeatedly.

## Test Expectations
- Add tests for the status summary endpoint.
- Add tests for queue listing and empty-state behavior.