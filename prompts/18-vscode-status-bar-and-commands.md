# 18 VS Code Status Bar and Commands

## Objective

Add status bar, command, and output-channel behavior for vscode-onedrive-sync-router so users can inspect the local agent and queue state inside VS Code.

## Files to Create or Modify

- `vscode-extension/src/status.ts`
- `vscode-extension/src/commands.ts`
- `vscode-extension/src/output.ts`
- `vscode-extension/src/extension.ts`

## Requirements

- Register commands for showing agent status, opening logs, and refreshing queue state.
- Show a concise status bar indicator that reflects local health.
- Use the output channel for diagnostic messages instead of noisy popups.

## Constraints

- Do not add unnecessary UI complexity.
- Do not expose secrets or file contents in status text.
- Do not imply direct control over OneDrive sync.

## Acceptance Criteria

- Commands are registered and callable from VS Code.
- Status feedback updates from agent responses.
- Output messages are useful without being verbose.

## Test Expectations

- Add a check that commands are registered.
- Add a check that status bar text can update from a local status response.
