import os
import yaml
import re
import csv
import argparse

# Parse command line arguments for the vault path
parser = argparse.ArgumentParser(description="Map metadata from an Obsidian vault")
parser.add_argument("vault_path", nargs="?", help="Path to the vault to scan")
args = parser.parse_args()

if args.vault_path:
    vault_path = args.vault_path
else:
    parser.error("vault_path argument is required. Provide the path to your vault.")

# Prepare output data
metadata_log = []

# Walk through all markdown files
for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, vault_path)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Extract YAML frontmatter
                    match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
                    if match:
                        frontmatter = yaml.safe_load(match.group(1))
                        if isinstance(frontmatter, dict):
                            metadata = {
                                "file": rel_path,
                                "id": frontmatter.get("id", ""),
                                "title": frontmatter.get("title", ""),
                                "type": frontmatter.get("type", ""),
                                "role": frontmatter.get("role", ""),
                                "section": frontmatter.get("section", ""),
                                "category": frontmatter.get("category", ""),
                                "folder": frontmatter.get("folder", ""),
                                "status": frontmatter.get("status", ""),
                                "visibility": frontmatter.get("visibility", ""),
                                "created": frontmatter.get("created", ""),
                                "updated": frontmatter.get("updated", "")
                            }
                            metadata_log.append(metadata)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Define output CSV path
csv_output_path = "vault-metadata-log.csv"

# Write to CSV
with open(csv_output_path, "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["file", "id", "title", "type", "role", "section", "category", "folder", "status", "visibility", "created", "updated"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in metadata_log:
        writer.writerow(row)

print(f"Metadata log saved to: {csv_output_path}")
