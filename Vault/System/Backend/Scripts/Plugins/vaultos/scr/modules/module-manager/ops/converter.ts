// scr/modules/module-manager/ops/converter.ts

import * as fs from 'fs';
import * as path from 'path';

export function convertModuleToJson(moduleName: string, modulePath: string): Record<string, any> {
  const configPath = path.join(modulePath, 'config', 'config.json');
  const output = {
    module: moduleName,
    config: null,
    timestamp: new Date().toISOString()
  };

  if (fs.existsSync(configPath)) {
    output.config = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
  } else {
    output.config = { error: "Missing config.json" };
  }

  return output;
}
