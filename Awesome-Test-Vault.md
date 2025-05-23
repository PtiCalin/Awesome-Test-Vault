---
id: vault-map-homepage
created: 2025-05-22
tags:
  - homepage
  - interactive
  - vault-map
  - dashboard
  - MOC
---

# 🏰 Welcome to the Vault

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
> _This homepage will soon feature status indicators, hover tooltips, last update dates, and active quest previews._
