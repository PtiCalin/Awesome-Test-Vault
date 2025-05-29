// scr/modules/module-manager/watcher.ts

import * as fs from 'fs';
import * as path from 'path';
import { scaffoldModule } from './scaffolder';

const MODULES_DIR = "vaultos/scr/modules";

export function registerWatcher(app: App, plugin: Plugin) {
  const fullPath = path.join(plugin.app.vault.adapter.basePath, MODULES_DIR);

  if (!fs.existsSync(fullPath)) {
    console.warn("⚠️ VaultOS modules folder not found:", fullPath);
    return;
  }

  fs.watch(fullPath, { recursive: false }, (eventType, filename) => {
    if (!filename || path.extname(filename)) return; // skip files
    if (eventType !== "rename") return; // only folder creations

    const newModulePath = path.join(fullPath, filename);
    const isDir = fs.existsSync(newModulePath) && fs.lstatSync(newModulePath).isDirectory();

    if (isDir) {
      console.log(`📦 Detected new module folder: ${filename}`);
      scaffoldModule(filename, newModulePath);
    }
  });

  console.log("👁️ Module watcher active:", fullPath);
}
