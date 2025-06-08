# 🤖 AGENT.md – PtiCalin Code Standards for `system/meta/`

Welcome to the **PtiCalin Code Standards** for the `system/meta/` section of the **Awesome Test Vault**. This file acts as your official briefing, agent Codex, for aligning all scripts and system metadata to the PtiCalin coding style. 🧸

---

## 🧠 PHILOSOPHY

> "Code should be readable, reusable, and a little bit magical."

The PtiCalin standard emphasizes:
- ✨ *Emotional clarity* — Code that calms.
- 🧩 *Modularity* — Single-purpose, stackable components.
- 🧃 *Self-sufficiency* — Each script runs alone, but thrives with others.
- 🕊 *Forgiveness* — Errors are helpful, not scolding.
- 🧠 *Narrative structure* — Comments and layout follow a story arc.
- 🌌 *Expansiveness* — Systems should be designed with future growth in mind.
- 👤 *User-Focused Functionality* — Features serve real needs clearly and accessibly.
- ⚙️ *Optimization* — Efficient performance without sacrificing readability.
- 🔐 *Security* — Avoid risky shortcuts and guard data integrity.
- 🧪 *Test Support* — Include testability in structure and logic by design.

---

## 🧸 GENERAL STYLE

### 🧾 Naming Conventions
- snake_case for Python; camelCase for JS.
- Be expressive and gentle: `gather_vault_stats.py`, `sync_index_map.ts`.
- Prefix standalone utilities with action verbs: `parse_`, `generate_`, `summon_`, `nudge_`, `align_`, etc.

### 📐 File Structure
- Start with a title comment block that includes:
  - File name
  - Purpose
  - Dependencies
  - Example output or behavior (if applicable)

```python
# === generate_vault_manifest.py ===
# Purpose: Traverse vault structure and compile a manifest.json file
# Dependencies: os, json, vault_config.yaml
# Output: /system/meta/manifest.json
```

### 🧩 Sectioning
Use block dividers and headers like:
```python
# === CONFIGURATION ===
# === DATA LOADING ===
# === MAIN EXECUTION ===
# === OUTPUT ===
```

---

## 🧃 FUNCTION DESIGN

### ✨ Self-Documenting
- Function names should tell a story.
- Prefer verbose and expressive over clever.
- Use clear input/output behavior. Add docstrings that include:
  - What it does
  - Input/Output
  - Optional emoji if helpful 🛠️

```python
def sync_vault_metadata(vault_path: str) -> dict:
    """
    🧠 Syncs all metadata files in the vault structure.

    Args:
        vault_path (str): Path to the base vault directory.

    Returns:
        dict: Compiled metadata tree.
    """
```

---

## 🎯 ERROR HANDLING

- Always offer actionable messages with a positive tone.
- Use emoji or icons to help differentiate levels of urgency:
  - ⚠️ Warning
  - ❌ Error
  - ✅ Success

```python
if not os.path.exists(config_file):
    raise FileNotFoundError(
        f"⚠️ Config file not found at {config_file}.\n"
        "💡 Try running `generate_default_config()` first."
    )
```

---

## 🧪 TESTING & OUTPUT

- Include `--dry-run` flags or modes whenever possible.
- Offer sample console output in comments if non-obvious.
- Be verbose in CLI logs, especially for multi-step processes.

```bash
🌱 Initializing vault metadata...
📚 7 modules detected
📦 Manifest updated: 2025-06-08 14:22
✅ All systems operational
```

---

## 🧵 CODING WITH CONTEXT

All `system/meta/` scripts should:
- Assume coexistence with VaultOS
- Respect shared folder schemas
- Log to `/system/logs/` if applicable
- Use YAML for config and JSON for outputs
- Tag outputs with vault build timestamp (UTC)

---

## 🛠️ META-SYSTEM INTEGRATION

When integrating new scripts:
- Place reusable logic in `utils/`
- Document expected inputs/outputs in a `.meta.md` sidecar file
- Register components to the central registry: `meta_index.yaml`
- If relevant, update: `manifest.json`, `vault_schema.yaml`, or `vault_diagram.svg`

---

## 🌟 CONTRIBUTING TONE

- Code should feel like it’s on your side.
- Humor is optional, gentleness is not.
- When in doubt, imagine a tired, overwhelmed developer discovering this file at 2AM. Help them feel safe, seen, and ready.

---

🧸 **End of Agent Briefing**

Proceed with elegance, Codex. Your scripts are the threads that hold the Vault together.

> "Be modular, be kind, and leave good breadcrumbs." 🍞
