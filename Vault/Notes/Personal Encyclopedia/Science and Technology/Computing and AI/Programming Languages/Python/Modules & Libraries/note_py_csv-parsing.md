---
# 📄 Identity & Classification
id: note_py_csv-parsing
title: "Parsing CSV files"
aliases: ["Parsing CSV files"]
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
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[⛮  System]]


### 📊 Reading and Writing CSV in Python

The `csv` module lets you read from and write to CSV (Comma Separated Values) files easily.

---

### 🧪 Reading a CSV File

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

### 🧾 Writing to CSV

```python
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['PtiCalin', 28])
```

---

### 🔗 Related Concepts

- `pandas` for advanced data handling
- `DictReader` and `DictWriter`

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