import { Plugin } from "obsidian";
import { registerWatcher } from "./src/core/watcher";
import { registerModuleManagerView } from "./src/ui/view";

export default class VaultOSPlugin extends Plugin {
  async onload() {
    console.log("🧠 VaultOS kernel loaded");
    registerWatcher(this.app, this);
    registerModuleManagerView(this.app);
  }
}
