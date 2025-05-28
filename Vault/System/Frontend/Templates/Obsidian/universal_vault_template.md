---
# 📄 Identity & Classification
id: <% title.toLowerCase().replaceAll(" ", "-") %>
title: "<% title %>"
aliases: []                          # Alternate titles
tags: []                             # Key terms
author(s):                           # Lists contributors (Default: PtiCalin)
version: 1.3                         # (Default 1.0)

# 📊 Status & Lifecycle
status: <% status %>                 # draft, in progress, complete, archived (Default: draft)
visibility: <% visibility %>         # public, private (Default: public)
created: <% tp.date.now("YYYY-MM-DD") %>                  
updated: <% tp.date.now("YYYY-MM-DD") %>

# 📚 Context & Description
summary: ""

# 🧱 Relationships
element: <% tp.file.folder(true).split("/")[1] %>         # 1st layer (Media, Note, Learning, System)
type: <% tp.file.folder(true).split("/")[2] %>            # 2nd layer
category: <% tp.file.folder(true).split("/")[3] %>        # 3rd layer
section: <% tp.file.folder(true).split("/")[4] %>         # 4th layer
topic: <% tp.file.folder(true).split("/")[5] %>           # 5th layer
parent: ""                           # One parent
children: []                         # Ordered or unordered children
siblings: []                         # Notes in the same layer
friends: []                          # Thematically or functionally connected
---

<%* 
let layer1 = tp.file.folder(true).split("/")[1];
let nav = "";
switch(layer1) {
  case "Notes":
    nav = "> [!map] 🗺 Notes Navigation\n[[Awesome-Test-Vault.md|🏡 Home]] • [[📚 Encyclopedia]] • [[Notes/Projects/Projects.md|📁 Projects]] • [[Notes/Calendar/Calendar.md|📆 Calendar]] • [[Notes/People/People.md|👥 People]]";
    break;
  case "Learning":
    nav = "> [!map] 🧠 Learnings Navigation\n[[Awesome-Test-Vault.md|🏡 Home]] • [[Learning/Progress.md|📈 Progress]] • [[Learning/Nuggets.md|💎 Nuggets Bank]] • [[Learning/Skill Tree.md|🌳 Skill Tree]]";
    break;
  case "Media":
    nav = "> [!map] 🖼 Media Navigation\n[[Awesome-Test-Vault.md|🏡 Home]] • [[Media/Images.md|🖼 Images]] • [[Media/Audio.md|🎵 Audio]] • [[Media/Documents.md|📄 Docs]]";
    break;
  case "System":
    nav = "> [!map] ⚙️ System Navigation\n[[Awesome-Test-Vault.md|🏡 Home]] • [[System/Backend.md|🧱 Backend]] • [[System/Frontend.md|🎨 Frontend]] • [[System/Middleware.md|🔌 Middleware]]";
    break;
  default:
    nav = "> [!map] Navigation\n[[Awesome-Test-Vault.md|🏡 Home]] •  > [[Files and Media.md|🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[🧠 Learnings]] • [[⚙️ System]]
";
}
%>
<%- nav %>

---

## <% title %>

<!-- Add content in this section -->

---

## 🔗 Related Notes

> [!info] 🧠 Relationships  
> This note is part of a larger structure. Below are its connections:

```dataview
table
  parent as "Parent",
  children as "Subpages",
  siblings as "Siblings",
  friends as "Friends"
from ""
where file.link = this.file.link
```
---
