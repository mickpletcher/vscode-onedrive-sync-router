# 02 Agent FastAPI Foundation

## Objective

Build the backend application foundation for the local sync router agent as a FastAPI service for vscode-onedrive-sync-router.

## Files to Create or Modify

- `agent/pyproject.toml`
- `agent/app/main.py`
- `agent/app/logging_config.py`
- `agent/app/models.py`
- `agent/tests/test_api.py`

## Requirements

- Create a FastAPI application factory or equivalent clean entry point.
- Add a health endpoint and a minimal API root response.
- Set up structured logging for the local agent.
- Keep the service local-only by default.

## Constraints

- Do not add Graph write logic.
- Do not add extension logic in this step.
- Do not assume the agent can influence native OneDrive sync behavior directly.

## Acceptance Criteria

- The agent starts successfully as a local FastAPI app.
- Health and root endpoints respond predictably.
- The code layout supports later queue, rule, and provider modules.

## Test Expectations

- Add an API test that verifies the health endpoint.
- Add an API test that verifies the service returns a stable local-only response.
