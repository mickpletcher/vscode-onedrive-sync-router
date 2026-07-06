# 08 File Events API

## Objective
Expose the backend API that receives VS Code file activity for vscode-onedrive-sync-router and routes it into the rule and queue layers.

## Files to Create or Modify
- `agent/app/main.py`
- `agent/app/rule_engine.py`
- `agent/app/queue_service.py`
- `agent/tests/test_api.py`

## Requirements
- Add an endpoint for posting file events from the VS Code extension.
- Validate the payload before it reaches persistence.
- Return a clear local processing response for accepted events.

## Constraints
- Do not expose a remote public API.
- Do not claim the endpoint controls native OneDrive sync.
- Do not perform real cloud writes from this endpoint.

## Acceptance Criteria
- The extension can send file events to the agent locally.
- Invalid payloads are rejected with useful errors.
- Accepted events are handed off to the rule and queue flow.

## Test Expectations
- Add API tests for accepted and rejected event payloads.
- Add a test for a minimal local file event submission path.