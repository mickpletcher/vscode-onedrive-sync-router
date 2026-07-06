# 16 VS Code Extension Scaffold

## Objective

Create the VS Code extension scaffold for vscode-onedrive-sync-router so the editor can talk to the local sync router agent.

## Files to Create or Modify

- `vscode-extension/package.json`
- `vscode-extension/tsconfig.json`
- `vscode-extension/src/extension.ts`
- `vscode-extension/src/client.ts`
- `vscode-extension/src/types.ts`
- `vscode-extension/src/config.ts`
- `vscode-extension/src/output.ts`
- `vscode-extension/src/status.ts`
- `vscode-extension/src/commands.ts`
- `vscode-extension/src/secrets.ts`

## Requirements

- Create a minimal extension activation flow.
- Add the VS Code extension identifier vscode-onedrive-sync-router.
- Set the display name to VS Code OneDrive Sync Router.
- Prepare the extension to register commands, status UI, and agent communication.

## Constraints

- Do not embed cloud-write behavior in the extension scaffold.
- Do not overbuild UI before the agent API exists.
- Do not rename the project away from vscode-onedrive-sync-router.

## Acceptance Criteria

- The extension can activate in VS Code.
- Metadata and scripts use the correct project name and identifier.
- Source files are ready for the event sender and status work.

## Test Expectations

- Add a minimal extension build or typecheck expectation.
- Ensure package metadata uses vscode-onedrive-sync-router consistently.
