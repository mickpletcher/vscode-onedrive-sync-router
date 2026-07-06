# Copilot Instructions

This repository is vscode-onedrive-sync-router.

Build from the numbered prompt files in `prompts/`, starting with `prompts/00-project-overview.md` and continuing in numeric order. Read `prompts/copilot-build-kickoff.md` before beginning implementation work.

Core boundaries:

- The product is local-first and dry-run first.
- The architecture is `VS Code Extension -> Local Sync Router Agent -> Local SQLite Queue -> Provider Layer -> Dry Run / Native Observer / Future Microsoft Graph Publish`.
- Do not claim the project can intercept, pause, delay, batch, or control the native OneDrive desktop sync client.
- Do not implement real Microsoft Graph or OneDrive cloud writes in the MVP.
- Do not require n8n, VPNs, home servers, kernel drivers, filesystem drivers, cloud-only infrastructure, secrets, or external services for normal tests.

Implementation process:

- Complete one numbered prompt at a time.
- Before editing, inspect the files listed by the current prompt and reuse existing code where it already satisfies the prompt.
- Keep changes scoped to the current prompt unless a small supporting edit is required for correctness.
- Add focused tests that match the current prompt's test expectations.
- Prefer deterministic local tests over networked or timing-sensitive tests.
- After each prompt, summarize changed files, validation commands, and remaining risks, then wait for the user before continuing.

Expected validation commands:

```bash
cd agent
python -m pip install -e '.[dev]'
pytest
```

```bash
cd vscode-extension
npm install
npm run check
```

Do not start long-running local servers, extension hosts, watch tasks, or production builds unless the user explicitly asks.
