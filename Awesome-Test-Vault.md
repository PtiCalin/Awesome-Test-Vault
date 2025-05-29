---
# 📄 Identity & Classification
id: vault-map-homepage
title: "🏰 Welcome to the Vault"
aliases: []
type: note
category: vault
section: structure
role: homepage
folder: system
tags: [homepage, interactive, vault-map, dashboard, MOC]
version: 1.2

# 📊 Status & Lifecycle
status: in progress
visibility: public
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>

# 📚 Context & Description
summary: "Landing page and map for navigating the Awesome-Test-Vault, featuring dynamic visual overlays and interactive dashboards."

# 🧱 Relationships
parent: ""
children: []
friends: []
related: []
---

> [!map] Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[🧠 Learnings]] • [[⛮ System]]

## 🏰 Welcome to the Vault

> _A living map of your mind – click the glowing districts to explore your knowledge city._

<div id="vault-map-wrapper">
  <img id="vault-map" src="Files and Media/Images/Vault Overview/vault-map.png" style="width:100%; border-radius: 10px;" />
</div>

```dataviewjs
const { VaultMap } = await cJS();
const map = new VaultMap({ vaultName: "Awesome-Test-Vault" });

function runWhenImageReady() {
  const img = document.getElementById("vault-map");
  if (!img || !img.complete) {
    setTimeout(runWhenImageReady, 50);
    return;
  }
  map.renderMap();
}

runWhenImageReady();
```

---

## 🧭 Vault OS Navigation Dashboard

```folder-index-content
```

---

## 🔧 Under Construction

> _This homepage will  feature status indicators, hover tooltips, last update dates, and active quest previews._

---

## 🔗 Related Notes

> [!rel] Relationships  
> This note is part of a larger structure. Below are its connections:

```dataviewjs
const { VaultMap } = await import("VaultMap.js");
const map = new VaultMap({ vaultName: "Awesome-Test-Vault" });

function runWhenImageReady() {
  const img = document.getElementById("vault-map");
  if (!img || !img.complete) {
    setTimeout(runWhenImageReady, 50);
    return;
  }
  map.renderMap();
}

runWhenImageReady();

table
  parent as "Parent",
  children as "Subpages",
  friends as "Friends",
  related as "Related"
from ""
where file.link = this.file.link
```
