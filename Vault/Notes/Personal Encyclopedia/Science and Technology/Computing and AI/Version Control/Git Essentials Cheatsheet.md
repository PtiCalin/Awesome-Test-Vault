---
id: git-essentials-cheatsheet
title: "Git Essentials Cheatsheet"
aliases: []
tags: [git, cheatsheet]
author(s): PtiCalin
version: 1.3
status: draft
visibility: public
created: "<% today %>"
updated: "<% today %>"
summary: ""
element: Notes
type: "Personal Encyclopedia"
category: "Science and Technology"
section: "Computing and AI"
topic: "Version Control"
parent: "Version Control"
children: []
siblings: []
friends: []
---
> [!nav] 🧱 Vault Navigation
<!-- Relative Nav Bars -->
<!-- Notes -->
<!-- Learnings -->
<!-- Libraries -->
<!-- System -->

## 🧪 Git Essentials Cheatsheet

## 🔤 Quick Summary  
Git is a distributed version control system for tracking changes in source code during software development.

---

## 🧠 Core Concepts

| Command        | Description                    |
|---------------|--------------------------------|
| `git init`     | Initialize a repo              |
| `git clone`    | Copy repo to local             |
| `git add`      | Stage changes                  |
| `git commit`   | Save staged changes            |
| `git push`     | Send changes to remote         |
| `git pull`     | Fetch + merge from remote      |
| `git branch`   | List or create branches        |
| `git checkout` | Switch branches                |
| `git merge`    | Merge branches                 |

---

## 🧰 Workflow

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main
```

### 💡 Gotchas
- Always pull before pushing to avoid merge conflicts
- Use `.gitignore` to avoid committing junk files
- Don’t commit sensitive data — use `.env` and secret managers

### 🔗 Related
- [[GitHub]]
- [[Version Control Concepts]]
- [[CLI Cheatsheets]]

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
