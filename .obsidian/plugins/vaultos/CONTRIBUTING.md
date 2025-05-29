# 🤝 Contributing to VaultOS

Thank you for your interest in contributing to **VaultOS** — the modular plugin orchestrator for Obsidian! 🎉

Whether you're a seasoned Obsidian plugin dev or just getting started, you're welcome here.

---

## 🧩 VaultOS Philosophy

VaultOS is a core plugin that manages, extends, and coordinates small feature-based **subplugins** called `vaultos_<moduleName>`.

These subplugins live in `.obsidian/plugins/` and are scaffolded + managed by VaultOS itself.

---

## 📦 What You Can Contribute

- 🧱 New subplugin templates (`templates/`)
- ⚙️ Core improvements (`src/core/`, `src/ops/`)
- 🧩 Subplugin ideas, UX flows, config schemas
- 📄 Docs: README, tutorials, subplugin examples
- 🪟 UI enhancements to the control panel
- 🐛 Bug reports and feature requests

---

## 🛠 Project Structure

```
.obsidian/plugins/vaultos/
├── main.ts                → Entry point
├── manifest.json          → Plugin metadata
├── src/
│   ├── core/              → watcher, cache, logger, etc.
│   ├── ops/               → converter, relocator, validator
│   ├── ui/                → control panel view
│   ├── utils/             → file + obsidian helpers
│   └── templates/         → subplugin blueprints
└── config/
```

---

## 🧪 Local Dev Workflow

1. Clone the repository into your Obsidian vault:
   ```
   .obsidian/plugins/vaultos/
   ```

2. Install dependencies and build:
   ```
   npm install
   npm run build
   ```

3. Open Obsidian → Enable VaultOS plugin

4. Test by creating `.obsidian/plugins/vaultos_<yourSubplugin>` and watching VaultOS scaffold it

---

## ✍️ Style & Conventions

- Use consistent naming: `vaultos_<module-name>`
- Keep functions small and single-purpose
- Prefer filesystem-neutral paths (`path.join`, `fs.existsSync`)
- Include timestamps where relevant
- Log meaningful actions (`logger.ts`)

---

## 🌍 Community

If you're unsure how to get started or want to pitch an idea:

- Open an issue
- Propose a new subplugin scaffold
- Share feedback on the Module Manager UI

---

## 💜 Thank You

VaultOS is being built as a tool for modular thinking, dynamic creativity, and vault-native workflows.

Thank you for helping shape its future 🙏
