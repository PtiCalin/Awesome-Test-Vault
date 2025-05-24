---
```yaml
# 📄 Identity & Classification
id: extract-helper
title: "Universal Extract Helper"
aliases: []
type: lesson
category: computing
section: shell
role: learning
folder: encyclopedia
tags: ['cli', 'bash', 'archive', 'utility']
version: 1.2

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-05-24
updated: 2025-05-24

# 📚 Context & Description
summary: "Extracts any archive file format with one command."

# 🧱 Relationships
parent: "cli-helper"
children: []
friends: ['cli-helper', 'file-utilities']
related: ['compression']
```
---

> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

---

> 🌛 Quick Actions  
> ➕ [New Project Ticket](obsidian://new?name=Projects/New%20Project%20-%20Universal%20Extract%20Helper)  
> 🌹 [New Quest](obsidian://new?name=Quests/New%20Quest%20-%20Universal%20Extract%20Helper)  
> 🎯 [New Task](obsidian://new?name=Tasks/New%20Task%20-%20Universal%20Extract%20Helper)  
> 🗕 [Schedule Event](obsidian://new?name=Events/New%20Event%20-%20Universal%20Extract%20Helper)  
> 📝 [Brain Dump](obsidian://new?name=Notes/Brain%20Dump%20-%20Universal%20Extract%20Helper)  
> 📚 [New Lesson](obsidian://new?name=Lessons/New%20Lesson%20-%20Universal%20Extract%20Helper)

---

## ✍️ Content Starts Here

### 🔧 Universal Extract Helper

```bash
extract() {
  if [ -f "$1" ]; then
    case "$1" in
      *.tar.bz2) tar xjf "$1" ;;
      *.tar.gz)  tar xzf "$1" ;;
      *.bz2)     bunzip2 "$1" ;;
      *.rar)     unrar x "$1" ;;
      *.gz)      gunzip "$1" ;;
      *.tar)     tar xf "$1" ;;
      *.tbz2)    tar xjf "$1" ;;
      *.tgz)     tar xzf "$1" ;;
      *.zip)     unzip "$1" ;;
      *.Z)       uncompress "$1" ;;
      *.7z)      7z x "$1" ;;
      *) echo "'$1' cannot be extracted via extract()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
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
