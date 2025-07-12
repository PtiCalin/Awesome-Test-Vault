---
id: generators
title: Generators
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

## 🔄 What is a Generator?

Generators are a type of iterable, like lists or tuples—but instead of holding all values in memory, they **generate values on the fly** using the `yield` keyword.

They are ideal for large datasets or infinite streams.

---

### 🧪 Basic Example

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)
```

🧠 Output:

```txt
1
2
3
```

---

### 🔍 Generator vs Return

- `return` exits and hands back a single value
- `yield` pauses execution and resumes later

---

### 💡 Use Cases

- Reading large files line by line
- Producing infinite sequences
- Streaming data pipelines

---

### 🔗 Related Concepts

- `yield from` syntax
- Generator expressions
- Coroutines (async/await)

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
