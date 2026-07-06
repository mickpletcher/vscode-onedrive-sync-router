import * as vscode from "vscode";

const SECRET_KEY = "vscode-onedrive-sync-router.sharedSecret";

export async function getSharedSecret(context: vscode.ExtensionContext): Promise<string> {
  return context.secrets.get(SECRET_KEY).then((value) => value ?? "");
}

export async function setSharedSecret(context: vscode.ExtensionContext, secret: string): Promise<void> {
  await context.secrets.store(SECRET_KEY, secret);
}
