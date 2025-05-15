---
id: qst_changelog-watcher
title: Automate Changelog Tracking
type: quest
version: '1.0'
status: completed
priority: high
created: '2025-05-10'
updated: '2025-05-10'
tags:
- quest
- automation
- changelog
- python
assigned_to: charlie
related:
- sys_nc-yaml
- sys_nc-index
parent: qst_vault-automation-series
rewards:
- 'XP: 40'
- 'Nugget: changelog'
- 'Unlocks: [qst_dashboard-sync]'
questline: Vault Automation Series
skill_tree: "\U0001F5A5\uFE0F Shell + Markup"
summary: Create a Python-based automation script that appends a changelog version
  entry to any file that has been updated and has a new version declared in its YAML
  frontmatter.
---

## 🎯 Objectives
- [x] Define changelog metadata standard
- [x] Build script to read `version` from YAML frontmatter
- [x] Detect whether that version is present in markdown changelog section
- [x] Append changelog entries automatically with date
- [x] Save and document the script

## 📁 Deliverables
- `changelog_watcher.py`
- Updated markdown files with `## 🔄 Change Log` entries

## 🛠️ Tools Used
- Python (re, pathlib, datetime)

## 🧩 Links
- [[sys_nc-yaml]]
- [[sys_nc-index]]