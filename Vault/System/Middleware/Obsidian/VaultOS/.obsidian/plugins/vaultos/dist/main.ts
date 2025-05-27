import { Plugin } from 'obsidian';

export default class VaultOS extends Plugin {
  registry: Record<string, any> = {};

  async onload() {
    console.log('Initiating VaultOS');
    this.registerVaultComponent('VaultMap', null); // placeholder
  }

  registerVaultComponent(name: string, component: any) {
    this.registry[name] = component;
    console.log(`[VaultOS] Registered: ${name}`);
    this.registerDomEvent(document, "DOMContentLoaded", () => {
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = this.app.vault.adapter.getResourcePath(this.manifest.dir + "/styles.css");
      document.head.appendChild(link);
      console.log(`[VaultOS] Stylesheet loaded: ${link.href}`);
    });
    this.registerDomEvent(document, "click", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Clicked on: ${name}`);
        // Handle click event
      }
    }
    );
    this.registerDomEvent(document, "mouseover", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Mouseover on: ${name}`);
        // Handle mouseover event
      }
    }
    );
    this.registerDomEvent(document, "mouseout", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Mouseout from: ${name}`);
        // Handle mouseout event
      }
    }
    );
    this.registerDomEvent(document, "keydown", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Keydown on: ${name}`);
        // Handle keydown event
      }
    }
    );
    this.registerDomEvent(document, "keyup", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Keyup on: ${name}`);
        // Handle keyup event
      }
    }
    );
    this.registerDomEvent(document, "keypress", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Keypress on: ${name}`);
        // Handle keypress event
      }
    }
    );
    this.registerDomEvent(document, "focus", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Focus on: ${name}`);
        // Handle focus event
      }
    }
    );
    this.registerDomEvent(document, "blur", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Blur from: ${name}`);
        // Handle blur event
      }
    }
    );
    this.registerDomEvent(document, "change", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Change on: ${name}`);
        // Handle change event
      }
    }
    );
    this.registerDomEvent(document, "input", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Input on: ${name}`);
        // Handle input event
      }
    }
    );
    this.registerDomEvent(document, "submit", (event) => {
      if (event.target instanceof HTMLElement && event.target.classList.contains(name)) {
        console.log(`[VaultOS] Submit on: ${name}`);
        // Handle submit event
      }
    }
    );
  }
  get(name: string): any {
    return this.registry[name];
  }
  console.log('Your Vault is ready!');
}
