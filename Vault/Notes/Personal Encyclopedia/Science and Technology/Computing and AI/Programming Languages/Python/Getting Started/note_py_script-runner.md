---
# 📄 Identity & Classification
id: note_py_script-runner
title: "Running scripts from terminal or IDE"
aliases: ["Running scripts from terminal or IDE"]
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


## 🔍 Running Python Scripts — Overview & Best Practices

There are multiple ways to run Python scripts depending on the context (terminal, editor, notebook). The main options:

### ▶️ Run via Terminal (PowerShell, Bash, CMD)

```bash
python script_name.py
```

- Must be in the script’s directory or provide full path
- Use `python3` if `python` is mapped to something else (common on macOS/Linux)

### ▶️ Run from Inside Python

Inside the REPL:

```python
exec(open("script_name.py").read())
```

Mostly for testing or exploration. Not the cleanest method for full runs.

### ▶️ Run from VS Code

- Open the file
- Click “Run Python File” in the top-right or use:

```bash
Ctrl + F5  # Run without debugging
F5         # Run with debugging
```

Make sure you’ve selected the correct interpreter:  
`Ctrl+Shift+P → Python: Select Interpreter`

### ▶️ Run as Executable Script (Optional)

Add a shebang at the top (Unix systems only):

```python
#!/usr/bin/env python3
```

Then:

```bash
chmod +x script_name.py
./script_name.py
```

Useful when scripting in Linux environments.

---

## 🧪 Experimental Log

### 💻 Trial 1: Running from PowerShell

```bash
python hello.py
```

→ Worked. No issues.  
Tested with a simple `print("Hello from PowerShell")`.

### ⚠️ Trial 2: Forgot to CD into Directory

Running from the wrong path caused:

```text
python: can't open file 'hello.py': [Errno 2] No such file or directory
```

Reminder: terminal context matters. Use `cd` or right-click → “Open in Terminal.”

---

### 🧪 Trial 3: VS Code Integration

- Opened file in VS Code
- Prompted to install Python extension
- Selected interpreter → top bar “Run Python File” worked as expected

Also tested the debugger. `F5` triggers breakpoint mode — useful for step-by-step learning.

---

## 🌀 Thoughts
- I keep forgetting that the terminal needs to be “in” the same folder as the script.
- VS Code makes it surprisingly smooth to run files without any setup.
- Not sure yet when to use `Ctrl + F5` vs `F5`. I just pick one and hope it runs.

### 💡 Ideas for Automating

- Might create a `run.ps1` or `run.bat` file to simplify multi-script workflows
- Could explore `watchdog` or `entr` to auto-run on file save

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
