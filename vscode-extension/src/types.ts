export type FileEventType = "create" | "modify" | "delete" | "rename";

export interface FileEventPayload {
  workspaceRoot: string;
  filePath: string;
  eventType: FileEventType;
  timestamp: string;
  revision?: string;
  size?: number;
  mtimeNs?: number;
  metadata?: Record<string, unknown>;
}

export interface AgentQueueItem {
  id: number;
  workspace_root: string;
  file_path: string;
  event_type: string;
  status: string;
  dedupe_key: string;
  payload: Record<string, unknown>;
  created_at: string;
  updated_at: string;
  attempts: number;
  available_at?: string | null;
  last_error?: string | null;
}

export interface AgentStatus {
  service: string;
  mode: string;
  queue: Record<string, number>;
}
