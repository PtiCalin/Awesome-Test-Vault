---
id: modules-and-packages
title: "Modules and Packages"
aliases: []
tags: []
author(s): PtiCalin
version: 1.3
status: draft
visibility: public
created: 2025-05-15
updated: 2025-05-15
summary: ""
element: Notes
type: "Personal Encyclopedia"
category: "Science and Technology"
section: "Computing and AI"
topic: "Programming Languages"
parent: ""
children: []
siblings: []
friends: []
---
> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[⛮  System]]

## 📦 Python Modules

A module is any `.py` file that contains Python code and can be imported into another script.

---

### 🔧 Example

```python
# in helpers.py
def greet(): print("Hello!")

# in main.py
import helpers
helpers.greet()
```

---

### 🧠 Benefits

- Organize code into separate files
- Reuse functions across scripts
- Reduce clutter in main programs

---

### 🔗 Related Concepts

- `import`, `from`, `as`
- Packages and `__init__.py`
- Python Path

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