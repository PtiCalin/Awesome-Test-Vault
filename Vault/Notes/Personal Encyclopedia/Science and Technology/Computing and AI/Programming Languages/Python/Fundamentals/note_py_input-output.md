---
# 📄 Identity & Classification
id: note_py_input-output
title: "Reading input and displaying output"
aliases: ["Reading input and displaying output"]
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

## 🖨️ Input and Output in Python

Python uses simple built-in functions for reading user input and displaying results.

---

### 🔡 Getting Input

```python
name = input("What's your name? ")
print("Hello,", name)
```

Input is always returned as a **string**—you’ll often need to cast it:

```python
age = int(input("Enter your age: "))
```

---

### 🖨️ Printing Output

```python
print("The answer is", 42)
print(f"Hello, {name}!")  # f-strings!
```

---

### 📁 File I/O

```python
with open("notes.txt", "r") as file:
    content = file.read()

with open("notes.txt", "w") as file:
    file.write("New content")
```

---

### 🔗 Related Concepts

- Type conversion
- f-strings and formatting
- Context managers (`with open(...)`)

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