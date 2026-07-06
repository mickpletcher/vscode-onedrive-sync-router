# Future Graph Provider Design

This document describes the future Microsoft Graph provider direction for vscode-onedrive-sync-router.

The provider abstraction should allow a later implementation to publish, reconcile, or compare queue items against remote state without changing the local-first MVP contract. Any future Graph integration must remain separate from the dry-run provider and must not be presented as currently available behavior.

## Provider Interface Contract

The current provider interface is intentionally small:

- Input: a queue item with resolved file metadata and event classification.
- Output: a provider result with `ok`, `message`, and optional structured `details`.

Future providers should continue to implement this contract so the queue worker and API status endpoints remain unchanged.

## Future Graph Provider Responsibilities

A future Graph provider may:

- Map queued create/modify/delete/rename actions into Microsoft Graph operations.
- Compare local queue intent with remote file metadata for conflict-aware behavior.
- Capture remote operation IDs, etags, and retry hints in provider result details.

It must not bypass path validation, rule classification, or queue lifecycle behavior.

## Separation From Dry-Run Provider

The dry-run provider remains the default and only MVP provider behavior. Graph provider work must be opt-in and clearly separated at configuration and runtime:

- `provider_mode = dry-run`: record intended actions only.
- `provider_mode = graph` (future): attempt remote publish/reconcile.

No code path should silently switch from dry-run to real cloud write behavior.

## Risk and Boundary Notes

- Credential handling must remain local and explicit.
- Failed Graph operations should return structured failures and keep queue state consistent.
- Backoff and retry logic should avoid hot loops and preserve deterministic local queue semantics.
- Conflict reporting should surface likely mismatches, not claim guaranteed prevention.

The MVP does not perform real cloud writes.
