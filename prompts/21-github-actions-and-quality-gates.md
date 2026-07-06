# 21 GitHub Actions and Quality Gates

## Objective
Add GitHub Actions and quality gates for vscode-onedrive-sync-router so the repo validates formatting, tests, and build correctness locally and in CI.

## Files to Create or Modify
- `.github/workflows/ci.yml`
- `agent/pyproject.toml`
- `vscode-extension/package.json`
- `README.md`

## Requirements
- Run backend tests, extension type checks, and any lint or formatting checks that fit the MVP.
- Use the project name vscode-onedrive-sync-router in workflow metadata where relevant.
- Keep the pipeline focused on local-first correctness, not deployment.

## Constraints
- Do not add deployment steps for cloud publishing.
- Do not require secrets for the quality gate.
- Do not add checks that assume native OneDrive control.

## Acceptance Criteria
- The CI workflow checks the important local build surfaces.
- The quality gates match the repo structure and test plan.
- The workflow can run without external services.

## Test Expectations
- Confirm the workflow references valid test and build commands.
- Confirm the workflow does not require cloud credentials.