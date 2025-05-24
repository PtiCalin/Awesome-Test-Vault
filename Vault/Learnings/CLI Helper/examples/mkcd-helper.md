---
```yaml
# 📄 Identity & Classification
id: mkcd-helper
title: "mkcd Helper"
aliases: []
type: lesson
category: computing
section: shell
role: learning
folder: encyclopedia
tags: ['cli', 'bash', 'function', 'navigation']
version: 1.2

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-05-24
updated: 2025-05-24

# 📚 Context & Description
summary: "Creates a directory and immediately navigates into it."

# 🧱 Relationships
parent: "cli-helper"
children: []
friends: ['cli-helper', 'bash-functions']
related: ['directory-management']
```
---

> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

---

> 🌛 Quick Actions  
> ➕ [New Project Ticket](obsidian://new?name=Projects/New%20Project%20-%20mkcd%20Helper)  
> 🌹 [New Quest](obsidian://new?name=Quests/New%20Quest%20-%20mkcd%20Helper)  
> 🎯 [New Task](obsidian://new?name=Tasks/New%20Task%20-%20mkcd%20Helper)  
> 🗕 [Schedule Event](obsidian://new?name=Events/New%20Event%20-%20mkcd%20Helper)  
> 📝 [Brain Dump](obsidian://new?name=Notes/Brain%20Dump%20-%20mkcd%20Helper)  
> 📚 [New Lesson](obsidian://new?name=Lessons/New%20Lesson%20-%20mkcd%20Helper)

---

## ✍️ Content Starts Here

### 🔧 mkcd Helper

```bash
mkcd() {
  mkdir -p "$1" && cd "$1"
}
```

📌 Add this to your `.bashrc` or `.zshrc` file to make it always available.

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
