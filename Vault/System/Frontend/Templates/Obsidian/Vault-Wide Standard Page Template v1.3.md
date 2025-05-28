---
# 📄 Identity & Classification
id: <% title.toLowerCase().replaceAll(" ", "-") %>
title: "<% title %>"
aliases: []                          # Alternate titles
tags: [

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

## ✍️ [Content Title]

<!-- Add content in this section -->

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

---
