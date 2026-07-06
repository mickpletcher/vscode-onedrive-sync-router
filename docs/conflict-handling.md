# Conflict Handling

vscode-onedrive-sync-router is designed to reduce conflict risk, not to control native OneDrive sync.

Conflict handling strategy:

1. Validate the event path and workspace root.
2. Classify the event and decide whether it should be queued.
3. Wait for the file to become stable when necessary.
4. Flag suspicious churn or unstable revisions for review.
5. Route the queued item through the provider abstraction in dry-run mode for the MVP.

The initial implementation should keep conflict detection conservative. It is better to defer processing than to guess incorrectly.