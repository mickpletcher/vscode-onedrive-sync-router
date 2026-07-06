# 14 Agent Security

## Objective
Add security controls for the vscode-onedrive-sync-router backend so only the local extension and trusted local callers can submit work.

## Files to Create or Modify
- `agent/app/security.py`
- `agent/app/main.py`
- `agent/app/config.py`
- `agent/tests/test_security.py`

## Requirements
- Add local authentication or shared-secret style protections suitable for a developer machine.
- Validate caller origin or token handling where appropriate.
- Avoid leaking secrets, paths, or queue payloads in logs.

## Constraints
- Do not require enterprise identity infrastructure for the MVP.
- Do not weaken path validation or queue validation.
- Do not expose the agent broadly on the network by default.

## Acceptance Criteria
- Unauthorized callers are rejected.
- Secret handling is local and minimal.
- Security behavior is testable and documented.

## Test Expectations
- Add tests for accepted and rejected caller scenarios.
- Add tests that sensitive values are not echoed back in responses.