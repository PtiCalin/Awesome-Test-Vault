---
# 📄 Identity & Classification
id: note_py_list-comprehensions
title: "Compact list manipulation"
aliases: ["Compact list manipulation"]
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

## 🧾 What is a List Comprehension?

A **list comprehension** provides a concise way to create lists using a single line of Python syntax.

It’s like a compact `for` loop inside square brackets.

---

### 🧪 Basic Syntax

```python
squares = [x**2 for x in range(5)]
```

🧠 Output:

```txt
[0, 1, 4, 9, 16]
```

---

### 🧪 With Conditions

```python
evens = [x for x in range(10) if x % 2 == 0]
```

🧠 Output:

```txt
[0, 2, 4, 6, 8]
```

---

### 💬 Readability Tips

- Prefer comprehensions for short, clear logic
- Avoid over-nesting (use loops or functions instead)

---

### 🔗 Related Concepts

- Dictionary and set comprehensions
- Generator expressions
- Functional tools like `map()` and `filter()`

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
