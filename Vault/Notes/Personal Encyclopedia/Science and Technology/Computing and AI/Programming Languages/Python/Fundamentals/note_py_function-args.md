---
# 📄 Identity & Classification
id: note_py_function-args
title: "Positional, keyword, *args, **kwargs"
aliases: ["Positional, keyword, *args, **kwargs"]
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

## 🧩 Understanding Function Arguments in Python

Python functions support multiple types of arguments:

- **Positional arguments**
- **Keyword arguments**
- **Default values**
- `*args` (variable positional arguments)
- `**kwargs` (variable keyword arguments)

---

### 🧪 Examples

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("PtiCalin")  # Hello, PtiCalin!
```

With `*args` and `**kwargs`:

```python
def show_all(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_all(1, 2, user="PtiCalin", mood="cheerful")
```

---

### 💬 Use Cases

- Flexible function design
- Passing dynamic configurations

---

### 🔗 Related Concepts

- Parameter unpacking
- `functools.partial`
- Function signatures with `inspect`

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
