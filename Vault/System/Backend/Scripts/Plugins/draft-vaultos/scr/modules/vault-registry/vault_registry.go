package main

import (
    "fmt"
)

type Plugin struct {
    ID       string
    Name     string
    Version  string
    Author   string
}

func main() {
    registry := []Plugin{
        {"vaultos-core", "VaultOS Core Plugin", "1.0.0", "PtiCalin"},
        {"plugin-template-obsidian", "Obsidian Plugin Template", "1.0.0", "PtiCalin"},
        {"vaultos-subplugin-template", "VaultOS Subplugin Template", "0.9.0", "PtiCalin"},
    }

    fmt.Println("🧠 VaultOS Plugin Registry")
    fmt.Println("==========================")
    for _, plugin := range registry {
        fmt.Printf("🔌 %s (%s) – v%s by %s\n", plugin.Name, plugin.ID, plugin.Version, plugin.Author)
    }
}
