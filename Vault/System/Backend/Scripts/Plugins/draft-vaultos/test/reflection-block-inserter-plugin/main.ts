import { App, Plugin, PluginManifest, TFile, MarkdownView, Notice } from "obsidian";

export default class ReflectionBlockPlugin extends Plugin {
	async onload() {
		this.addCommand({
			id: "insert-random-reflection-block",
			name: "🪞 Insert Reflection Block",
			callback: () => this.insertReflectionBlock()
		});

		this.addRibbonIcon("document", "Insert Reflection Block", () => this.insertReflectionBlock());
	}

	async insertReflectionBlock() {
		const file = this.app.workspace.getActiveFile();
		const editor = this.app.workspace.getActiveViewOfType(MarkdownView)?.editor;
		if (!file || !editor) {
			new Notice("No active note found.");
			return;
		}

		const prompts = await this.loadPrompts();
		if (!prompts.length) {
			new Notice("No reflection prompts found.");
			return;
		}

		const prompt = prompts[Math.floor(Math.random() * prompts.length)];

		const block = `### 🪞 Reflection\n> Prompt: ${prompt}\n\n\\`\\`\\`reflection\n\n\\`\\`\\``;

		editor.replaceSelection(`\n\n${block}\n\n`);
		new Notice("Reflection block inserted 🪞");
	}

	async loadPrompts(): Promise<string[]> {
		try {
			const file = await this.app.vault.adapter.read("reflection-prompts.json");
			return JSON.parse(file);
		} catch (e) {
			console.error("Error reading reflection-prompts.json:", e);
			return [];
		}
	}
}