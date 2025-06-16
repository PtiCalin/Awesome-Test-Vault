---
# 📄 Identity & Classification
id: intro-to-computing-algorithms
title: "Intro to Computing Algorithms"
aliases: []
tags: [computing-algorithms]
author(s):
element:
type: note
category:
section:
topic:
role:
folder: Personal Encyclopedia/Science and Technology/Computing and AI/Computing Algorithms
tags: []
version: 1.3

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-06-16
updated: 2025-06-16

# 📚 Context & Description
summary: "Overview of algorithm fundamentals."

# 🧱 Relationships
parent: "Computing Algorithms"
children: []
friends: []
related: []
---

> [!nav] 🧱 Vault Navigation
<!-- Relative Nav Bars -->
<!-- Notes -->
<!-- Learnings -->
<!-- Libraries -->
<!-- System -->

## ✍️ Intro to Computing Algorithms

An algorithm is a step-by-step set of instructions designed to solve a problem or perform a computation. Algorithms form the core of computer science, enabling everything from simple arithmetic to advanced AI.

They are logic engines—abstract machines that transform input into output by following a precise, finite process.

## 🧠 Core Concepts
| Concept | Definition |
| --- | --- |
| Algorithm | A finite, ordered sequence of steps to solve a specific task |
| Input | The data the algorithm receives |
| Output | The result produced after processing the input |
| Deterministic | Produces the same output for the same input |
| Non-deterministic | May produce different results with same input (e.g., probabilistic algorithms) |
| Efficiency | Time and space used to complete the task (Big O notation) |

## 🔢 Common Types of Algorithms
| Type | Description | Example |
| --- | --- | --- |
| Sorting | Arrange data in a specific order | Bubble Sort, Merge Sort, Quick Sort |
| Searching | Find an element in data | Binary Search, Linear Search |
| Recursive | Solve by calling itself with subproblems | Fibonacci, Factorial |
| Greedy | Make optimal local choice at each step | Dijkstra’s, Huffman Coding |
| Divide & Conquer | Split problem into smaller chunks | Merge Sort, Quick Sort |
| Dynamic Programming | Solve complex problems by breaking into overlapping subproblems | Knapsack, Memoized Fibonacci |
| Backtracking | Explore possible solutions by trial and error | Sudoku Solver, N-Queens |
| Machine Learning Algorithms | Learn patterns from data | Decision Trees, K-Means, Neural Networks |

## ⏱️ Time & Space Complexity (Big O)
| Complexity | Example | Description |
| --- | --- | --- |
| O(1) | Accessing an array index | Constant time |
| O(log n) | Binary search | Logarithmic |
| O(n) | Linear search | Scales directly |
| O(n log n) | Merge sort | Efficient sorting |
| O(n²) | Bubble sort | Nested loops |
| O(2ⁿ) | Recursive subset generation | Exponential |

## 🛠️ Real-World Examples
- Google Search → PageRank (graph-based algorithm)
- Spotify Recommendations → Collaborative filtering algorithms
- GPS Routing → Dijkstra’s Algorithm
- Bank Fraud Detection → Pattern recognition algorithms
- Healthcare Diagnosis → Decision tree + neural nets

## 🧪 Sample Algorithm (Pseudocode: Linear Search)
```text
function linearSearch(list, target):
  for each item in list:
    if item == target:
      return index
  return -1
```

## 🧭 Related Topics
- "Data Structures"
- "Machine Learning Fundamentals"
- "Algorithmic Complexity & Optimization"
- "Turing Machines & Computability"
- "Pseudocode vs Code"

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
