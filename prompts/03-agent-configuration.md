# 03 Agent Configuration

## Objective
Add configuration loading and example settings for the vscode-onedrive-sync-router backend agent.

## Files to Create or Modify
- `agent/app/config.py`
- `agent/config/sync-router.example.json`
- `agent/app/main.py`
- `agent/tests/test_api.py`

## Requirements
- Support configuration from environment variables and a local JSON file.
- Include settings for host, port, database path, queue behavior, and dry-run mode.
- Use the project name vscode-onedrive-sync-router in all example metadata and comments.

## Constraints
- Keep defaults safe for local development.
- Do not require cloud credentials for the MVP.
- Do not expose secrets in logs or example files.

## Acceptance Criteria
- The agent can load a config file with sane defaults.
- The example config documents local-first behavior clearly.
- Configuration values are easy to reuse in later queue and provider modules.

## Test Expectations
- Add a test for config parsing or loading.
- Add a test that default values do not require external services.