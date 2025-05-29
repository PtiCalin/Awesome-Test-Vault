// scr/modules/module-manager/view.ts

import { ItemView, WorkspaceLeaf, TFile } from "obsidian";
import { getModuleMetadata } from "./cache";

export const MODULE_MANAGER_VIEW = "vaultos-module-manager";

export class ModuleManagerView extends ItemView {
  constructor(leaf: WorkspaceLeaf) {
    super(leaf);
  }

  getViewType(): string {
    return MODULE_MANAGER_VIEW;
  }

  getDisplayText(): string {
    return "🧠 VaultOS Modules";
  }

  async onOpen() {
    const container = this.containerEl.children[1];
    container.empty();

    const metadata = getModuleMetadata();
    container.createEl("h2", { text: "🧩 VaultOS Modules" });

    const table = container.createEl("table", { cls: "vaultos-modules-table" });
    const thead = table.createTHead();
    const headerRow = thead.insertRow();
    ["Module", "Enabled", "Status", "Config"].forEach(header =>
      headerRow.insertCell().textContent = header
    );

    const tbody = table.createTBody();
    Object.entries(metadata).forEach(([name, data]) => {
      const row = tbody.insertRow();
      row.insertCell().textContent = name;
      row.insertCell().textContent = data.enabled ? "✅" : "❌";
      row.insertCell().textContent = data.status || "unknown";

      const configBtn = row.insertCell().createEl("button", { text: "Open" });
      configBtn.onclick = () => this.openConfigFile(data.path);
    });
  }

  async openConfigFile(modulePath: string) {
    const filePath = `${modulePath}/config/config.json`;
    const file = this.app.vault.getAbstractFileByPath(filePath);
    if (file instanceof TFile) {
      this.app.workspace.getLeaf(true).openFile(file);
    } else {
      new Notice(`⚠️ Config not found: ${filePath}`);
    }
  }

  async onClose() {
    // Cleanup if needed
  }
}
export function registerModuleManagerView(app: App) {
  app.workspace.registerView(
    MODULE_MANAGER_VIEW,
    (leaf) => new ModuleManagerView(leaf)
  );

  console.log("🧠 VaultOS Module Manager view registered");
}
