declare module "obsidian" {
  export interface App {
    workspace: Workspace;
  }

  export interface Workspace {
    getLeftLeaf(create: boolean): WorkspaceLeaf;
  }

  export interface WorkspaceLeaf {
    setViewState(state: ViewState): Promise<void>;
  }

  export interface ViewState {
    type: string;
    active: boolean;
  }
}
declare module "obsidian" {
  export interface Plugin {
    app: App;
    onunload(): void;
    onload(): void;
  }

  export interface PluginManifest {
    id: string;
    name: string;
    version: string;
    description?: string;
    author?: string;
  }
}