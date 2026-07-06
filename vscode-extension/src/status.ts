import * as vscode from "vscode";

import type { AgentStatus } from "./types";

export class StatusBarController {
  private readonly item: vscode.StatusBarItem;

  public constructor() {
    this.item = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
    this.item.command = "vscode-onedrive-sync-router.refreshStatus";
  }

  public show(): void {
    this.item.show();
  }

  public dispose(): void {
    this.item.dispose();
  }

  public update(status: AgentStatus | undefined): void {
    if (!status) {
      this.item.text = "$(cloud-offline) vscode-onedrive-sync-router";
      this.item.tooltip = "Local agent status unavailable";
      return;
    }

    const queueCount = Object.values(status.queue ?? {}).reduce((total, value) => total + value, 0);
    this.item.text = `$(sync) vscode-onedrive-sync-router ${queueCount}`;
    this.item.tooltip = `Mode: ${status.mode}; Queue items: ${queueCount}`;
  }
}
