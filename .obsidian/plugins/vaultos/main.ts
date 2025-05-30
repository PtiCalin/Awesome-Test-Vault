import { Plugin } from "obsidian";
import { registerWatcher } from "./src/core/watcher";
import { registerModuleManagerView, VaultOSPanelView, VAULTOS_PANEL_VIEW } from "./src/core/view";
import { logModuleAction } from "./src/core/logger";
import { updateModuleCache } from "./src/core/cache";
import { compileManifest } from "./src/ops/compilator";

export default class VaultOSPlugin extends Plugin {
  async onload() {
    console.log("🧠 VaultOS kernel loaded");

    // Register file watcher to detect new subplugin folders
    registerWatcher(this.app, this);

    // Register VaultOS control panel view
    registerModuleManagerView(this.app);

    // 🔲 Open VaultOS panel in the left sidebar
    const leaf = (this as any).app.workspace.getLeftLeaf(false);
    await leaf.setViewState({
      type: VAULTOS_PANEL_VIEW,
      active: true,
    });

    // Initial metadata caching
    updateModuleCache("vaultos", {
      enabled: true,
      status: "active",
      description: "VaultOS plugin orchestrator kernel",
      loadedAt: new Date().toISOString()
    });

    // Optional: compile manifest at launch
    compileManifest();

    // Log the plugin start
    logModuleAction({
      action: "vaultos-load",
      module: "vaultos",
      result: "success",
      notes: "VaultOS loaded and watching for subplugins"
    });
  }

  async onunload() {
    console.log("💤 VaultOS kernel unloaded");

    logModuleAction({
      action: "vaultos-unload",
      module: "vaultos",
      result: "success",
      notes: "VaultOS was deactivated"
    });
  }
}
