Use this replacement block at the top of the Copilot prompt, and replace every instance of onedrive-sync-router with vscode-onedrive-sync-router.

GitHub Copilot Prompt

Create a directory named prompts at the repository root.

Inside prompts, create a series of numbered Markdown prompt files that break the vscode-onedrive-sync-router project into small, sequential implementation prompts.

The goal is not to build the full project immediately. The goal is to generate a clean prompt plan that can later be executed file by file in GitHub Copilot.

Project name:

vscode-onedrive-sync-router

Project purpose:

Create a lightweight, local-first VS Code extension and sync routing agent that reduces OneDrive file sync conflict risk by queuing, deduping, classifying, and safely routing VS Code file activity through a local agent, rule engine, SQLite queue, and future OneDrive/Microsoft Graph provider layer.

Important architectural rule:

This project does not intercept, pause, delay, or control the native OneDrive desktop sync client. VS Code file events occur after files are written. The MVP must not claim that it can directly batch native OneDrive synchronization.

The generated prompt files must preserve this architecture:

VS Code Extension → Local Sync Router Agent → Local SQLite Queue → Provider Layer → Dry Run / Native Observer / Future Microsoft Graph Publish

The system must work locally on each coding machine. It must not depend on n8n, VPN, home servers, kernel drivers, filesystem drivers, or cloud-only infrastructure.

Use this repository structure as the intended final structure:

vscode-onedrive-sync-router/
  agent/
    app/
      main.py
      config.py
      database.py
      migrations.py
      models.py
      rule_engine.py
      queue_service.py
      queue_worker.py
      provider.py
      dry_run_provider.py
      conflict_detection.py
      path_utils.py
      file_stability.py
      security.py
      logging_config.py
    config/
      sync-router.example.json
    tests/
      test_rule_engine.py
      test_path_utils.py
      test_queue_service.py
      test_dedupe.py
      test_file_stability.py
      test_security.py
      test_api.py
    pyproject.toml
    README.md
  vscode-extension/
    src/
      extension.ts
      client.ts
      status.ts
      commands.ts
      types.ts
      config.ts
      secrets.ts
      output.ts
    package.json
    tsconfig.json
    README.md
  docs/
    architecture.md
    rules.md
    conflict-handling.md
    setup-macos.md
    setup-windows.md
    development-roadmap.md
    graph-provider-design.md
  prompts/
  README.md
  .gitignore
  .github/
    workflows/
      ci.yml

Create the following prompt files:

prompts/
  00-project-overview.md
  01-repo-structure.md
  02-agent-fastapi-foundation.md
  03-agent-configuration.md
  04-path-security-and-root-resolution.md
  05-rule-engine.md
  06-database-and-migrations.md
  07-queue-service.md
  08-file-events-api.md
  09-dedupe-and-coalescing.md
  10-file-stability-and-revision-checks.md
  11-provider-interface-and-dry-run-provider.md
  12-conflict-detection.md
  13-background-worker.md
  14-agent-security.md
  15-status-and-queue-endpoints.md
  16-vscode-extension-scaffold.md
  17-vscode-event-sender.md
  18-vscode-status-bar-and-commands.md
  19-testing-plan.md
  20-documentation.md
  21-github-actions-and-quality-gates.md
  22-future-graph-provider-design.md

Each generated prompt file must refer to the project as vscode-onedrive-sync-router.

The README, documentation, package metadata, GitHub Actions workflow, VS Code extension metadata, and generated prompt files must all use vscode-onedrive-sync-router consistently.

Use this short project description anywhere a concise description is needed:

A local-first VS Code extension and sync routing agent that reduces OneDrive file sync conflict risk by queuing, deduping, classifying, and safely routing VS Code file activity.

Acceptance criteria for this prompt generation task:

1. The prompts directory exists.
2. All 23 Markdown prompt files exist.
3. Each prompt file is standalone.
4. The files are numbered in implementation order.
5. Each file includes objective, files to create or modify, requirements, constraints, acceptance criteria, and test expectations where relevant.
6. Every generated prompt uses vscode-onedrive-sync-router as the project name.
7. No generated prompt uses onedrive-sync-router as the project name.
8. The prompt files are consistent with each other.
9. No generated prompt claims the project can directly control native OneDrive desktop sync.
10. No generated prompt tells the MVP to perform real cloud writes.
11. The prompt set builds toward a dry-run local-first MVP first.
12. Future Graph work is isolated to design and provider interface prompts unless explicitly marked as future implementation.
13. The final prompt file set is ready to be executed sequentially by GitHub Copilot.

Also update any internal package identifiers like this:

Python package/module label: vscode-onedrive-sync-router
VS Code extension display name: VS Code OneDrive Sync Router
VS Code extension identifier: vscode-onedrive-sync-router
CLI name, if added later: vscode-onedrive-sync-router
