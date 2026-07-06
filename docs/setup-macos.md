# macOS Setup

## Requirements

- Python 3.11 or newer
- Node.js 20 or newer
- VS Code

## Setup

1. Create a Python environment in `agent/`.
2. Install the Python dependencies defined in `agent/pyproject.toml`.
3. Install the VS Code extension dependencies in `vscode-extension/`.
4. Start the local FastAPI agent.
5. Run the extension against the local agent endpoint.

The MVP is local-only and should not require cloud credentials.