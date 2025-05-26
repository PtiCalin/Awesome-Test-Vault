---
# 📄 Identity & Classification
id: note_py_regex
title: "Regular Expressions"
aliases: ["Regular Expressions"]
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

### 🔤 Regular Expressions (Regex) in Python

The `re` module lets you work with regular expressions—patterns for matching text.

---

### 🧪 Example

```python
import re

pattern = r'\d+'
text = "There are 3 apples"
result = re.findall(pattern, text)
print(result)  # ['3']
```

---

### 🔍 Common Patterns

- `\d` = digit
- `\w` = word char
- `.` = any char
- `*` = zero or more
- `+` = one or more
- `^` / `$` = start / end of line

---

### 🔗 Related Concepts

- String parsing
- Pattern matching
- Validation logic


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
