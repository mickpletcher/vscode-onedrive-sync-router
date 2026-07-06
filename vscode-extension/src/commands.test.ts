import { describe, expect, it, vi } from "vitest";

const { registerCommand } = vi.hoisted(() => ({
  registerCommand: vi.fn((_name, callback) => ({ dispose: vi.fn(), callback })),
}));

vi.mock("vscode", () => ({
  commands: {
    registerCommand,
  },
}));

import { registerCommands } from "./commands";

describe("registerCommands", () => {
  it("registers expected commands", () => {
    const context = { subscriptions: [] as Array<{ dispose: () => void }> };
    const client = {
      getStatus: vi.fn(),
      getQueueItems: vi.fn(),
    };
    const statusBar = {
      update: vi.fn(),
    };

    registerCommands(context as never, client as never, statusBar as never);

    expect(registerCommand).toHaveBeenCalledTimes(3);
    expect(registerCommand).toHaveBeenCalledWith(
      "vscode-onedrive-sync-router.refreshStatus",
      expect.any(Function),
    );
    expect(registerCommand).toHaveBeenCalledWith(
      "vscode-onedrive-sync-router.showQueue",
      expect.any(Function),
    );
    expect(registerCommand).toHaveBeenCalledWith(
      "vscode-onedrive-sync-router.openLogs",
      expect.any(Function),
    );
    expect(context.subscriptions.length).toBe(3);
  });
});
