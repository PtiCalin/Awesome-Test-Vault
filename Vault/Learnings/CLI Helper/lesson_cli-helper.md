---
```yaml
# 📄 Identity & Classification
id: cli-helper
title: "CLI Helper"
aliases: ["command line helper", "cli tools", "shell shortcut"]
type: lesson
category: computing
section: shell
role: learning
folder: encyclopedia
tags: [cli, shell, bash, productivity]
version: 1.2

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-05-24
updated: 2025-05-24

# 📚 Context & Description
summary: "An introduction to CLI helpers—tools, scripts, and shortcuts that improve command-line workflows."

# 🧱 Relationships
parent: "shell-basics"
children: []
friends: ["bash-aliases", "tldr", "fzf"]
related: ["terminal-basics", "bash-functions"]
```
---

> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

---

### 🧰 What is a CLI Helper?

A **CLI Helper** is a tool, script, or shortcut that enhances the usability and efficiency of working in the **Command Line Interface (CLI)**. CLI Helpers simplify complex commands, automate routine tasks, and improve the readability or speed of terminal workflows.

---

### 🛠️ Types of CLI Helpers

| Type       | Example                                        | What It Does                              |
|------------|------------------------------------------------|--------------------------------------------|
| Alias      | `alias gs="git status"`                        | Shortens long commands                     |
| Function   | `mkcd() { mkdir -p "$1" && cd "$1"; }`       | Creates and enters a directory             |
| Script     | `backup.sh`                                    | Automates file backups and logs output     |
| Tool       | `tldr`, `navi`, `bat`, `http-server`, `fzf`    | Adds user-friendly features or enhancements|

---

### 🎯 Why Use CLI Helpers?

✅ Saves time on repetitive commands  
✅ Reduces cognitive load by standardizing syntax  
✅ Makes scripts and workflows reusable  
✅ Provides readable output or additional features  

---

### 💡 Sample Bash Helper: `gitlog-pretty`

```bash
gitlog-pretty() {
  git log --oneline --graph --decorate --all
}
```

Run `gitlog-pretty` to see a color-coded Git history graph—no memorization needed!

---

### 🧱 Build Your Own CLI Helpers

Start small:
- Use `alias` for common commands
- Define functions in your `.bashrc` or `.zshrc`
- Write `.sh` scripts for tasks with multiple steps
- Add helpful CLI tools (`tldr`, `navi`, `bat`)

Organize helpers in a `~/cli-helpers/` folder for reuse and sharing.

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
---

> 🌛 Quick Actions  
> ➕ [New Project Ticket](obsidian://new?name=Projects/New%20Project%20-%20CLI%20Helper)  
> 🌹 [New Quest](obsidian://new?name=Quests/New%20Quest%20-%20CLI%20Helper)  
> 🎯 [New Task](obsidian://new?name=Tasks/New%20Task%20-%20CLI%20Helper)  
> 🗕 [Schedule Event](obsidian://new?name=Events/New%20Event%20-%20CLI%20Helper)  
> 📝 [Brain Dump](obsidian://new?name=Notes/Brain%20Dump%20-%20CLI%20Helper)  
> 📚 [New Lesson](obsidian://new?name=Lessons/New%20Lesson%20-%20CLI%20Helper)

---