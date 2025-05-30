# 🧠 VaultOS

**VaultOS** is a self-extending plugin management and operations system for Obsidian.

It acts as the **central kernel** of a modular plugin ecosystem built around **VaultOS-subplugins** — lightweight feature modules that can be scaffolded, enabled, updated, and orchestrated by VaultOS itself.

---

## 🚀 What It Does

- 🏗️ **Scaffold** new VaultOS subplugins with a full plugin template
- 🧠 **Cache** and track all enabled subplugins with live metadata
- 📦 **Validate**, **convert**, and **relocate** plugin data into `.json` packages
- 🔄 **Orchestrate** full build pipelines across all subplugins
- 📡 **(Coming Soon)**: Download subplugins remotely from GitHub
- 🪟 Manage everything through a **VaultOS Control Panel**

---

## 🧩 What Is a VaultOS Subplugin?

A VaultOS subplugin is a mini-plugin folder prefixed with:

```txt
.obsidian/plugins/vaultos_<moduleName>
```

Each subplugin is self-contained and may include:

```txt
vaultos_myplugin/
├── index.ts
├── wizzard.ts
├── config/
│   └── config.json
├── views.ts
├── automations.ts
├── utils/
├── manifest.json
└── README.md
```

---

## 📂 VaultOS Structure

```txt
.obsidian/plugins/vaultos/
├── main.ts                → VaultOS plugin entry
├── manifest.json          → Obsidian plugin declaration
├── src/
│   ├── core/              → cache, logger, watcher, scaffolder
│   ├── ops/               → converter, relocator, validator, orchestrator
│   ├── ui/                → Module Manager view
│   ├── templates/         → Subplugin scaffolding blueprints
│   └── utils/             → Shared logic (fs, http, obsidian)
├── config/                → VaultOS plugin configuration
└── dist/                  → Compiled plugin output
```

---

## ⚙️ Core Features

| Feature | Description |
|--------|-------------|
| 🔁 Watcher | Detects new `vaultos_*` folders in `.obsidian/plugins` |
| 🧱 Scaffolder | Generates all needed files from templates |
| 📓 Logger | Appends creation events to `.jsonl` log |
| 🧠 Cache | Stores metadata about all subplugins |
| 🔨 Orchestrator | Validates → Converts → Relocates → Compiles |
| 🧩 View | VaultOS UI to see/manage modules (toggle, open config, etc.) |

---

## 🧪 Commands

- `VaultOS: Scaffold New Subplugin`
- `VaultOS: Run Build Pipeline`
- `VaultOS: Open Module Manager Panel`
- `VaultOS: Refresh Module Metadata`

(To be registered in upcoming releases.)

---

## ✨ Roadmap

- [ ] Remote subplugin downloads
- [ ] Auto-update + changelog detection
- [ ] Subplugin marketplace registry
- [ ] Live dashboard stats + activity tracker
- [ ] Developer tools for linting / packaging

---

## 👩‍💻 Credits

Built with love by [@PtiCalin](https://github.com/PtiCalin)  
Engineered for self-growing minds 🧠✨
