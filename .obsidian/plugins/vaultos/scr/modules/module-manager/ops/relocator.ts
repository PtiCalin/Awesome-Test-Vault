// scr/modules/module-manager/ops/relocator.ts

import * as fs from 'fs';
import * as path from 'path';
import { ensureDir } from '../utils/file';

export function relocateModuleJson(moduleName: string, jsonData: Record<string, any>) {
  const outPath = path.resolve("vaultos/dist/modules", moduleName);
  ensureDir(outPath);
  fs.writeFileSync(path.join(outPath, `${moduleName}.json`), JSON.stringify(jsonData, null, 2));
}
