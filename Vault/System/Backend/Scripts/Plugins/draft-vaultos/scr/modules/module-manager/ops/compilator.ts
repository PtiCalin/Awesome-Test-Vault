// scr/modules/module-manager/ops/compilator.ts

import * as fs from 'fs';
import * as path from 'path';
import { getModuleMetadata } from '../cache';

export function compileManifest(manifestPath: string = "vaultos/manifest.json") {
  const metadata = getModuleMetadata();
  const output = {
    generated: new Date().toISOString(),
    modules: metadata
  };

  fs.writeFileSync(path.resolve(manifestPath), JSON.stringify(output, null, 2));
  console.log("📦 VaultOS manifest compiled.");
}
