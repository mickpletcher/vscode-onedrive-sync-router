# Rules

The rule engine in vscode-onedrive-sync-router should stay deterministic, conservative, and local-first.

Core rules:

- Reject unsafe or out-of-root paths.
- Ignore obvious infrastructure and generated files when appropriate.
- Classify file activity by path, extension, event type, and workspace context.
- Prefer queueing and stabilization over immediate processing when the file is still changing.
- Use the dry-run provider for the MVP.

Rules should be simple enough to unit test and stable enough to produce predictable queue behavior.