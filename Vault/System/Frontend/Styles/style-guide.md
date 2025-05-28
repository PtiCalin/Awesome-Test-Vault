---
id: style-guide
title: "🎨 VaultOS UI Style Guide"
tags: [design, frontend, css, theming]
version: 1.0
visibility: public
created: 2025-05-27
---

## 🧠 Overview

This guide defines the user interface language of VaultOS HUDs, panels, and modals.

## 🎯 Design Principles

- **Minimal UI:** Avoid clutter. Keep focus on modular information.
- **Pulsing Animation:** Used for live data (e.g. CPU, clock).
- **Backdrop Blur:** Creates depth. Works with Safari fallback.
- **Glowing Gradients:** Used in outlines/shadows for system metaphors.

## 🧱 Vault HUD Components

### `.vaultos-hud`

> Floating status/control widget

- Fixed bottom-right
- Blurred glass UI
- Fade-in animation
- Subcomponents: `.vaultos-hud-icon`, `.vaultos-hud-label`, `.vaultos-hud-value`

## 📁 Location of Styles

| Component         | File                                |
|------------------|-------------------------------------|
| HUD UI           | `System/Frontend/Obsidian/styles.css` |
| Modal themes     | _to be created_                     |
| Snippet overrides| `System/Frontend/Snippets/`         |

## 🧪 Testing Tips

- Test with Obsidian light + dark themes
- Resize to mobile widths for responsiveness
- Safari: ensure `-webkit-backdrop-filter` is present

## 🛠 To Do

- [ ] Create reusable modal styles
- [ ] Add `.vaultos-tooltip` standard
- [ ] Standardize icons with lucide or system font
