# Architecture

vscode-onedrive-sync-router uses a local-first architecture:

VS Code Extension -> Local Sync Router Agent -> Local SQLite Queue -> Provider Layer -> Dry Run / Native Observer / Future Microsoft Graph Publish

The extension observes file activity after the editor writes the file. The agent validates the event, classifies it, stores it in SQLite, and processes it through a local worker. The MVP provider is a dry-run provider that records intended actions without performing real cloud writes.

The system does not intercept, pause, delay, or control the native OneDrive desktop sync client. That boundary is intentional and should remain explicit in the code and documentation.
