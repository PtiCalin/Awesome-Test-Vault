// 🧠 Dev Typings for Obsidian API (Stub)
// This file is used to allow development of Obsidian plugins
// without the actual `obsidian` module present during compilation.

declare module 'obsidian' {
    
  // Plugin System
 
  export class Plugin {
    app: App;
    addCommand(options: {
      id: string;
      name: string;
      callback: () => void;
    }): void;
    // Optional lifecycle hooks
    onload?(): void;
    onunload?(): void;
  }


  // App & Vault API

  export interface App {
    vault: Vault;
  }

  export class Vault {
    createFolder(path: string): Promise<void>;
    create(path: string, data: string): Promise<void>;
    getAbstractFileByPath(path: string): AbstractFile | null;
  }

  export interface AbstractFile {}

 
  // File System Types         

  export interface TFolder extends AbstractFile {
    children: AbstractFile[];
    name: string;
    path: string;
  }
}
