// scr/modules/module-manager/ops/orchestrator.ts

import * as path from 'path';
import { validateModuleStructure } from './validator';
import { convertModuleToJson } from './converter';
import { relocateModuleJson } from './relocator';
import { compileManifest } from './compilator';
import { logModuleAction } from '../logger';
import { updateModuleCache } from '../cache';
import * as fs from 'fs';

const MODULES_DIR = "vaultos/scr/modules";

/**
 * Run full build pipeline on a single module
 */
export function runModuleBuildPipeline(moduleName: string) {
  const modulePath = path.resolve(MODULES_DIR, moduleName);

  if (!fs.existsSync(modulePath)) {
    console.warn("❌ Module folder does not exist:", modulePath);
    return;
  }

  // 1. Validate
  const missing = validateModuleStructure(modulePath);
  if (missing.length > 0) {
    console.warn(`⚠️ Module '${moduleName}' is missing files:`, missing);
    logModuleAction({
      action: "validate",
      module: moduleName,
      result: "failed",
      missing
    });
    return;
  }

  // 2. Convert
  const jsonData = convertModuleToJson(moduleName, modulePath);

  // 3. Relocate
  relocateModuleJson(moduleName, jsonData);

  // 4. Update cache
  updateModuleCache(moduleName, {
    compiled: true,
    lastCompiled: new Date().toISOString()
  });

  // 5. Log success
  logModuleAction({
    action: "build-pipeline",
    module: moduleName,
    result: "success",
    filesExported: [`dist/modules/${moduleName}/${moduleName}.json`]
  });

  console.log(`✅ Build pipeline completed for: ${moduleName}`);
}

/**
 * Run build pipeline on all existing modules
 */
export function runFullBuildPipeline() {
  const modules = fs.readdirSync(path.resolve(MODULES_DIR), { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name);

  modules.forEach(runModuleBuildPipeline);

  // Recompile full manifest
  compileManifest();
}
