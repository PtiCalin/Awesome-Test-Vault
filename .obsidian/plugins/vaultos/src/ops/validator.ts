// scr/modules/module-manager/ops/validator.ts

import * as fs from 'fs';
import * as path from 'path';

const REQUIRED_FILES = ['index.ts', 'wizzard.ts', 'README.md', 'config/config.json'];

export function validateModuleStructure(modulePath: string): string[] {
  const missing = [];

  for (const relPath of REQUIRED_FILES) {
    const filePath = path.join(modulePath, relPath);
    if (!fs.existsSync(filePath)) {
      missing.push(relPath);
    }
  }

  return missing;
}
