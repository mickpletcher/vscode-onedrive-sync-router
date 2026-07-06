# 17 VS Code Event Sender

## Objective
Implement the extension-side event sender for vscode-onedrive-sync-router so VS Code file activity is posted to the local agent.

## Files to Create or Modify
- `vscode-extension/src/client.ts`
- `vscode-extension/src/extension.ts`
- `vscode-extension/src/types.ts`
- `vscode-extension/src/config.ts`

## Requirements
- Listen for relevant editor file events and forward them to the local backend.
- Batch or debounce client-side emissions only when it improves local reliability.
- Preserve enough context for the agent to classify, dedupe, and stabilize events.

## Constraints
- Do not attempt to control the OneDrive desktop client.
- Do not send events to a remote service by default.
- Do not perform cloud writes from the extension.

## Acceptance Criteria
- Editor events reach the local agent over the local API.
- Event payloads are consistent with the backend schema.
- Failures are surfaced to the user or output channel.

## Test Expectations
- Add a unit or integration-style test for payload assembly.
- Add a test that local agent unavailability is handled gracefully.