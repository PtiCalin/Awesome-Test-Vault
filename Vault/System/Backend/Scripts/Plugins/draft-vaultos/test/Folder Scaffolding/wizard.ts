import { App, Modal, Plugin } from 'obsidian';

export class VaultOSWizardModal extends Modal {
  plugin: Plugin;

  constructor(app: App, plugin: Plugin) {
    super(app);
    this.plugin = plugin;
  }

  onOpen() {
    const { contentEl } = this;
    contentEl.createEl('h1', { text: '🔧 VaultOS Setup Wizard' });

    contentEl.createEl('p', { text: 'Choose a vault structure preset:' });

    ['standard', 'learning', 'dev', 'world'].forEach(preset => {
      const btn = contentEl.createEl('button', {
        text: `🧱 ${preset[0].toUpperCase() + preset.slice(1)}`
      });
      btn.classList.add('wizard-preset-button');
      btn.onclick = () => {
        console.log(`Preset selected: ${preset}`);
        this.close();
      };
    });
  }

  onClose() {
    this.contentEl.empty();
  }
}
