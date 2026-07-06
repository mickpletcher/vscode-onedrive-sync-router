import * as vscode from "vscode";

import type { AgentClient } from "./client";
import { getOutputChannel, logLine } from "./output";
import type { StatusBarController } from "./status";

export function registerCommands(context: vscode.ExtensionContext, client: AgentClient, statusBar: StatusBarController): void {
  context.subscriptions.push(
    vscode.commands.registerCommand("vscode-onedrive-sync-router.refreshStatus", async () => {
      const status = await client.getStatus();
      statusBar.update(status);
      logLine("Refreshed vscode-onedrive-sync-router status.");
    }),
  );

  context.subscriptions.push(
    vscode.commands.registerCommand("vscode-onedrive-sync-router.showQueue", async () => {
      const items = await client.getQueueItems();
      logLine(JSON.stringify(items, null, 2));
      getOutputChannel().show(true);
    }),
  );

  context.subscriptions.push(
    vscode.commands.registerCommand("vscode-onedrive-sync-router.openLogs", async () => {
      getOutputChannel().show(true);
    }),
  );
}
