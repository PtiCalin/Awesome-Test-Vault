---
# 📄 Identity & Classification
id: note_py_partial-functions
title: "Partial functions"
aliases: ["Partial functions"]
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

### 🧩 What is `functools.partial`?

`functools.partial` lets you "freeze" some portion of a function’s arguments and keywords, returning a new function with fewer arguments.

---

### 🧪 Example

```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # 10
```

---

### 🔗 Related Concepts

- Higher-order functions
- Currying
- `functools.wraps`


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
