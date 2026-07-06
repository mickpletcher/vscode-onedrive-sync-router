# 07 Queue Service

## Objective
Implement the local queue service for vscode-onedrive-sync-router so validated file events can be stored, updated, listed, and processed safely.

## Files to Create or Modify
- `agent/app/queue_service.py`
- `agent/app/models.py`
- `agent/app/database.py`
- `agent/tests/test_queue_service.py`

## Requirements
- Support enqueue, update, claim, complete, and fail operations.
- Preserve enough metadata for later dedupe, conflict detection, and status reporting.
- Keep queue operations transactionally safe for a single local agent.

## Constraints
- Do not perform provider writes in the queue service.
- Do not assume concurrent distributed workers.
- Do not allow malformed records to enter the queue.

## Acceptance Criteria
- Queue operations behave predictably against SQLite.
- Records can be listed with their current state.
- The service is ready for dedupe and worker integration.

## Test Expectations
- Add tests for enqueue and retrieval.
- Add tests for status transitions and failure handling.