# 20 Documentation

## Objective
Write the core documentation for vscode-onedrive-sync-router so the architecture, rules, setup, and roadmap are clear to future contributors.

## Files to Create or Modify
- `README.md`
- `docs/architecture.md`
- `docs/rules.md`
- `docs/conflict-handling.md`
- `docs/setup-macos.md`
- `docs/setup-windows.md`
- `docs/development-roadmap.md`
- `docs/graph-provider-design.md`
- `agent/README.md`
- `vscode-extension/README.md`

## Requirements
- Document the local-first architecture and the dry-run MVP path.
- Explain setup, configuration, and how the agent and extension fit together.
- Keep the project name vscode-onedrive-sync-router consistent everywhere.

## Constraints
- Do not describe unsupported real cloud writes as available functionality.
- Do not claim direct control over native OneDrive sync.
- Do not bury the local-first constraint in the docs.

## Acceptance Criteria
- New contributors can understand the architecture and setup from the docs.
- The documentation matches the code boundaries established in earlier prompts.
- The Graph material remains clearly future-facing.

## Test Expectations
- Review docs for name consistency and architectural accuracy.
- Ensure setup instructions align with the MVP implementation plan.