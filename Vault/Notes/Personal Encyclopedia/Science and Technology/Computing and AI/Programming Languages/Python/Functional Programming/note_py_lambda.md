---
# 📄 Identity & Classification
id: note_py_lambda
title: "Lambda functions"
aliases: ["Lambda functions"]
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

## ⚡ What is a Lambda Function?

A **lambda function** is a small, anonymous function in Python. It can have any number of arguments, but only one expression.

Think of it as a throwaway function—ideal for short, one-off uses.

---

### 🧪 Basic Syntax

```python
square = lambda x: x**2
print(square(4))  # 16
```

---

### 🔁 Use with `map()`, `filter()`, `sorted()`

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
```

---

### 🚫 Limitations

- No multi-line code
- Only expressions, not statements

---

### 🔗 Related Concepts

- `def` vs `lambda`
- Functional programming (with `map`, `filter`, `reduce`)


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