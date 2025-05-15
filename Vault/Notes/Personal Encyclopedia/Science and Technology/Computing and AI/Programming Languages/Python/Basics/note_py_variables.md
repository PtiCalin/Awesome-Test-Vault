
## 🔍 Python Variables — Basics

Variables are just names that point to values. No declarations needed. No types specified. Python figures it out at runtime.

### 🧠 Key Concepts

- Use `=` to assign values
- Variable types are inferred automatically
- Names must start with a letter or underscore
- Python is case-sensitive → `Name` ≠ `name`
- You can reassign a variable to a new value or type

```python
x = 42
name = "Charlie"
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
