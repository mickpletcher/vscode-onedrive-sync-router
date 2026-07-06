import * as vscode from "vscode";

let outputChannel: vscode.OutputChannel | undefined;

export function getOutputChannel(): vscode.OutputChannel {
  if (!outputChannel) {
    outputChannel = vscode.window.createOutputChannel("vscode-onedrive-sync-router");
  }
  return outputChannel;
}

export function logLine(message: string): void {
  getOutputChannel().appendLine(message);
}
