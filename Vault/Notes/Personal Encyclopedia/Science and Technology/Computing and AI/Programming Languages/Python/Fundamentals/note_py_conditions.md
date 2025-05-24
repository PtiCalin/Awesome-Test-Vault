---
# 📄 Identity & Classification
id: note_py_conditions
title: "Conditional Logic"
aliases: ["Conditional Logic", "conditions"]
type: note
category: programming
section: science-and-technology
role: documentation
folder: python
tags: []
version: 1

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


> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[💘 Learnings]] • [[🧠 System]]

---


## 🔍 Python Conditions — If, Elif, Else

Conditional statements let you run code based on whether a condition is `True`. Python uses `if`, `elif`, and `else` — with colons and indentation to define blocks.

### 🧠 Key Concepts

- `if` starts the condition chain
- `elif` = “else if” — check another condition if the first was false
- `else` = fallback if none of the above matched
- Conditions must end with a colon `:`
- Indentation defines what runs in each block

```python
x = 10

if x > 15:
    print("Large")
elif x > 5:
    print("Medium")
else:
    print("Small")
```

---

### 💡 Tips

- Boolean expressions use `==`, `!=`, `<`, `>`, `<=`, `>=`
- Use `and`, `or`, `not` for compound conditions
- Always indent blocks (standard: 4 spaces)
- Python doesn’t use parentheses or braces — just logic and spacing

---

## 🧪 Experimental Log

### 🔸 Trial 1: Basic Condition

```python
if True:
    print("This runs")
```

→ As expected.

---

### 🔸 Trial 2: Multiple Elif Blocks

```python
temp = 22

if temp > 30:
    print("Hot")
elif temp > 20:
    print("Nice")
elif temp > 10:
    print("Cool")
else:
    print("Cold")
```

→ Prints `"Nice"` — only the first matching block runs. Good to know.

---

### 🔸 Trial 3: Chaining with `and`

```python
age = 25
if age > 18 and age < 30:
    print("Young adult")
```

→ Worked. Tried again using:

```python
if 18 < age < 30:
```

→ Also valid. Python allows chained comparisons.

---

## 🌀 Thoughts

- I keep forgetting the colon at the end of `if` and `elif` lines.
- Chained comparisons like `18 < age < 30` are weirdly elegant.
- `elif` feels cleaner than a nested `if` — makes reading easier.
- No parentheses needed is still hard to get used to, coming from other languages.

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
