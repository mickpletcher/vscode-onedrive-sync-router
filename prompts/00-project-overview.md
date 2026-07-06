# 00 Project Overview

## Objective

Establish the project charter for vscode-onedrive-sync-router: a local-first VS Code extension and sync routing agent that reduces OneDrive file sync conflict risk by queuing, deduping, classifying, and safely routing VS Code file activity.

## Files to Create or Modify

- `README.md`
- `docs/architecture.md`
- `docs/development-roadmap.md`
- `docs/conflict-handling.md`
- `docs/rules.md`

## Requirements

- Define the architecture as VS Code Extension → Local Sync Router Agent → Local SQLite Queue → Provider Layer → Dry Run / Native Observer / Future Microsoft Graph Publish.
- State clearly that the project does not intercept, pause, delay, or control the native OneDrive desktop sync client.
- State that the MVP is local-first and dry-run oriented.
- Use the project name vscode-onedrive-sync-router everywhere.
- Use the short description: A local-first VS Code extension and sync routing agent that reduces OneDrive file sync conflict risk by queuing, deduping, classifying, and safely routing VS Code file activity.

## Constraints

- Do not promise direct control over native OneDrive synchronization.
- Do not describe any real cloud writes for the MVP.
- Do not introduce n8n, VPN, home-server, kernel-driver, filesystem-driver, or cloud-only dependencies.

## Acceptance Criteria

- The project purpose and scope are written consistently across the selected docs.
- The local-first and dry-run-first MVP framing is explicit.
- The architecture boundary between VS Code events and OneDrive sync is unambiguous.

## Test Expectations

- No code test is required for this prompt.
- If the documents are updated, verify that every mention of the project name uses vscode-onedrive-sync-router.
