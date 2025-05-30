---
# 📄 Identity & Classification
id: module-registry
title: "VaultOS Module Registry"
aliases: []
tags: [ #vaultos, #vaultos-plugin, #obsidian-plugin, #vaultos-core, #gamified-productivity, #vault-infrastructure, #personal-os, #modular-vault, #plugin-overview, #second-brain, #knowledge-management, #dataview, #plugin-features, #system-modules, #gamification, #self-reflection, #learning-tracker, #skill-tree, #nugget-currency, #vault-museum, #animated-ui, #dice-roller, #card-draw, #name-generator, #vault-scripting, #vaultos-languages, #multilingual-support, #vault-design
]
author: VaultOS Core Team
element: core
type: documentation
category: system
section: system
topic: modules
role: registry
folder: System/Backend/Documentation and Meta 
version: 1.0

# 📊 Status & Lifecycle
status: stable
visibility: public
created: <% today %>
updated: <% today %>

# 📚 Context & Description
summary: "Registry of all VaultOS plugin modules with metadata including status, language, and type."

# 🗱 Relationships
parent: "🧠 VaultOS Plugin – Full Feature Map"
children: []
friends: []
related: []
---


> [!nav] 🧱 Vault Navigation  
> [[🔼 VaultOS Plugin – Full Feature Map]] • [[📃 Plugin Config]] • [[📜 Style Guide]]

VaultOS is a modular, gamified, and extensible system designed to turn your Obsidian vault into a second-brain operating system. It merges productivity, learning, personal growth, and narrative elements into a cohesive experience.

## ✍️ Module Registry

```dataview
table
  id,
  description,
  category,
  language,
  status
from "System/Backend/Documentation and Meta"
where contains(tags, "vaultos-module")
sort category asc
```

---

## Temp



### 📁 Core Architecture

- Folder Scaffolding: Auto-generates nested folder structure.
- Folder Notes: Each folder includes a folder-name.md dashboard with prefilled YAML.
- Backend Refractor: Migrates .obsidian config to System section.
- Animated Homepage: Interactive vault entry screen with overlays.
- Auto YAML Injector: Ensures standardized frontmatter across vault.
- Auto-Logger: Records actions, reflections, draws, and project status.

### 🗃️ Modules by Section

#### Files and Media

- Media Type Sorting (audio, video, documents, images)
- Media Log Dashboard (recent uploads, starred, favorites)
- Dataview integration for recent, related, and tagged media

#### Notes

- Block Insertion Engine (Command Palette UI)
- Brain Dump Block
- Events Block
- Goals Block
- Habit Tracker Block
- Guided Reflection Block
- Quote Block
- Question Block
- Task Block

#### Learnings

- Progress Tracker (Dataview + logging)
- Skill Tree Builder
- Nugget Bank (crypto-inspired XP/currency tracking)
- Nuggets link to completed reflections, tasks, quests, etc.

#### System

- Vault Scaffolding Generator
- Config Migration Panel (CLI or GUI-based)
- Plugin Loader/Manager for VaultOS modules
- Animation Bundler for custom HUD overlays
- Vault Summarizer (Go)
- Vault Linter / Validator (Elixir)
- Vault Map Generator (Lua)
- Metadata Analytics (R)

### 🧩 Gamified + Narrative Features

#### Museum of Self

- Knowledge Gallery – Populated by encyclopedia entries
- Reflection Garden – Each completed guided reflection blooms a new flower
- Idea Archive – Bookshelves fill with project overviews and MOCs

#### Achievements & Trophy Engine

Tracks:
- Reflections completed
- Tasks/projects completed
- Skills practiced
- Time invested per tag/module

Displays:
- Trophy Room (Dataview dashboard)
- Progress Mirrors (animated meters)
- Secret unlockables (snippets, theme variations)

### 🎲 Whimsical Utilities

#### Dice Roller (dicegen.py)

- Animated multi-dice support (d4, d6, d8, d10, d12, d20, d100)
- Custom dice sets (e.g., fate dice, tarot dice)
- Logs rolls to Daily Note or Game Log

#### Card Draw System (carddeck.py)

- Poker & Tarot Deck support
- Animated draw, flip, and shuffle
- Card metadata and prompt interpretation lookup
- Draw Log with backlinks

#### Name & Identity Generator

- Thematic control (e.g. Ancient, Draconic, Forest, Cyber)
- Output logged to Character Profile or Dictionary

---

## 🧱 Supported Languages for Utilities

- Python – dice roller, card draw engine, logger
- Lua – directory map generator
- Go – markdown summarizer
- Elixir – vault validator (async hygiene checks)
- Rust – link fixer / ID repair tool
- R – vault metadata analytics
- Ruby – YAML injector / bulk metadata updater

---

## 🧩 UI Helpers

- VaultOS HUD
- styles.css for animated HUD and labels
- variables.css with customizable tokens
- snippets.css for quick drop-in visuals and states
- style-guide.md for contributor design consistency

---

## 🔗 Related Notes

> [!info] 🧠 Relationships  
> This note is part of a larger structure. Below are its connections:

```dataview
table
  parent as "Parent",
  children as "Subpages",
  friends as "Friends",
  related as "Related"
from ""
where file.link = this.file.link
```
