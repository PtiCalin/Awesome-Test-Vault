---
# 📄 Identity & Classification
id: yaml
title: "Yaml"
aliases: ["About Yaml"]                          # Alternate titles
tags: [yaml

]                                    # Key terms
author(s):                           # Lists contributors (Default: PtiCalin)
element: 
type: <% type %>
category: 
section:
topic: 
role: 
folder: 
tags: []
version: 1.3                         # (Default 1.0)

# 📊 Status & Lifecycle
status: <% status %>                 # draft, in progress, complete, archived (Default: Draft)
visibility: <% visibility %>         # public, private (Default: public)
created: <% today %>
updated: <% today %>

# 📚 Context & Description
summary: ""

# 🧱 Relationships
parent: ""                           # One parent
children: []                         # Ordered or unordered children
friends: []                          # Related items of similar nature
related: []                          # General related content
---

> [!nav] 🧱 Vault Navigation
<!-- Relative Nav Bars -->
<!-- Notes -->
<!-- Learnings -->
<!-- Libraries -->
<!-- System -->

## ✍️ 🧠 YAML – Yet Another Markup Language

### 🧾 Overview

YAML (rhymes with "camel") stands for YAML Ain't Markup Language. It’s a human-readable data serialization language commonly used for configuration files, data exchange, and applications that require structured input/output. Unlike XML or JSON, YAML prioritizes simplicity and readability.

---

### 🛠️ Core Characteristics

- File Extension: .yaml or .yml
- Syntax Style: Indentation-based (uses spaces, not tabs)
- Data Types Supported: Strings, numbers, booleans, arrays (sequences), dictionaries (mappings), nulls
- Main Purpose: Data configuration and serialization

---

### 🧱 Basic Syntax Elements

🔹 Key-Value Pair (Mapping)

```yaml
name: PtiCalin
language: YAML
```

🔹 Lists (Sequence)

```yaml
tools:
  - GitHub
  - Obsidian
  - VS Code
```

🔹 Nested Structures

```yaml
user:
  name: PtiCalin
  projects:
    - VaultOS
    - Veridonia
```

🔹 Multiline Strings

```yaml
bio: >
  YAML is easy to read,
  supports multiline values,
  and is used everywhere.
```

🔹 Comments

```yaml
# This is a comment
```

### 🧾 YAML Syntax Cheatsheet

#### Quick Summary
YAML (YAML Ain’t Markup Language) is a human-readable data serialization format used for config files and data exchange.

#### Core Concepts
- **Key-Value Pairs**: Basic unit, like a dictionary.
- **Indentation**: Uses spaces (not tabs!) to nest.
- **Lists**: Use `-` to denote list items.
- **Scalars**: strings, integers, booleans.

#### Syntax Examples

```yaml
name: PtiCalin
projects:
  - VaultOS
  - Veridonia
features:
  automation: true
  plugins:
    count: 7
    custom: yes
```

#### Tips & Tools
- Strings with special characters: use quotes
- Use `---` to denote the start of a YAML doc
- Multiline strings: use `|` (literal) or `>` (folded)

#### Gotchas
- Don’t mix tabs and spaces
- Don’t forget colons `:` and indent levels
- Booleans like `yes` / `no` might be interpreted as strings or truthy values

#### Related
- [[Obsidian YAML Templates]]
- [[Frontmatter Metadata]]
- [[JSON vs YAML]]

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
