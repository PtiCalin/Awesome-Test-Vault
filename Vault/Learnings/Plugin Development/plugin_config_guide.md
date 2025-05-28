---
id: plugin-config-guide
title: "VaultOS Plugin Configuration Guide"
type: documentation
category: configuration
section: system
role: reference
folder: System/Documentation and Meta
tags: [vaultos, config, plugin, setup, guide, documentation]
version: 1.0
status: complete
visibility: public
created: 2025-05-28
updated: 2025-05-28
summary: "Annotated breakdown of plugin_config.json settings used by VaultOS"
parent: ""
children: []
friends: []
related: []
---

# 🧩 VaultOS Plugin Configuration – Developer Guide

This page explains the `plugin_config.json` file used by the VaultOS plugin. While JSON doesn’t allow comments, you can use this guide to understand what each setting does and customize your plugin behavior accordingly.

---

## 🧠 General Info

| Key         | Description                                   |
|-------------|-----------------------------------------------|
| `pluginName` | Name of the plugin (`VaultOS`)               |
| `version`    | Current version number                       |
| `description`| Plugin summary                               |
| `author`     | You! The creator(s)                          |
| `enabled`    | Boolean flag to toggle the plugin globally   |

---

## 📦 Module Flags

Each section of VaultOS is modular. Toggle entire sections on/off with simple `true` or `false` values.

### `core`
Essential engine components of VaultOS.

- `folderScaffolding`: Auto-create vault folder structure
- `folderNoteDashboards`: Enables folder-name.md dashboards
- `backendRefractor`: Redirect .obsidian config to System
- `animatedHomepage`: Loads animated entry screen
- `yamlInjector`: Populates standardized YAML blocks
- `autoLogger`: Tracks vault events, actions, and reflections

### `filesAndMedia`
For organizing multimedia assets.

- `mediaSorting`: Subcategorize media types
- `mediaDashboard`: Local media MOC
- `dataviewIntegration`: Surfacing tagged or recent items

### `notes`
Block injection and modular note enhancement.

- `blockEngine`: Enables block insertion UI
  - `brainDump`, `events`, `goals`, `habit`, `reflection`, `quote`, `question`, `task`

### `learnings`
Track personal growth and structured learning.

- `progressTracker`: Shows vault learning progress
- `skillTree`: Visualize and manage skills
- `nuggetBank`: Nugget currency system

### `system`
Scripting engine and advanced automation.

- `scaffoldGenerator`: CLI-based folder generator
- `configMigrator`: Moves settings to VaultOS System
- `pluginManager`: Loads/unloads VaultOS modules
- `animationBundler`: HUD + homepage animations
- `summarizerGo`: Markdown summarizer (Go)
- `validatorElixir`: YAML + link hygiene tool (Elixir)
- `mapGenLua`: Directory tree visualizer (Lua)
- `analyticsR`: Vault metadata dashboard (R)

---

## 🏛️ Gamified & Narrative

- `museumOfSelf`: Unlockable rooms based on note activity
- `trophyEngine`: Achievement tracking system
- `progressMirror`: Animated visual bar of module activity
- `unlockables`: Hidden snippets, surprise visuals, and more

---

## 🎲 Whimsical Utilities

- `diceRoller`: Multi-dice animation module
- `cardDraw`: Tarot + poker draw system
- `nameGenerator`: Procedural name generation

---

## 🎨 UI Helpers

- `hud`: HUD toggle
- `stylesCss`, `variablesCss`, `snippetsCss`: Loads helper styles
- `styleGuideMd`: Documentation for visual consistency

---

## ⚙️ Default Settings

These settings define how VaultOS operates globally.

- `vaultRoot`: Path to your vault root (ex: `VAULT`)
- `useDataview`: Enables Dataview integration
- `logFile`: Where plugin logs are stored
- `defaultHomepage`: Sets the homepage location
- `defaultYAMLVersion`: Frontmatter format version
