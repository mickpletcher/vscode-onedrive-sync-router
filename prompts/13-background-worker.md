# 13 Background Worker

## Objective

Implement the background worker for vscode-onedrive-sync-router so queued items can be claimed, stabilized, classified, and handed to the provider layer locally.

## Files to Create or Modify

- `agent/app/queue_worker.py`
- `agent/app/queue_service.py`
- `agent/app/provider.py`
- `agent/app/dry_run_provider.py`
- `agent/tests/test_queue_service.py`

## Requirements

- Process queued items in a single local worker loop or equivalent background task.
- Respect queue item states, stability checks, and provider outcomes.
- Record success, retry, and failure states predictably.

## Constraints

- Do not create a distributed job system.
- Do not block the API from receiving new events while the worker runs.
- Do not route work to a real cloud service in the MVP.

## Acceptance Criteria

- The worker can process queued events end to end in dry-run mode.
- Failures are recorded rather than hidden.
- The worker cooperates with dedupe and stability behavior.

## Test Expectations

- Add tests for successful item processing.
- Add tests for deferred and failed item states.
