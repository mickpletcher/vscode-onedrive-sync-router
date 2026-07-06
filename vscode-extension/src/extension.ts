import * as vscode from "vscode";

import { AgentClient } from "./client";
import { getExtensionConfiguration } from "./config";
import { getOutputChannel, logLine } from "./output";
import { registerCommands } from "./commands";
import { StatusBarController } from "./status";

export async function activate(context: vscode.ExtensionContext): Promise<void> {
  const configuration = getExtensionConfiguration();
  const client = new AgentClient(configuration.agentUrl, configuration.sharedSecret);
  const statusBar = new StatusBarController();

  context.subscriptions.push(getOutputChannel());
  context.subscriptions.push(statusBar);
  registerCommands(context, client, statusBar);

  statusBar.show();

  const refresh = async (): Promise<void> => {
    statusBar.update(await client.getStatus());
  };

  void refresh();

  context.subscriptions.push(
    vscode.workspace.onDidSaveTextDocument(async (document) => {
      await client.sendDocumentEvent(document, "modify");
    }),
  );

  context.subscriptions.push(
    vscode.workspace.onDidCreateFiles(async (event) => {
      for (const uri of event.files) {
        const workspaceFolder = vscode.workspace.getWorkspaceFolder(uri);
        if (!workspaceFolder) {
          continue;
        }
        await client.postFileEvent({
          workspaceRoot: workspaceFolder.uri.fsPath,
          filePath: uri.fsPath,
          eventType: "create",
          timestamp: new Date().toISOString(),
        });
      }
    }),
  );

  context.subscriptions.push(
    vscode.workspace.onDidDeleteFiles(async (event) => {
      for (const uri of event.files) {
        const workspaceFolder = vscode.workspace.getWorkspaceFolder(uri);
        if (!workspaceFolder) {
          continue;
        }
        await client.postFileEvent({
          workspaceRoot: workspaceFolder.uri.fsPath,
          filePath: uri.fsPath,
          eventType: "delete",
          timestamp: new Date().toISOString(),
        });
      }
    }),
  );

  context.subscriptions.push(
    vscode.workspace.onDidRenameFiles(async (event) => {
      for (const file of event.files) {
        const workspaceFolder = vscode.workspace.getWorkspaceFolder(file.newUri);
        if (!workspaceFolder) {
          continue;
        }
        await client.postFileEvent({
          workspaceRoot: workspaceFolder.uri.fsPath,
          filePath: file.newUri.fsPath,
          eventType: "rename",
          timestamp: new Date().toISOString(),
          metadata: { oldPath: file.oldUri.fsPath },
        });
      }
    }),
  );

  logLine("vscode-onedrive-sync-router activated.");
}

export function deactivate(): void {
  return;
}
