---
# 📄 Identity & Classification
id: note_py_closures
title: Closures
aliases:
  - Closures
type: note
category: programming
section: science-and-technology
role: documentation
folder: python
tags: 
version: 1.0

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-05-15
updated: 2025-05-15

# 🧱 Relationships
parent: ""
children: []
friends: []
related: []
---

> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

## 🧬 What is a Closure?

A **closure** is a function that captures variables from its enclosing scope even after that scope has finished executing.

Closures “remember” their context.

---

### 🧪 Basic Example

```python
def outer(msg):
    def inner():
        print(msg)
    return inner

say_hi = outer("Hi!")
say_hi()  # prints "Hi!"
```

Even though `outer()` has returned, `inner()` still has access to `msg`.

---

### 🧠 Closures vs Regular Functions

Closures can:
- Maintain state without using classes
- Be used for decorators or custom logic injection

---

### 🔗 Related Concepts

- Nested functions
- Nonlocal variables
- Decorators (built with closures!)


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