---
title: "Big O Notation"
created: 2025-04-30
type: note
tags: [note, "computational complexity"]
parent: "Computational Complexity"
children: []
---

# ⏱️ Big O Notation

## 🧭 Summary
Big O Notation is a mathematical framework used to describe the performance of an algorithm—specifically its time or space complexity—as the input size increases.

It captures the worst-case growth rate, ignoring constants and lower-order terms to focus on asymptotic behavior.

"Big O is about how your algorithm scales."

## 🧠 Core Concepts
| Term | Description |
| --- | --- |
| n | The size of the input |
| Time Complexity | How computation time grows with input |
| Space Complexity | How memory usage grows with input |
| Worst-Case | The maximum time or space required |
| Best-Case | The minimum time required (often ignored in Big O) |
| Average-Case | Expected time over all inputs (used with caution) |

## 🧮 Common Big O Complexities
| Notation | Name | Example | Growth |
| --- | --- | --- | --- |
| O(1) | Constant | Array access by index | 🔒 |
| O(log n) | Logarithmic | Binary search | 📉 Efficient |
| O(n) | Linear | Loop through array | 📈 |
| O(n log n) | Quasilinear | Merge sort, Quick sort | ⚖️ Efficient sorting |
| O(n²) | Quadratic | Nested loops (e.g., Bubble sort) | 🐢 Slow |
| O(2ⁿ) | Exponential | Recursive brute-force (e.g., subset problems) | 🧨 |
| O(n!) | Factorial | Travelling salesman brute-force | 💀 |

## 📊 Visual Growth Comparison
| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 1 | 0 | 1 | 2 |
| 10 | 1 | 3 | 10 | 33 | 100 | 1024 |
| 100 | 1 | 6 | 100 | 664 | 10,000 | ~1e30+ |

## 🛠️ Rules of Thumb
- Drop constants: `O(3n)` ➝ `O(n)`
- Drop lower terms: `O(n + log n)` ➝ `O(n)`
- Multiply nested loops: `O(n) * O(n) = O(n²)`
- Function calls can stack: recursion and sorting affect growth

## 🧪 Quick Code Examples
**O(1) — Constant**
```python
def get_first_item(lst):
    return lst[0]
```

**O(n) — Linear**
```python
for item in lst:
    print(item)
```

**O(n²) — Quadratic**
```python
for i in lst:
    for j in lst:
        print(i, j)
```

## 🧬 Related Topics
- "Time and Space Complexity"
- "Algorithm Efficiency"
- "Recursion & Stack Depth"
- "Dynamic Programming vs Greedy"
- "Data Structures & Complexity Tradeoffs"
