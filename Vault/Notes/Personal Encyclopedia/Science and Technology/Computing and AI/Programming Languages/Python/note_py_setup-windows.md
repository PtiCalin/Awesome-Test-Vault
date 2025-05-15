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
version: 1.2

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

## 🌀 Reflection Dump

The process isn’t hard, but it feels opaque the first time — especially what “Add to PATH” really does.  
It’s one of those invisible setup decisions that can quietly break everything later if you skip it.

There’s something satisfying about seeing `python` respond from anywhere in the terminal. Like the system finally recognizes your intention.

This install is one of those small steps that unlocks everything else.
