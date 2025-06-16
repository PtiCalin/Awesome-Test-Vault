---
# 📄 Identity & Classification
id: data-structures
title: "Data Structures"
aliases: ["Structures de Données"]
tags: [data-structures, computing, programming, algorithms]
author(s): ["Charlie Bouchard"]
element: concept
type: note
category: Computing and AI
section: Core Concepts
topic: Data Architecture
role: Reference
folder: "Personal Encyclopedia/Science and Technology/Computing and AI"
version: 1.1

# 📊 Status & Lifecycle
status: stable
visibility: public
created: 2025-06-08
updated: 2025-06-16

# 📚 Context & Description
summary: >
  A data structure is a specialized format for organizing, storing, accessing, and modifying data.
  It determines how efficiently a program can solve problems or scale with increased input.

# 🧱 Relationships
parent: "Computing and AI"
children: ["Big O Notation", "Algorithms"]
friends: ["Abstract Data Types", "Object-Oriented Programming"]
related: ["Data Types", "Memory Management"]
---

# 🧱 Data Structures

## 🧭 Summary
A data structure is a way of organizing, storing, and accessing data in a computer so it can be used efficiently. It’s the internal architecture behind every program’s logic—from simple calculators to high-frequency trading systems.

Data structures determine how data is held and how efficiently it can be accessed, modified, traversed, or deleted.

## 🧠 Core Concepts
ConceptDescription
Data StructureA model that defines how data is organized and manipulated
Linear vs Non-LinearLinear: elements in sequence (e.g., array); Non-linear: hierarchical or interconnected (e.g., tree, graph)
Static vs DynamicStatic: fixed-size (e.g., array); Dynamic: grows/shrinks during runtime (e.g., linked list)
Abstract Data Type (ADT)A theoretical concept like Stack, Queue, List—defined by behavior, not implementation
Time & Space ComplexityDescribes resource use of operations (see Big O Notation)

## 📦 Types of Data Structures
### 🔹 Linear Structures
Array: Fixed-size, index-based collection

Linked List: Nodes with pointers to next (or previous)

Stack: LIFO structure (used in backtracking, parsing)

Queue: FIFO structure (used in task scheduling)

Deque: Double-ended queue

Circular Buffer: Fixed-size queue with wraparound (useful in streaming data)

### 🔸 Non-Linear Structures
Tree: Hierarchical structure (e.g., file systems, DOM)

Binary Tree, BST, AVL Tree, Red-Black Tree

Heap: Special tree used for efficient min/max retrieval (used in priority queues)

Graph: Nodes (vertices) and edges; used in routing, relationships, and AI planning

Can be directed/undirected, weighted/unweighted, cyclic/acyclic

## 🛠️ Specialized & Advanced Structures
StructureDescriptionExample Use
Hash Table / Hash MapKey-value pairs with fast access via hashingDictionaries, caches
SetUnordered, no duplicatesMembership checks
Trie (Prefix Tree)Tree where nodes store prefixesAutocomplete, spell-check
Matrix / Grid2D array representationGame boards, image pixels
Skip ListOrdered structure with fast search via layered linksConcurrent data access
Bloom FilterProbabilistic structure for membership testingCache/memory optimization
Disjoint Set (Union-Find)Tracks components in a partitioned setNetwork connectivity, Kruskal's algorithm

## 🧪 Code Example: Stack in Python
```python
stack = []
stack.append('a')  # push
stack.append('b')
print(stack.pop())  # pop ➜ 'b'
```

## ⏱️ Big O Cheatsheet
OperationArrayLinked ListStack/QueueHash TableBST*
AccessO(1)O(n)O(n)O(1)O(log n)
SearchO(n)O(n)O(n)O(1)O(log n)
Insert/DeleteO(n)O(1)**O(1)O(1)O(log n)

Balanced BST (e.g., AVL or Red-Black Tree)
** If pointer/reference to position is known

## 🧩 Real-World Applications
Stacks: Undo in text editors, expression parsing, backtracking algorithms

Queues: OS job scheduling, customer support systems

Trees: UI layout rendering, compiler syntax trees, routing tables

Graphs: Social networks, transportation systems, neural networks

Hash Tables: Language interpreters, databases, caches

Tries: Search engines, predictive text input, IP routing

## 🧬 Related Topics
[[Big O Notation]]

[[Algorithms]]

[[Object-Oriented Programming (OOP)]]

[[Data Types vs Data Structures]]

[[Memory Management]]

[[Recursion & Tree Traversals]]
