---
# 📄 Identity & Classification
id: note_py_introspection
title: "Code introspection and reflection"
aliases: ["Code introspection and reflection"]
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

---

> 🌛 Quick Actions  
> ➕ [New Project Ticket](obsidian://new?name=Projects/New%20Project%20-%20<% tp.file.title %>)  
> 🌹 [New Quest](obsidian://new?name=Quests/New%20Quest%20-%20<% tp.file.title %>)  
> 🎯 [New Task](obsidian://new?name=Tasks/New%20Task%20-%20<% tp.file.title %>)  
> 🗕 [Schedule Event](obsidian://new?name=Events/New%20Event%20-%20<% tp.file.title %>)  
> 📝 [Brain Dump](obsidian://new?name=Notes/Brain%20Dump%20-%20<% tp.file.title %>)  
> 📚 [New Lesson](obsidian://new?name=Lessons/New%20Lesson%20-%20<% tp.file.title %>)

---

## ✍️ Content Starts Here

## ✍️ Content Starts Here

### 🧠 What is Introspection?

**Introspection** is Python’s ability to examine the type or properties of objects at runtime.

You can explore variables, functions, and modules programmatically.

---

### 🧪 Common Tools

```python
type(42)             # <class 'int'>
dir(str)             # List attributes/methods of str
help(list)           # Show docstring
isinstance(3, int)   # True
callable(print)      # True
```

---

### 🔍 Deep Dive with `inspect`

```python
import inspect

def f(x): return x
print(inspect.signature(f))  # (x)
```

---

### 🧩 Use Cases

- Debugging and REPL exploration
- Reflection in frameworks (e.g., Flask route discovery)
- Dynamic function signatures and wrappers

---

### 🔗 Related Concepts

- `__dict__` and `__name__`
- Reflection vs introspection
- Metaprogramming


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
