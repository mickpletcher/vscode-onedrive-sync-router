# Copilot Build Kickoff

Use this file to start the vscode-onedrive-sync-router build in GitHub Copilot Chat. Do not treat this as an extra implementation prompt; it is the operating process for executing the numbered prompts already in this folder.

## What Copilot Should Build

Build vscode-onedrive-sync-router as a local-first VS Code extension and sync routing agent that reduces OneDrive file sync conflict risk by queuing, deduping, classifying, and safely routing VS Code file activity.

Preserve this architecture:

```text
VS Code Extension -> Local Sync Router Agent -> Local SQLite Queue -> Provider Layer -> Dry Run / Native Observer / Future Microsoft Graph Publish
```

The MVP is dry-run first. It must not:

- Intercept, pause, delay, or control the native OneDrive desktop sync client.
- Perform real Microsoft Graph or OneDrive cloud writes.
- Depend on n8n, VPNs, home servers, kernel drivers, filesystem drivers, or cloud-only infrastructure.
- Require secrets or external services for tests.

## Prompt Execution Order

Execute the prompts in numeric order:

1. `prompts/00-project-overview.md`
2. `prompts/01-repo-structure.md`
3. `prompts/02-agent-fastapi-foundation.md`
4. `prompts/03-agent-configuration.md`
5. `prompts/04-path-security-and-root-resolution.md`
6. `prompts/05-rule-engine.md`
7. `prompts/06-database-and-migrations.md`
8. `prompts/07-queue-service.md`
9. `prompts/08-file-events-api.md`
10. `prompts/09-dedupe-and-coalescing.md`
11. `prompts/10-file-stability-and-revision-checks.md`
12. `prompts/11-provider-interface-and-dry-run-provider.md`
13. `prompts/12-conflict-detection.md`
14. `prompts/13-background-worker.md`
15. `prompts/14-agent-security.md`
16. `prompts/15-status-and-queue-endpoints.md`
17. `prompts/16-vscode-extension-scaffold.md`
18. `prompts/17-vscode-event-sender.md`
19. `prompts/18-vscode-status-bar-and-commands.md`
20. `prompts/19-testing-plan.md`
21. `prompts/20-documentation.md`
22. `prompts/21-github-actions-and-quality-gates.md`
23. `prompts/22-future-graph-provider-design.md`

## Build Process For Copilot

For each numbered prompt:

1. Read the prompt completely before editing files.
2. Check the current repository state first; if part of the prompt is already implemented, verify it rather than duplicating it.
3. Implement only the files and behavior requested by that prompt unless a small supporting edit is required to make the prompt pass.
4. Keep behavior local-first and dry-run safe.
5. Add or update focused tests named by the prompt.
6. Run only the relevant validation commands for the files touched.
7. Summarize changed files, validation results, and the next prompt to run.
8. Stop after each prompt and wait for the user's approval before continuing.

## Validation Commands

Use these commands when the relevant part of the project has been touched.

Backend agent:

```bash
cd agent
python -m pip install -e '.[dev]'
pytest
```

VS Code extension:

```bash
cd vscode-extension
npm install
npm run check
```

CI workflow reference:

```bash
.github/workflows/ci.yml
```

Do not start the local agent, extension host, or any long-running build/watch task unless the user explicitly asks for it.

## First Message To Paste Into GitHub Copilot

```text
We are building vscode-onedrive-sync-router from the sequential prompt files in this repository.

Start with prompts/00-project-overview.md only. Read prompts/copilot-build-kickoff.md and .github/copilot-instructions.md first, then read prompts/00-project-overview.md completely.

Implement only prompt 00. Preserve the local-first dry-run MVP boundary: do not claim direct control over native OneDrive sync, do not add real cloud writes, and do not require external services.

Before editing, check the current files named in the prompt and report what already exists. Then make the smallest needed changes, run only validations that are relevant to prompt 00, summarize the changed files and validation results, and stop. Wait for my approval before moving to prompt 01.
```

## Handoff Notes

- The existing prompt set is already numbered and standalone.
- The first implementation pass should be conservative; prefer prompt-sized changes over broad refactors.
- Keep project naming consistent as `vscode-onedrive-sync-router`.
- Keep the VS Code extension identifier as `vscode-onedrive-sync-router`.
- Keep the VS Code extension display name as `VS Code OneDrive Sync Router`.
