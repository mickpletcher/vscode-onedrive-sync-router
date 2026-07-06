import * as vscode from "vscode";

import type { AgentQueueItem, AgentStatus, FileEventPayload } from "./types";

export class AgentClient {
  public constructor(private readonly agentUrl: string, private readonly sharedSecret: string) {}

  private buildHeaders(): HeadersInit {
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
    };

    if (this.sharedSecret) {
      headers["X-Sync-Router-Token"] = this.sharedSecret;
    }

    return headers;
  }

  public async getStatus(): Promise<AgentStatus | undefined> {
    const response = await fetch(`${this.agentUrl}/status`, { headers: this.buildHeaders() });
    if (!response.ok) {
      return undefined;
    }
    return (await response.json()) as AgentStatus;
  }

  public async getQueueItems(): Promise<AgentQueueItem[]> {
    const response = await fetch(`${this.agentUrl}/queue`, { headers: this.buildHeaders() });
    if (!response.ok) {
      return [];
    }
    const body = (await response.json()) as { items?: AgentQueueItem[] };
    return body.items ?? [];
  }

  public async postFileEvent(payload: FileEventPayload): Promise<boolean> {
    const response = await fetch(`${this.agentUrl}/events`, {
      method: "POST",
      headers: this.buildHeaders(),
      body: JSON.stringify(payload),
    });
    return response.ok;
  }

  public async sendDocumentEvent(document: vscode.TextDocument, eventType: FileEventPayload["eventType"]): Promise<boolean> {
    const workspaceFolder = vscode.workspace.getWorkspaceFolder(document.uri);
    if (!workspaceFolder) {
      return false;
    }

    return this.postFileEvent({
      workspaceRoot: workspaceFolder.uri.fsPath,
      filePath: document.uri.fsPath,
      eventType,
      timestamp: new Date().toISOString(),
      size: document.getText().length,
      metadata: {
        languageId: document.languageId,
      },
    });
  }
}
