---
# 📄 Identity & Classification
id: note_py_syntax-basics
title: Keywords, indentation, structure
aliases:
  - Keywords, indentation, structure
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
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

## 🧾 Python Syntax Basics

Python’s syntax emphasizes readability and indentation.

---

### Key Rules

- No curly braces — use indentation
- No semicolons needed
- Variables are dynamically typed

---

### 🧪 Example

```python
x = 5
if x > 0:
    print("Positive")
else:
    print("Zero or negative")
```

---

## 🔍 Python Syntax — Basics

Python’s syntax is designed to be clean and readable. It avoids symbols and ceremony. Whitespace matters. Blocks are defined by indentation instead of braces or keywords.

### 🧠 Key Concepts

- **Statements** end by line breaks (not semicolons)
- **Indentation** is structural, not stylistic (4 spaces is standard)
- **Blocks** (loops, functions, classes) are defined by indentation
- **Colons** `:` signal the start of a block (e.g. `if`, `for`, `def`)
- **Comments** use `#` and are ignored by the interpreter
- **Case-sensitive** — `Variable` and `variable` are different

```python
# This is a comment
x = 10

if x > 5:
    print("x is large")
```

---

### 💡 Tips

- No braces `{}` or `end` keywords — just indentation.
- Use 4 spaces consistently. Mixing tabs and spaces will break things.
- Empty blocks need `pass` as a placeholder.
- Use parentheses for multi-line expressions or function chains.

---

## 🧪 Experimental Log

### 🔸 Trial 1: Indentation Errors

Tried copy-pasting from a poorly-formatted source:

```python
def test():
print("oops")
```

→ Got `IndentationError: expected an indented block`.  
Fixed it with 4-space indent.

---

### 🔸 Trial 2: Multi-line Code

Tried this:

```python
total = (
    1 +
    2 +
    3
)
```

→ Worked. Python allows this if wrapped in `()` — good for readability.

---

### 🔸 Trial 3: Mixing Tabs and Spaces

Did it by accident. VS Code showed a warning. Python threw a `TabError`.  
Lesson: Stick to 4 spaces. Always.

---

## 🌀 Thoughts

- Indentation rules are strict, but they make things more readable by default.
- I tend to forget to add a colon after `if`, `def`, etc.
- Comments with `#` are surprisingly satisfying. Clean and out of the way.
- The way line breaks and parentheses interact feels intuitive once I tried it a few times.

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