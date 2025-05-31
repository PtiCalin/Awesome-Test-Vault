-- generate_manifest.lua
-- Generates a mock Obsidian plugin manifest from metadata
-- Usage: lua generate_manifest.lua

local manifest = {
  id = "vaultos-plugin-template",
  name = "VaultOS Plugin Template",
  version = "1.0.0",
  author = "PtiCalin",
  description = "A modular starter template for building VaultOS-compatible Obsidian plugins.",
  main = "dist/main.js",
  minAppVersion = "1.0.0"
}

print("🔮 Generated Obsidian Plugin Manifest:")
print("--------------------------------------")
for k, v in pairs(manifest) do
  print(string.format("%s: %s", k, v))
end
