---
# 📄 Identity & Classification
id: note_py_venv-guide
title: "Using virtual environments"
aliases: ["Using virtual environments"]
type: note
category: programming
section: science-and-technology
role: documentation
folder: python
tags: []
version: 1.0

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-05-15
updated: 2025-05-15

# 📚 Context & Description
summary: ""

# 🧱 Relationships
parent: ""
children: []
friends: []
related: []
---


> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[⛮  System]]

## 🔍 Virtual Environments — Overview & Key Takeaways

A **virtual environment** in Python is a self-contained workspace where dependencies are isolated from the system-wide Python install. It allows you to:

- Keep projects from interfering with each other
- Avoid dependency conflicts
- Experiment safely without breaking global packages

---

### 🧱 Create a venv

```bash
python -m venv venv
```

Activate it:

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

---

### 🔄 Deactivate

```bash
deactivate
```

---

### 📦 How to Create One

```bash
python -m venv venv
```

This creates a `venv/` directory with its own Python binary and `pip`.

### ▶️ How to Activate (Windows)

```powershell
.env\Scriptsctivate
```

You’ll know it’s active when the terminal prompt includes `(venv)`.

### ❌ How to Exit

```bash
deactivate
```

### 🧠 Best Practices

- Use `.venv` instead of `venv` to keep the folder hidden (especially with VS Code).
- Never commit the `venv` folder — use `.gitignore`.
- Use `pip freeze > requirements.txt` to export dependencies.
- Recreate the environment elsewhere with `pip install -r requirements.txt`.

---

## 🧪 Experimental Log

### 🧱 Trial 1: Basic Setup

Created a new folder → ran:

```bash
python -m venv venv
```

→ Created instantly. Saw folders for `Scripts`, `Lib`, etc.  
Activated it:

```powershell
.env\Scriptsctivate
```

→ Prompt changed to `(venv)`. Success.

---

### 🧪 Trial 2: Installing a Package Inside

Ran:

```bash
pip install rich
pip list
```

→ Only `rich`, `pip`, `setuptools` shown.  
Verified that outside the venv, `rich` didn’t exist. Isolation confirmed.

---

### 🛠 Trial 3: Requirements.txt Workflow

```bash
pip freeze > requirements.txt
```

Created a full list of dependencies.

Deleted the venv, recreated it, and then:

```bash
pip install -r requirements.txt
```

→ Restored everything. Will use this more often moving forward.

---

## 🌀 Thoughts

- Took me a while to realize `venv` folders don’t copy well between systems.
- I tend to forget to activate the venv and wonder why pip is acting weird.
- Using `.venv` instead of `venv` keeps things cleaner in VS Code.

---

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
> ➕ [New Project Ticket](obsidian://new?name=Projects/New%20Project%20-%20<% tp.file.title %>)  
> 🌹 [New Quest](obsidian://new?name=Quests/New%20Quest%20-%20<% tp.file.title %>)  
> 🎯 [New Task](obsidian://new?name=Tasks/New%20Task%20-%20<% tp.file.title %>)  
> 🗕 [Schedule Event](obsidian://new?name=Events/New%20Event%20-%20<% tp.file.title %>)  
> 📝 [Brain Dump](obsidian://new?name=Notes/Brain%20Dump%20-%20<% tp.file.title %>)  
> 📚 [New Lesson](obsidian://new?name=Lessons/New%20Lesson%20-%20<% tp.file.title %>)

---
