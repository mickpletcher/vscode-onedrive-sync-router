# Future Graph Provider Design

This document describes the future Microsoft Graph provider direction for vscode-onedrive-sync-router.

The provider abstraction should allow a later implementation to publish, reconcile, or compare queue items against remote state without changing the local-first MVP contract. Any future Graph integration must remain separate from the dry-run provider and must not be presented as currently available behavior.

The MVP does not perform real cloud writes.