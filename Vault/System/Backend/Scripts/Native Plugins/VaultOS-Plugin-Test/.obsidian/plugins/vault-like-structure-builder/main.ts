import { Plugin } from 'obsidian';

export default class VaultStructureBuilder extends Plugin {
  async onload() {
    this.addCommand({
      id: 'generate-vault-structure',
      name: '🧱 Generate Vault Structure',
      callback: () => this.buildStructure(),
    });

    console.log('✅ VaultStructureBuilder plugin loaded');
  }

  onunload() {
    console.log('❌ VaultStructureBuilder plugin unloaded');
  }

  buildStructure() {
    const vault = this.app.vault;
    const folders = [
    "VAULT"
    "VAULT/Files and media"
    "VAULT/Files and media/Audio"
    "VAULT/Files and media/Documents"
    "VAULT/Files and media/Images"
    "VAULT/Files and media/Other Media"
    "VAULT/Files and media/Video"
    "VAULT/Files and media/Web Clippings"
    "VAULT/Notes"
    "VAULT/Notes/Areas"
    "VAULT/Notes/Calendar"
    "VAULT/Notes/Daily Notes"
    "VAULT/Notes/Journaling"
    "VAULT/Notes/Meeting Notes"
    "VAULT/Notes/People"
    "VAULT/Notes/Projects"
    "VAULT/System"
    "VAULT/System/Backend"
    "VAULT/System/Backend/Configuration"
    "VAULT/System/Backend/Data Models"
    "VAULT/System/Backend/Logs"
    "VAULT/System/Backend/Metadata"
    "VAULT/System/Backend/Scripts"
    "VAULT/System/Backend/Utilities"
    "VAULT/System/Frontend"
    "VAULT/System/Frontend/Dashboard"
    "VAULT/System/Frontend/Snippets"
    "VAULT/System/Frontend/Templates"
    "VAULT/System/Frontend/Themes"
    "VAULT/System/Frontend/UX"
    "VAULT/System/Middleware"
    "VAULT/System/Documentation and Meta"
    "VAULT/System/Documentation and Meta/README.md"
    ];

    folders.forEach(async path => {
      try {
        await vault.createFolder(path);
        const name = path.split('/').pop();
        const content = `---
id: ${name?.toLowerCase() || 'section'}.md
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
created: ${new Date().toISOString().split('T')[0]}
updated: ${new Date().toISOString().split('T')[0]}
summary: "Folder note for ${name} section."
parent: ""
children: []
friends: []
related: []
---

> [!nav] 🧱 Vault Navigation  
> [[🖼 Media Gallery]] • [[🗓 Daily Notes]] • [[📚 Encyclopedia]] • [[🧠 Learnings]] • [[⛮ System]]

## ✍️ Content Title

<!-- Add content in this section -->

---`;
        const notePath = path + '/' + name + '.md';
        if (!vault.getAbstractFileByPath(notePath)) {
          await vault.create(notePath, content);
        }
      } catch (err) {
        console.error(`Failed to create ${path}`, err);
      }
    });
  }
}
