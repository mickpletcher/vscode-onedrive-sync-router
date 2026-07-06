import { describe, expect, it, vi } from "vitest";

const statusItem = {
  text: "",
  tooltip: "",
  command: "",
  show: vi.fn(),
  dispose: vi.fn(),
};

vi.mock("vscode", () => ({
  StatusBarAlignment: { Left: 1, Right: 2 },
  window: {
    createStatusBarItem: vi.fn(() => statusItem),
  },
}));

import { StatusBarController } from "./status";

describe("StatusBarController", () => {
  it("shows offline text when status is unavailable", () => {
    const controller = new StatusBarController();
    controller.update(undefined);

    expect(statusItem.text).toBe("$(cloud-offline) vscode-onedrive-sync-router");
    expect(statusItem.tooltip).toBe("Local agent status unavailable");
  });

  it("shows queue total when status is present", () => {
    const controller = new StatusBarController();
    controller.update({
      service: "vscode-onedrive-sync-router",
      mode: "dry-run",
      queue: { pending: 2, completed: 1 },
    });

    expect(statusItem.text).toBe("$(sync) vscode-onedrive-sync-router 3");
    expect(statusItem.tooltip).toBe("Mode: dry-run; Queue items: 3");
  });
});
