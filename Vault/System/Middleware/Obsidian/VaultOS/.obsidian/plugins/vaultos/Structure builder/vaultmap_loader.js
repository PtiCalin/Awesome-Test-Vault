/**
 * Inject VaultMap for dataviewjs
 */
async function cJS() {
  const module = await import("VaultMap.js");
  return module;
}