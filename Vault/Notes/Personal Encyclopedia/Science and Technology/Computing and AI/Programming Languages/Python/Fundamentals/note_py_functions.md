---
# 📄 Identity & Classification
id: note_py_functions
title: "Defining and using functions"
aliases: ["Defining and using functions"]
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

## 🧩 What is a Function?

A **function** is a named block of reusable code that performs a specific task. Functions let you modularize your programs and avoid repetition.

---

### 🧪 Basic Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("PtiCalin")
```

---

### 🧮 With Return Values

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

---

### 🧠 Benefits

- Improves readability and reuse
- Makes testing and debugging easier
- Supports abstraction and design patterns

---

### 🔗 Related Concepts

- `*args`, `**kwargs`
- Scope (`global` vs `local`)
- Closures and decorators


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