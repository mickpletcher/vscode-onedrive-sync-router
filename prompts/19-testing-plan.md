# 19 Testing Plan

## Objective

Define and implement the test plan for vscode-onedrive-sync-router across the agent, the extension, and their local contract.

## Files to Create or Modify

- `agent/tests/test_rule_engine.py`
- `agent/tests/test_path_utils.py`
- `agent/tests/test_queue_service.py`
- `agent/tests/test_dedupe.py`
- `agent/tests/test_file_stability.py`
- `agent/tests/test_security.py`
- `agent/tests/test_api.py`
- `vscode-extension/src/*.ts` test support files if needed

## Requirements

- Cover path validation, rule classification, queue transitions, dedupe, stability, security, and API responses.
- Include enough extension-side coverage to verify agent communication and command registration.
- Prefer deterministic tests that run locally without cloud dependencies.

## Constraints

- Do not require network access for the test suite.
- Do not rely on a real Microsoft Graph endpoint.
- Do not make tests depend on native OneDrive sync timing.

## Acceptance Criteria

- The test matrix covers the MVP-local behavior end to end.
- Each important backend module has at least one meaningful test.
- The extension has a clear path for build and type checks.

## Test Expectations

- Add explicit test commands or scripts where helpful.
- Keep tests aligned with the local-first dry-run design.
