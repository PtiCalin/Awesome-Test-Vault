---
# 📄 Identity & Classification
id: note_py_decorators
title: "Decorators"
aliases: ["Decorators"]
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

> [!nav] Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

## 🧩 What are Python Decorators?

A **decorator** is a special function that modifies the behavior of another function or method without changing its actual code. It “wraps” a function, often to add logic before or after it runs.

They are commonly used for logging, timing, caching, authentication, and more.

---

### 🧪 Basic Example

```python
def shout(func):
    def wrapper():
        print("Before the call")
        func()
        print("After the call")
    return wrapper

@shout
def greet():
    print("Hello!")

greet()
```

🧠 Output:
```
Before the call
Hello!
After the call
```

---

### 🔎 Why Use Decorators?

- Clean separation of concerns
- Reusable wrappers
- Enhances readability when scaling logic

---

### 🔗 Related Concepts

- `@staticmethod` and `@classmethod`
- `functools.wraps` for preserving metadata
- Custom middleware in web frameworks


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