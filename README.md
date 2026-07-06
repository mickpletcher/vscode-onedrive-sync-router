# vscode-onedrive-sync-router

> **Status: Under construction. Not ready for use.**
> This project is actively being built out and has known gaps between documented behavior and current implementation. Do not rely on it for real OneDrive workspaces yet.

A local-first VS Code extension and sync routing agent that reduces OneDrive file sync conflict risk by queuing, deduping, classifying, and safely routing VS Code file activity.

## Architecture

VS Code Extension -> Local Sync Router Agent -> Local SQLite Queue -> Provider Layer -> Dry Run / Native Observer / Future Microsoft Graph Publish

This repository is intentionally local-first. It does not intercept, pause, delay, or control the native OneDrive desktop sync client, and the MVP does not perform real cloud writes.

## Repository Layout

- `agent/` - FastAPI backend, queue service, SQLite storage, and provider abstraction.
- `vscode-extension/` - VS Code extension that sends file activity to the local agent and displays status.
- `docs/` - Architecture, setup, roadmap, and future provider design notes.
- `prompts/` - Sequential Copilot prompts that can be executed file by file.

## MVP Scope

The initial goal is a dry-run local-first workflow:

1. VS Code captures file events.
2. The extension sends them to the local agent.
3. The agent validates paths, classifies events, and writes them to a local SQLite queue.
4. A local worker dedupes, stabilizes, and routes items through a dry-run provider.

## Project Name

The project name is vscode-onedrive-sync-router.
