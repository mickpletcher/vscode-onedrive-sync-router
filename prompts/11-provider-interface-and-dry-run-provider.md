# 11 Provider Interface and Dry-Run Provider

## Objective

Define the provider layer for vscode-onedrive-sync-router and implement the dry-run provider as the default MVP behavior.

## Files to Create or Modify

- `agent/app/provider.py`
- `agent/app/dry_run_provider.py`
- `agent/app/models.py`
- `agent/tests/test_api.py`

## Requirements

- Create a provider interface that can represent queue item handling without performing real cloud writes.
- Implement a dry-run provider that logs or records intended actions locally.
- Make the default provider path safe for local-first development.

## Constraints

- Do not implement Microsoft Graph publishing yet.
- Do not make any external write calls in the MVP.
- Do not blur the boundary between dry-run and future provider implementations.

## Acceptance Criteria

- The agent can route queue items through the provider abstraction.
- The dry-run provider returns predictable local results.
- The provider interface is ready for later native observer or Graph work.

## Test Expectations

- Add tests that confirm the dry-run provider does not call a real cloud service.
- Add tests that provider selection is deterministic.
