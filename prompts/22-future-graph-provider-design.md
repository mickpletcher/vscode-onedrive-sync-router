# 22 Future Graph Provider Design

## Objective
Document the future Microsoft Graph provider design for vscode-onedrive-sync-router without implementing real cloud writes in the MVP.

## Files to Create or Modify
- `docs/graph-provider-design.md`
- `agent/app/provider.py`
- `agent/app/dry_run_provider.py`

## Requirements
- Describe how a future provider could publish or reconcile queued work through Microsoft Graph.
- Keep the design isolated from the current local-first MVP implementation.
- Define the interface expectations needed so the provider layer can evolve later.

## Constraints
- Do not implement real Graph write operations in this prompt.
- Do not move MVP behavior away from dry-run mode.
- Do not imply that future design work is already shipped functionality.

## Acceptance Criteria
- The design explains the provider contract clearly.
- The document identifies future-only responsibilities and risks.
- The current code remains safe for local-only use.

## Test Expectations
- No integration test is required for this future-design prompt.
- If interface notes are added, verify they do not advertise unsupported behavior.