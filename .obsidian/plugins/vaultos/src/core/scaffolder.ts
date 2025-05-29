// scr/modules/module-manager/scaffolder.ts

import * as fs from 'fs';
import * as path from 'path';
import { logModuleAction } from './logger';
import { updateModuleCache } from './cache';
import { ensureDir } from './utils/file';

const TEMPLATE_DIR = "vaultos/scr/modules/module-manager/templates";

const defaultFiles = [
  { name: "index.ts", template: "index.ts.hbs" },
  { name: "manifest.json", template: "manifest.json.hbs" },
  { name: "styles.css", template: "styles.css.hbs" },
  { name: "settings.ts", template: "settings.ts.hbs" },
  { name: "commands.ts", template: "commands.ts.hbs" },
  { name: "views.ts", template: "views.ts.hbs" },
  { name: "automations.ts", template: "automations.ts.hbs" },
  { name: "utils/file.ts", template: "file.ts.hbs" },
  { name: "utils/http.ts", template: "http.ts.hbs" },
  { name: "utils/obsidian.ts", template: "obsidian.ts.hbs" },
  { name: "wizzard.ts", template: "wizzard.ts.hbs" },
  { name: "README.md", template: "README.md.hbs" },
  { name: "config/config.json", template: "config.json.hbs" },
  { name: "assets/assets.json", template: "assets.json.hbs" }
];

export function scaffoldModule(moduleName: string, modulePath: string) {
  const createdFiles: string[] = [];

  for (const file of defaultFiles) {
    const fullPath = path.join(modulePath, file.name);
    const templatePath = path.join(TEMPLATE_DIR, file.template);

    // Create config folder if needed
    ensureDir(path.dirname(fullPath));

    // Skip if file already exists
    if (!fs.existsSync(fullPath)) {
      let content = fs.readFileSync(templatePath, 'utf-8');
      content = content.replace(/{{MODULE-NAME}}/g, moduleName);
      content = content.replace(/{{CREATED_DATE}}/g, new Date().toISOString());
      fs.writeFileSync(fullPath, content);
      createdFiles.push(file.name);
    }
  }

  // Log creation
  logModuleAction({
    action: "scaffold",
    module: moduleName,
    trigger: "watcher",
    result: createdFiles.length > 0 ? "success" : "skipped",
    filesCreated: createdFiles
  });

  // Update metadata
  updateModuleCache(moduleName, {
    enabled: true,
    status: "ok",
    path: modulePath,
    created: new Date().toISOString(),
    files: createdFiles
  });
}
