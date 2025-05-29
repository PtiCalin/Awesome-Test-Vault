// scr/modules/module-manager/logger.ts

import * as fs from 'fs';
import * as path from 'path';
import { ensureDir } from './utils/file';

const LOG_FILE = "vaultos/scr/modules/module-manager/data/module-log.jsonl";

function getLogPath(): string {
  return path.resolve(LOG_FILE);
}

/**
 * Logs a single action to the JSONL log
 */
export function logModuleAction(entry: Record<string, any>) {
  const fullPath = getLogPath();
  ensureDir(path.dirname(fullPath));

  const logEntry = {
    timestamp: new Date().toISOString(),
    ...entry
  };

  fs.appendFileSync(fullPath, JSON.stringify(logEntry) + "\n");
}

/**
 * Optional: Read the last N entries from the log
 */
export function readModuleLog(limit: number = 100): Record<string, any>[] {
  const fullPath = getLogPath();
  if (!fs.existsSync(fullPath)) return [];

  const lines = fs.readFileSync(fullPath, 'utf-8').trim().split('\n');
  const recent = lines.slice(-limit);

  return recent.map(line => {
    try {
      return JSON.parse(line);
    } catch {
      return { error: "Malformed log entry" };
    }
  });
}
