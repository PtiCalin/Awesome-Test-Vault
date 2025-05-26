---
# 📄 Identity & Classification
id: note_py_partial-functions
title: "Partial functions"
aliases: ["Partial functions"]
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

## 🧩 What is `functools.partial`?

`functools.partial` lets you “freeze” some arguments of a function—returning a new function that takes fewer arguments. This technique is great for simplifying complex call signatures or creating reusable variants of existing functions.

---

### 🧪 Basic Example

```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # ➝ 10
```

Here, `double()` behaves like a new function that always uses `2` as the first argument to `multiply()`.

---

### 🧠 Why Use It?

- 💡 You have a general-purpose function and want to create a more specific version of it.
- 📦 Useful in callbacks, configuration layers, or when wrapping APIs that expect a different interface.
- 🧼 Keeps your code cleaner than defining many small wrapper functions manually.

---

### 💬 Comparison with Lambda

```python
double = lambda y: multiply(2, y)
```

✅ Works just as well—but `partial()` is more descriptive, especially when combined with keyword arguments.

---

### 🧪 Keyword Example

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

friendly_hello = partial(greet, greeting="Hey")
print(friendly_hello("PtiCalin"))  # ➝ Hey, PtiCalin!
```

---

### 🧱 Common Use Cases

- Pre-configuring function arguments
- Making cleaner callback signatures (e.g. in GUIs or web frameworks)
- Simplifying pipelines with preloaded functions

---

### 🔗 Related Concepts

- `functools.update_wrapper()` (used in decorators)
- Currying (functional programming)
- `functools.partialmethod` (for use in class methods)
- Wrapper functions and closures

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
