import os
import re
from pathlib import Path
from datetime import date

# Configuration
VAULT_DIR = Path("your_vault_path_here")  # <-- Update to your vault root path
CHANGELOG_HEADING = "## 🔄 Change Log"
TODAY = date.today().isoformat()

def extract_version(yaml_text):
    match = re.search(r'version:\s*["\']?(\d+\.\d+(?:\.\d+)?)["\']?', yaml_text)
    return match.group(1) if match else None

def extract_changelog_versions(text):
    changelog_versions = []
    lines = text.splitlines()
    in_log = False
    for line in lines:
        if CHANGELOG_HEADING in line:
            in_log = True
            continue
        if in_log:
            match = re.match(r"\|\s*(\d+\.\d+)\s*\|", line)
            if match:
                changelog_versions.append(match.group(1))
    return changelog_versions

def append_changelog_if_needed(file_path):
    content = file_path.read_text(encoding="utf-8")
    if "---" not in content:
        return  # Skip non-YAML files

    yaml_block = content.split("---")[1]
    current_version = extract_version(yaml_block)
    if not current_version:
        return

    changelog_versions = extract_changelog_versions(content)
    if current_version in changelog_versions:
        return  # Already logged

    log_entry = f"| {current_version} | {TODAY} | Auto-logged version update. |"

    if CHANGELOG_HEADING not in content:
        content += f"\n\n{CHANGELOG_HEADING}\n\n| Version | Date       | Notes                       |\n|---------|------------|-----------------------------|\n"

    content += f"\n{log_entry}\n"
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Updated changelog in: {file_path.name}")

def run():
    for md_file in VAULT_DIR.rglob("*.md"):
        append_changelog_if_needed(md_file)

if __name__ == "__main__":
    run()