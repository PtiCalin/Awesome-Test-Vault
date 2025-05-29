// scr/modules/module-manager/watcher.ts

import * as fs from 'fs';
import * as path from 'path';

const MODULES_DIR = "vaultos/scr/modules";

export function registerWatcher(app, plugin) {
  const fullPath = path.join(plugin.app.vault.adapter.basePath, MODULES_DIR);
  if (!fs.existsSync(fullPath)) return;

  fs.watch(fullPath, { recursive: false }, (eventType, filename) => {
    if (eventType === "rename") {
      const newModulePath = path.join(fullPath, filename);
      if (fs.existsSync(newModulePath) && fs.lstatSync(newModulePath).isDirectory()) {
        console.log(`📁 New module folder detected: ${filename}`);
        // Here: generate index.ts, README.md, wizzard.ts, config.json
        // TODO: Auto-generate using templates
      }
    }
  });
}
