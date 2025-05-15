
## 🔍 Python Syntax — Basics

Python’s syntax is designed to be clean and readable. It avoids symbols and ceremony. Whitespace matters. Blocks are defined by indentation instead of braces or keywords.

### 🧠 Key Concepts

- **Statements** end by line breaks (not semicolons)
- **Indentation** is structural, not stylistic (4 spaces is standard)
- **Blocks** (loops, functions, classes) are defined by indentation
- **Colons** `:` signal the start of a block (e.g. `if`, `for`, `def`)
- **Comments** use `#` and are ignored by the interpreter
- **Case-sensitive** — `Variable` and `variable` are different

```python
# This is a comment
x = 10

if x > 5:
    print("x is large")
```

---

### 💡 Tips

- No braces `{}` or `end` keywords — just indentation.
- Use 4 spaces consistently. Mixing tabs and spaces will break things.
- Empty blocks need `pass` as a placeholder.
- Use parentheses for multi-line expressions or function chains.

---

## 🧪 Experimental Log

### 🔸 Trial 1: Indentation Errors

Tried copy-pasting from a poorly-formatted source:

```python
def test():
print("oops")
```

→ Got `IndentationError: expected an indented block`.  
Fixed it with 4-space indent.

---

### 🔸 Trial 2: Multi-line Code

Tried this:

```python
total = (
    1 +
    2 +
    3
)
```

→ Worked. Python allows this if wrapped in `()` — good for readability.

---

### 🔸 Trial 3: Mixing Tabs and Spaces

Did it by accident. VS Code showed a warning. Python threw a `TabError`.  
Lesson: Stick to 4 spaces. Always.

---

## 🌀 Thoughts

- Indentation rules are strict, but they make things more readable by default.
- I keep forgetting to add a colon after `if`, `def`, etc.
- Comments with `#` are surprisingly satisfying. Clean and out of the way.
- The way line breaks and parentheses interact feels intuitive once I tried it a few times.
