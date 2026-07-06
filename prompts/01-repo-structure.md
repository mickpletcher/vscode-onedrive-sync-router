# 01 Repo Structure

## Objective

Create the repository skeleton for vscode-onedrive-sync-router so the backend agent, VS Code extension, docs, and prompts can be implemented in later steps without changing the architecture.

## Files to Create or Modify

- `agent/app/main.py`
- `agent/app/config.py`
- `agent/app/database.py`
- `agent/app/migrations.py`
- `agent/app/models.py`
- `agent/app/rule_engine.py`
- `agent/app/queue_service.py`
- `agent/app/queue_worker.py`
- `agent/app/provider.py`
- `agent/app/dry_run_provider.py`
- `agent/app/conflict_detection.py`
- `agent/app/path_utils.py`
- `agent/app/file_stability.py`
- `agent/app/security.py`
- `agent/app/logging_config.py`
- `agent/config/sync-router.example.json`
- `agent/tests/`
- `vscode-extension/src/`
- `vscode-extension/package.json`
- `vscode-extension/tsconfig.json`
- `docs/`
- `.github/workflows/ci.yml`
- `.gitignore`
- `README.md`

## Requirements

- Create the final folder layout described by the project charter.
- Keep the structure local-first and split cleanly between `agent/`, `vscode-extension/`, `docs/`, and `prompts/`.
- Use vscode-onedrive-sync-router for all package, extension, and repository naming.

## Constraints

- Use placeholder implementations only if needed for the scaffold.
- Do not add any provider implementation that performs real cloud writes.
- Do not couple the extension directly to OneDrive or Graph APIs in this step.

## Acceptance Criteria

- The repo contains the intended directories and placeholder files.
- The backend and extension boundaries are visible from the file structure.
- The scaffold is compatible with later FastAPI, SQLite, and TypeScript implementation steps.

## Test Expectations

- If placeholder files are added, make sure they do not introduce syntax errors.
- If a README is updated, confirm the name appears as vscode-onedrive-sync-router.
