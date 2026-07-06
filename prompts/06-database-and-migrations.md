# 06 Database and Migrations

## Objective

Add the SQLite persistence layer for vscode-onedrive-sync-router with a small schema that supports queueing, dedupe, status, and audit history.

## Files to Create or Modify

- `agent/app/database.py`
- `agent/app/migrations.py`
- `agent/app/models.py`
- `agent/tests/test_queue_service.py`

## Requirements

- Create a durable SQLite schema for queued events and processing state.
- Include timestamps, dedupe keys, status fields, and workspace identifiers.
- Make migration behavior explicit and repeatable.

## Constraints

- Keep the schema compact for the MVP.
- Do not introduce cloud database dependencies.
- Do not store more data than the queue and status features need.

## Acceptance Criteria

- The database initializes cleanly on a fresh machine.
- Schema changes can be applied deterministically.
- Models map cleanly to the queue service and API layers.

## Test Expectations

- Add a test that creates the database and schema from scratch.
- Add a test that a migration or schema upgrade path is repeatable.
