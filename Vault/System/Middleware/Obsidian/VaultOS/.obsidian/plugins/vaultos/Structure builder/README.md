# 🧱 Vault Structure Builder

This is an Obsidian community plugin designed to scaffold a clean, modular folder structure for VaultOS-based vaults.

---

## 🚀 Setup Instructions

### 📁 1. Install the Plugin
Place the extracted plugin folder here:

```
<YourVault>/.obsidian/plugins/vault-structure-builder/
```

---

### 🧰 2. Build the Plugin

Open a terminal and navigate to the plugin folder:

```bash
cd "<YourVault>/.obsidian/plugins/vault-structure-builder"
npm install
npm run build
```

If successful, this will output:
```
dist/main.js  ✅
```

> This script automatically avoids bundling the Obsidian API (`--external:obsidian`).

---

### ⚙️ 3. Enable the Plugin

1. Open Obsidian
2. Go to `Settings → Community Plugins`
3. Enable **Vault Structure Builder**

---

### 💡 4. Use It!

Open the Command Palette (Ctrl+P or Cmd+P) and search for:

```
🧱 Generate Vault Structure
```

This will:

- Scaffold a full `VAULT/` directory structure
- Place `.md` folder notes in each directory
- Insert your default `Standard Page Template`

---

## 🔌 Advanced CLI Tool

In `VAULT/System/Backend/Scripts/`, there's also:

```
vault-like-structure.sh
```

You can run this manually for more advanced use:

```bash
./vault-like-structure.sh MyProject --obsidian --dry-run
```

This supports:

- 🧪 Dry run preview
- 📂 Presets: `--preset standard`, `learning`, `dev`, `world`
- 🧠 Obsidian config migration

---

Created with ❤️ by PtiCalin · Built for VaultOS ⚙️
