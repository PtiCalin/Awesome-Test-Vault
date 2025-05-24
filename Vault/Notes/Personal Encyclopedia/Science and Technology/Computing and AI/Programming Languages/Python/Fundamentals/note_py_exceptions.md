---
# 📄 Identity & Classification
id: note_py_exceptions
title: "Exception Handling"
aliases: ["Exception Handling"]
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

## ⚠️ What are Exceptions?

Exceptions are errors detected during execution that disrupt the normal flow of a program. Python provides built-in ways to **catch**, **handle**, or **raise** them.

---

### 🧪 Basic Structure

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero.")
finally:
    print("Always runs!")
```

---

### 🧠 Custom Exceptions

```python
class MyError(Exception):
    pass
```

Raise it:

```python
raise MyError("Something went wrong!")
```

---

### 🔍 Best Practices

- Be specific: catch only exceptions you expect
- Use `finally` for cleanup
- Create custom exceptions for clarity

---

### 🔗 Related Concepts

- `assert`
- Error logs & debugging
- Context managers (`with`)

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