---
# 📄 Identity & Classification
id: note_py_variables
title: Variables and Types
aliases:
  - Variables and Types
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

## 🧮 Variables in Python

Variables are just names that point to values. No declarations needed. No types specified. Python figures it out at runtime.

Variables are labels pointing to objects in memory. No need to declare types.

```python
x = 5
name = "PtiCalin"
is_happy = True
```

---

### 🔁 Reassigning

```python
x = 42
x = "now I'm a string"
```

---

### 🔗 Related Concepts

- `id()`, `type()`
- Mutability
- Constants (by convention: `ALL_CAPS`)

---

### 🧠 Key Concepts

- Use `=` to assign values
- Variable types are inferred automatically
- Names must start with a letter or underscore
- Python is case-sensitive → `Name` ≠ `name`
- You can reassign a variable to a new value or type

```python
x = 42
name = "PtiCalin"
pi = 3.14
x = "now I'm a string"
```

---

### 💡 Tips

- Use descriptive names (`user_age`, not `ua`)
- Avoid overwriting built-in names (like `list`, `str`, `id`)
- Variables hold references to objects, not the objects themselves
- Multiple assignment works: `a, b = 1, 2`

---

## 🧪 Experimental Log

### 🔸 Trial 1: Reassigning Types

```python
x = 10
x = "hello"
```

→ Python doesn’t complain. Variable types can change mid-script.

---

### 🔸 Trial 2: Swapping Variables

```python
a = 1
b = 2
a, b = b, a
```

→ This swap works without needing a temp variable. Feels elegant.

---

### 🔸 Trial 3: Dynamic Typing Confusion

```python
total = 5
total += "5"
```

→ Got `TypeError`. Python doesn't auto-convert strings and ints.  
Lesson: dynamic doesn’t mean careless.

---

## 🌀 Thoughts

- Still weird that variables don’t need to be declared — I keep expecting an error.
- I like being able to swap values without temp vars. Very Pythonic.
- Naming things feels more important here — no types to rely on as hints.
- Accidentally overwriting built-ins (like `list`) is easier than expected. Need to be more careful.

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