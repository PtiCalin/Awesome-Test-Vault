---
# 📄 Identity & Classification
id: note_py_setup-windows
title: "Installing Python on Windows"
aliases: ["Installing Python on Windows"]
type: note
category: programming
section: science-and-technology
role: documentation
folder: python
tags: []
version: 1

# 📊 Status & Lifecycle
status: draft
visibility: draft-only
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
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

---


## 🔍 Installing Python on Windows — Key Notes & Takeaways

Installing Python on Windows is a little more visible than expected — installers, dialogs, choices. Most of it works if you trust the defaults, but a few key steps matter more than others.

### 🧭 What I Needed to Do

1. Download from: [python.org/downloads/windows](https://www.python.org/downloads/windows/)
2. Launched the `.exe` installer.
3. **Checked** the box for “Add Python to PATH.” Critical.
4. Went with “Customize Installation” just to see — left most defaults untouched.
5. Installed.

After install, opened PowerShell and ran:

```powershell
python --version
```

→ Output: `Python 3.13.3`  
That confirmed the install and that the PATH variable was set correctly.

---

### 🧠 Key Points

- Always check the “Add Python to PATH” box — missing it leads to hard-to-debug errors.
- Python installs both `python` and `pip` by default.
- Avoid the Windows Store version. It’s a different experience and not always consistent.
- Custom install lets you choose advanced options, but defaults are usually fine.
- Install location matters — good to make a note of it.

---

## 🧪 Experimental Log

### 💻 First Run: Clean Install

Went through the installer with PATH checked. Install completed cleanly.

Ran:

```powershell
python
```

→ Opened the REPL. Typed `print("hello world")`. Output appeared as expected.

Checked pip:

```powershell
pip --version
```

→ Also worked immediately. No manual installation needed.

---

### 🛠 Editor Setup

Installed VS Code.

- Opened a `.py` file.
- Got prompted to install the Python extension.
- Used `Ctrl+Shift+P → Python: Select Interpreter` to link VS Code to the new install.

Worked without issues.

---

## 🌀 Thoughts
- I hesitate at the “Add Python to PATH” checkbox. It feels important but unclear.
- The fact that it works from PowerShell after install surprised me.
- Noticed how VS Code quietly fixes a lot of setup pain.
- Still unsure when I’ll need to mess with advanced install options. For now I just stuck to defaults.

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
> ➕ [New Project Ticket](obsidian://new?name=Projects/New%20Project%20-%20<% tp.file.title %>)  
> 🌹 [New Quest](obsidian://new?name=Quests/New%20Quest%20-%20<% tp.file.title %>)  
> 🎯 [New Task](obsidian://new?name=Tasks/New%20Task%20-%20<% tp.file.title %>)  
> 🗕 [Schedule Event](obsidian://new?name=Events/New%20Event%20-%20<% tp.file.title %>)  
> 📝 [Brain Dump](obsidian://new?name=Notes/Brain%20Dump%20-%20<% tp.file.title %>)  
> 📚 [New Lesson](obsidian://new?name=Lessons/New%20Lesson%20-%20<% tp.file.title %>)

---