import { beforeEach, describe, expect, it, vi } from "vitest";

import { AgentClient } from "./client";

const { getWorkspaceFolder } = vi.hoisted(() => ({
  getWorkspaceFolder: vi.fn(),
}));

vi.mock("vscode", () => ({
  workspace: {
    getWorkspaceFolder,
  },
}));

describe("AgentClient", () => {
  beforeEach(() => {
    getWorkspaceFolder.mockReset();
    vi.restoreAllMocks();
  });

  it("posts file events with shared-secret header", async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true });
    vi.stubGlobal("fetch", fetchMock);

    const client = new AgentClient("http://127.0.0.1:8765", "secret");
    const ok = await client.postFileEvent({
      workspaceRoot: "/tmp/ws",
      filePath: "/tmp/ws/file.md",
      eventType: "modify",
      timestamp: "2026-07-06T12:00:00Z",
    });

    expect(ok).toBe(true);
    expect(fetchMock).toHaveBeenCalledTimes(1);
    expect(fetchMock).toHaveBeenCalledWith(
      "http://127.0.0.1:8765/events",
      expect.objectContaining({
        method: "POST",
        headers: expect.objectContaining({
          "Content-Type": "application/json",
          "X-Sync-Router-Token": "secret",
        }),
      }),
    );
  });

  it("returns false when document has no workspace folder", async () => {
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);

    getWorkspaceFolder.mockReturnValue(undefined);

    const client = new AgentClient("http://127.0.0.1:8765", "");
    const ok = await client.sendDocumentEvent(
      {
        uri: { fsPath: "/tmp/ws/file.md" },
        languageId: "markdown",
        getText: () => "hello",
      } as never,
      "modify",
    );

    expect(ok).toBe(false);
    expect(fetchMock).not.toHaveBeenCalled();
  });
});
