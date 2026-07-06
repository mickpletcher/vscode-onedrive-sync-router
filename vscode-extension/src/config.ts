import * as vscode from "vscode";

export interface ExtensionConfiguration {
  agentUrl: string;
  sharedSecret: string;
}

export function getExtensionConfiguration(): ExtensionConfiguration {
  const configuration = vscode.workspace.getConfiguration("vscode-onedrive-sync-router");
  return {
    agentUrl: configuration.get<string>("agentUrl", "http://127.0.0.1:8765"),
    sharedSecret: configuration.get<string>("sharedSecret", ""),
  };
}
