declare module "vscode" {
  export interface Disposable {
    dispose(): void;
  }

  export enum StatusBarAlignment {
    Left = 1,
    Right = 2,
  }

  export interface OutputChannel extends Disposable {
    appendLine(value: string): void;
    show(preserveFocus?: boolean): void;
  }

  export interface StatusBarItem extends Disposable {
    text: string;
    tooltip?: string;
    command?: string;
    show(): void;
  }

  export interface Uri {
    fsPath: string;
  }

  export interface TextDocument {
    uri: Uri;
    languageId: string;
    getText(): string;
  }

  export interface WorkspaceFolder {
    uri: Uri;
  }

  export interface ExtensionContext {
    subscriptions: Disposable[];
    secrets: {
      get(key: string): Promise<string | undefined>;
      store(key: string, value: string): Promise<void>;
    };
  }

  export interface FileRenameEvent {
    files: Array<{ oldUri: Uri; newUri: Uri }>;
  }

  export interface FileEventCollection {
    files: Uri[];
  }

  export interface WindowApi {
    activeTextEditor?: { document: TextDocument };
    createOutputChannel(name: string): OutputChannel;
    createStatusBarItem(alignment: StatusBarAlignment, priority?: number): StatusBarItem;
    showInformationMessage(message: string): Promise<string | undefined>;
  }

  export interface ConfigurationApi {
    get<T>(key: string, defaultValue?: T): T;
  }

  export interface WorkspaceApi {
    getConfiguration(section: string): ConfigurationApi;
    getWorkspaceFolder(uri: Uri): WorkspaceFolder | undefined;
    onDidSaveTextDocument(listener: (document: TextDocument) => unknown): Disposable;
    onDidCreateFiles(listener: (event: FileEventCollection) => unknown): Disposable;
    onDidDeleteFiles(listener: (event: FileEventCollection) => unknown): Disposable;
    onDidRenameFiles(listener: (event: FileRenameEvent) => unknown): Disposable;
  }

  export interface CommandsApi {
    registerCommand(command: string, callback: (...args: unknown[]) => unknown): Disposable;
    executeCommand<T = unknown>(command: string, ...rest: unknown[]): Promise<T>;
  }

  export const window: WindowApi;
  export const workspace: WorkspaceApi;
  export const commands: CommandsApi;
}