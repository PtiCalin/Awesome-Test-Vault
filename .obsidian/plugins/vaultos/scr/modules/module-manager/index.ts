// scr/modules/module-manager/index.ts

import { registerWatcher } from './watcher';
import { App, Plugin } from 'obsidian';

export function registerModule(app: App, plugin: Plugin) {
  console.log("✅ module-manager loaded");
  registerWatcher(app, plugin);
}
