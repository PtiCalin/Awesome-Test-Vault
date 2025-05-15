#!/bin/bash

# 📜 Bash Changelog Watcher Script
# Appends a changelog entry to markdown files with a new version in YAML frontmatter

VAULT_DIR="./your_vault_path_here"  # Update this to your vault path
TODAY=$(date +%Y-%m-%d)
CHANGELOG_HEADING="## 🔄 Change Log"
VERSION_REGEX='version:\s*["\'']?([0-9]+\.[0-9]+)["\'']?'

# Loop through markdown files
find "$VAULT_DIR" -type f -name "*.md" | while read -r file; do
  if grep -q "^version:" "$file"; then
    current_version=$(grep -oP "$VERSION_REGEX" "$file" | grep -oP "[0-9]+\.[0-9]+")
    
    if [ -z "$current_version" ]; then
      continue
    fi

    # Check if the changelog section exists
    if ! grep -q "$CHANGELOG_HEADING" "$file"; then
      echo -e "\n$CHANGELOG_HEADING\n\n| Version | Date       | Notes                       |\n|---------|------------|-----------------------------|" >> "$file"
    fi

    # Check if the current version is already in the changelog
    if ! grep -q "| $current_version |" "$file"; then
      echo "| $current_version | $TODAY | Auto-logged version update. |" >> "$file"
      echo "✅ Changelog updated in: $file"
    fi
  fi
done