class VaultOS {
  constructor() {
    this.registry = {};
  }

  async onload() {
    console.log("VaultOS v0.3.0 loading...");
    this.injectStyles();
    this.createHUD();
    this.registerVaultComponent("VaultMap", null);
    console.log("VaultOS is ready.");
  }

  registerVaultComponent(name, component) {
    this.registry[name] = component;
    console.log(`[VaultOS] Registered: ${name}`);
  }

  injectStyles() {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = this.app.vault.adapter.getResourcePath(this.manifest.dir + "/styles.css");
    document.head.appendChild(link);
    console.log(`[VaultOS] Stylesheet injected from: ${link.href}`);
  }

  createHUD() {
    const hud = document.createElement("div");
    hud.className = "vaultos-hud";
    hud.innerHTML = `
      <div class="vaultos-hud-item">
        <span class="vaultos-hud-icon">🧠</span>
        <span class="vaultos-hud-label">Vault:</span>
        <span class="vaultos-hud-value">${this.app.vault.getName()}</span>
      </div>
    `;
    document.body.appendChild(hud);
  }

  get(name) {
    return this.registry[name];
  }

  getMarkdownFilesByTag(tag) {
    return this.app.vault.getMarkdownFiles().filter(file => {
      const cache = this.app.metadataCache.getFileCache(file);
      return cache?.frontmatter?.tags?.includes(tag);
    });
  }
}

module.exports = VaultOS;
