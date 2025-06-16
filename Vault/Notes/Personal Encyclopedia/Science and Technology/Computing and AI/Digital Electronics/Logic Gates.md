---
title: "Logic Gates"
created: 2025-04-30
type: note
tags: [note, Digital Electronics]
parent: "Digital Electronics"
children: []
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

## 🔗 Related Topics
- "Digital Circuits"
- "Boolean Algebra"
- "Flip-Flops and Registers"
- "Combinational vs Sequential Logic"
