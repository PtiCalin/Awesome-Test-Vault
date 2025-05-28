---
# 📄 Identity & Classification
id: note_py_map-filter-reduce
title: "Functional tools"
aliases: ["Functional tools"]
type: note
category: programming
section: science-and-technology
role: documentation
folder: python
tags: []
version: 1.2

# 📊 Status & Lifecycle
status: draft
visibility: draft-only
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

### 🔀 Functional Tools: `map`, `filter`, and `reduce`

These built-in functions enable functional-style processing of data.

---

### 🧪 Examples

```python
nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

---

### ➕ Using `reduce`

```python
from functools import reduce

product = reduce(lambda x, y: x * y, nums)
```

---

### 🔗 Related Concepts

- Lambda functions
- List comprehensions
- `functools` module


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
