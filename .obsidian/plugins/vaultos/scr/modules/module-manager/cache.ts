// scr/modules/module-manager/cache.ts

import * as fs from 'fs';
import * as path from 'path';
import { ensureDir } from './utils/file';

const CACHE_FILE = "vaultos/scr/modules/module-manager/data/module-metadata.json";

function getCachePath(): string {
  return path.resolve(CACHE_FILE);
}

function readCache(): Record<string, any> {
  const fullPath = getCachePath();
  if (!fs.existsSync(fullPath)) return {};
  return JSON.parse(fs.readFileSync(fullPath, 'utf-8'));
}

function writeCache(data: Record<string, any>) {
  ensureDir(path.dirname(getCachePath()));
  fs.writeFileSync(getCachePath(), JSON.stringify(data, null, 2));
}

/**
 * Updates or creates the metadata entry for a given module
 */
export function updateModuleCache(moduleName: string, metadata: Record<string, any>) {
  const cache = readCache();

  cache[moduleName] = {
    ...(cache[moduleName] || {}),
    ...metadata,
    lastUpdated: new Date().toISOString()
  };

  writeCache(cache);
}

/**
 * Returns the full module metadata cache
 */
export function getModuleMetadata(): Record<string, any> {
  return readCache();
}

/**
 * Returns metadata for a specific module
 */
export function getSingleModule(moduleName: string): Record<string, any> | null {
  const cache = readCache();
  return cache[moduleName] || null;
}
/**
 * Deletes a module's metadata from the cache
 */
export function deleteModuleCache(moduleName: string) {
  const cache = readCache();
  if (cache[moduleName]) {
    delete cache[moduleName];
    writeCache(cache);
  }
}
