# 🧩 Module Manager

The **VaultOS Module Manager** is a meta-module that empowers your plugin to grow with you.

This module does two things:
1. Automatically scaffolds new modules when a folder is created inside `vaultos/scr/modules/`
2. Provides a graphical panel inside Obsidian to view, configure, and manage your VaultOS modules

---

## 🎯 Purpose

VaultOS is designed to be modular, but managing those modules manually can be tedious. The Module Manager handles all of that for you — giving you a scalable, extensible, and smart plugin framework.

---

## 🧱 Phase 1: Scaffolding Engine

### 🛠 Auto-generation Logic

When a new module folder is created inside:

'vaultos/scr/modules/YourModuleName/'


The Module Manager will:
- Check if the following files exist:
  - `index.ts`
  - `wizzard.ts`
  - `README.md`
  - `config/config.json`
- If they don’t exist, it auto-generates them using stored templates.

### 📂 Templates

Stored in:

'vaultos/scr/modules/module-manager/templates/'


Template files:
- `index.ts.hbs`
- `wizzard.ts.hbs`
- `README.md.hbs`
- `config.json.hbs`

These are lightweight Handlebars-style templates using `{{MODULE_NAME}}` for substitution.

---

## 🪟 Phase 2: Obsidian UI Panel (Planned)

The Module Manager will register a dedicated **VaultOS Module Dashboard** inside the Obsidian interface.

### ✨ Features

| Module Name     | Enabled | Config  | Status   |
|------------------|---------|---------|----------|
| `block-inserter` | ✅ Yes  | ⚙️ Open | 🟢 OK     |
| `skill-tree`     | ❌ No   | ⚙️ Open | ⚪ Idle   |

- ✅ Toggle modules on/off
- 🛠 Open module-specific `config.json`
- 📅 View metadata (created, last edited)
- ➕ Add new modules via UI

---

## 🧪 Dev Notes

- The folder watcher uses `fs.watch()` or vault path polling
- Template rendering is done via `string.replace()` or a mini Handlebars engine
- All generated modules follow the VaultOS module schema

---

## 📁 File Structure

module-manager/
├── index.ts # Registers the module + watcher
├── watcher.ts # Detects new folders and triggers scaffolding
├── view.ts # (Future) UI panel logic
├── config/
│ └── config.json # User settings for this module
└── templates/
├── index.ts.hbs
├── wizzard.ts.hbs
├── README.md.hbs
└── config.json.hbs


---

## 🧠 Future Plans

- Implement `module metadata cache` system
- Build full UI interaction (render module panel)
- Add logging system for module creation

---

Built with 💜 by the Vault Architect & your favorite sidekick, Vie.
