(() => {
  var __require = /* @__PURE__ */ ((x) => typeof require !== "undefined" ? require : typeof Proxy !== "undefined" ? new Proxy(x, {
    get: (a, b) => (typeof require !== "undefined" ? require : a)[b]
  }) : x)(function(x) {
    if (typeof require !== "undefined")
      return require.apply(this, arguments);
    throw Error('Dynamic require of "' + x + '" is not supported');
  });

  // main.ts
  var import_obsidian = __require("obsidian");
  var VaultStructureBuilder = class extends import_obsidian.Plugin {
    async onload() {
      this.addCommand({
        id: "generate-vault-structure",
        name: "\u{1F9F1} Generate Vault Structure",
        callback: () => this.buildStructure()
      });
      console.log("\u2705 VaultStructureBuilder plugin loaded");
    }
    onunload() {
      console.log("\u274C VaultStructureBuilder plugin unloaded");
    }
    buildStructure() {
      const vault = this.app.vault;
      const folders = [
        "VAULT/Files and media/Audio",
        "VAULT/Files and media/Documents",
        "VAULT/Files and media/Images",
        "VAULT/Files and media/Other Media",
        "VAULT/Files and media/Video",
        "VAULT/Files and media/Web Clippings",
        "VAULT/Notes/Areas",
        "VAULT/Notes/Calendar",
        "VAULT/Notes/Daily Notes",
        "VAULT/Notes/Journaling",
        "VAULT/Notes/Meeting Notes",
        "VAULT/Notes/People",
        "VAULT/Notes/Projects",
        "VAULT/System/Backend/Configuration",
        "VAULT/System/Backend/Data Models",
        "VAULT/System/Backend/Logs",
        "VAULT/System/Backend/Metadata",
        "VAULT/System/Backend/Scripts",
        "VAULT/System/Backend/Utilities",
        "VAULT/System/Frontend/Dashboard",
        "VAULT/System/Frontend/Snippets",
        "VAULT/System/Frontend/Templates",
        "VAULT/System/Frontend/Themes",
        "VAULT/System/Frontend/UX",
        "VAULT/System/Middleware",
        "VAULT/System/Documentation and Meta/readme"
      ];
      folders.forEach(async (path) => {
        try {
          await vault.createFolder(path);
          const name = path.split("/").pop();
          const content = `---
id: ${name?.toLowerCase() || "section"}.md
title: "${name}"
aliases: []
author: 
element: core
type: section
category: 
section: ${name}
topic: 
role: 
folder: ${name}
tags: []
version: 1.0
status: draft
visibility: private
created: ${(/* @__PURE__ */ new Date()).toISOString().split("T")[0]}
updated: ${(/* @__PURE__ */ new Date()).toISOString().split("T")[0]}
summary: "Folder note for ${name} section."
parent: ""
children: []
friends: []
related: []
---

> [!nav] \u{1F9F1} Vault Navigation  
> [[\u{1F5BC} Media Gallery]] \u2022 [[\u{1F5D3} Daily Notes]] \u2022 [[\u{1F4DA} Encyclopedia]] \u2022 [[\u{1F9E0} Learnings]] \u2022 [[\u26EE System]]

## \u270D\uFE0F Content Title

<!-- Add content in this section -->

---`;
          const notePath = path + "/" + name + ".md";
          if (!vault.getAbstractFileByPath(notePath)) {
            await vault.create(notePath, content);
          }
        } catch (err) {
          console.error(`Failed to create ${path}`, err);
        }
      });
    }
  };
})();
