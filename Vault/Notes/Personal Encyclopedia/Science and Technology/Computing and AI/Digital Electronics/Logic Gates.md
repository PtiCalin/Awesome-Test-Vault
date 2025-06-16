---
# 📄 Identity & Classification
id: logic-gates
title: "Logic Gates"
aliases: []
tags: [logic-gates, digital-electronics]
author(s):
element:
type: note
category:
section:
topic:
role:
folder:
tags: []
version: 1.3

# 📊 Status & Lifecycle
status: draft
visibility: public
created: 2025-04-30
updated: 2025-04-30

# 📚 Context & Description
summary: "Logic gates are the fundamental building blocks of digital electronics."

# 🧱 Relationships
parent: "Digital Electronics"
children: []
friends: []
related: []
---
# ⚙️ Logic Gates

## 🧭 Summary
Logic gates are the fundamental building blocks of digital electronics. They process binary inputs to produce specific binary outputs, enabling all forms of digital computation and control.

## 🧠 Core Concepts
| Concept | Description |
| --- | --- |
| Binary | System with two discrete states, typically 0 and 1 |
| Truth Table | Chart that lists outputs for every possible input combination |
| Combinational Logic | Gates that produce outputs based solely on current inputs |
| Sequential Logic | Circuits with memory of past inputs (e.g., flip-flops) |

## 🔑 The Seven Basic Gates
1. **AND** – Output is 1 only if *all* inputs are 1.
2. **OR** – Output is 1 if *any* input is 1.
3. **NOT** – Inverts the input (also called an inverter).
4. **NAND** – NOT + AND; output is 0 only if all inputs are 1.
5. **NOR** – NOT + OR; output is 1 only if all inputs are 0.
6. **XOR** – "Exclusive OR"; output is 1 if inputs differ.
7. **XNOR** – "Exclusive NOR"; output is 1 if inputs are the same.

## 🔧 Example Circuit
A **half adder** combines an XOR gate for the sum and an AND gate for the carry. It adds two single binary digits to produce a 2-bit result.

## 🎯 Common Use Cases
- Building arithmetic logic units (ALUs)
- Implementing memory and storage elements
- Creating timers, counters, and control logic
- Designing digital signal processing chains

## 🏗️ Implementation Platforms
- **TTL (Transistor–Transistor Logic)** and **CMOS** integrated circuits
- **Field Programmable Gate Arrays (FPGAs)** for configurable logic
- **Microcontrollers** for embedded control

## 🐍 Python Example
```python
# Simple demonstration of logic gates using Python
A = True
B = False
print("AND:", A and B)
print("OR:", A or B)
print("XOR:", A ^ B)
```

## 🔌 Logic Gates Cheatsheet

### 🔤 Quick Summary
Logic gates are the basic building blocks of digital circuits. Each gate performs
a simple logical function on one or more binary inputs (0 or 1) to produce a single
binary output.

### 🧠 Core Concepts
| Gate | Symbol | Function |
|------|--------|---------------------------------|
| AND  | ∧      | Output is 1 only if both are 1 |
| OR   | ∨      | Output is 1 if *either* is 1 |
| NOT  | ¬      | Inverts input: 1 → 0, 0 → 1 |
| NAND | ↑      | NOT + AND: Output is 0 only if both are 1 |
| NOR  | ↓      | NOT + OR: Output is 1 only if both are 0 |
| XOR  | ⊕      | Output is 1 if inputs are *different* |
| XNOR | ⊙      | Output is 1 if inputs are *equal* |

### 📐 Truth Tables

#### AND (A ∧ B)
| A | B | A ∧ B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

#### OR (A ∨ B)
| A | B | A ∨ B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

#### NOT (¬A)
| A | ¬A |
|---|----|
| 0 | 1 |
| 1 | 0 |

### 🧰 Logic Gate Shortcuts
- **Boolean Algebra Notation**:
  AND = `A·B` or `AB`
  OR = `A + B`
  NOT = `A̅` or `¬A`
- **Symbols in Circuit Diagrams**:
  - USA uses IEC/ANSI symbols (rectangle with label)
  - EU uses IEC shapes (distinct curved and triangle shapes)

### 💡 Gotchas & Pitfalls
- XOR ≠ OR → XOR excludes the case when both inputs are 1.
- NAND and NOR are *functionally complete* — any circuit can be built with just
  NAND or NOR gates.
- Don’t confuse the *inverted output* of NOR/NAND with the input side — placement
  of the NOT circle matters!

### 🔗 Related
- [[Boolean Algebra]]
- [[Truth Tables]]
- [[Transistors and Digital Circuits]]
- [[Computing and AI]]
- [[Hardware Fundamentals]]

## 🔗 Related Topics
- "Digital Circuits"
- "Boolean Algebra"
- "Flip-Flops and Registers"
- "Combinational vs Sequential Logic"

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

---
