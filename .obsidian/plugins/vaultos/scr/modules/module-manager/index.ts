// scr/modules/module-manager/index.ts

import { App, Plugin } from 'obsidian';
import { registerWatcher } from './watcher';
import { updateModuleCache } from './cache';
import { logModuleAction } from './logger';

export function registerModule(app: App, plugin: Plugin) {
  console.log("🧠 VaultOS Module Manager loaded");

  // Watch for new module folders
  registerWatcher(app, plugin);

  // Initial log
  logModuleAction({
    action: "module-manager-init",
    module: "module-manager",
    result: "success",
    notes: "Module manager booted and watcher activated"
  });

  // Optional: update own metadata in cache
  updateModuleCache("module-manager", {
    enabled: true,
    status: "active",
    description: "Handles scaffolding, caching, and logging for all VaultOS modules"
  });

  // Placeholder: Register view panel (future)
  // plugin.registerView(VIEW_TYPE, () => new ModuleManagerView(...));
}
