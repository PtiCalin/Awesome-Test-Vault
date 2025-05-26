"""
📄 YAML Tools
Read, write, and update YAML frontmatter in markdown files.
"""

import yaml

def extract_yaml_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) > 2:
            return yaml.safe_load(parts[1])
    return {}

def update_yaml_frontmatter(filepath, updates):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) > 2:
            current_yaml = yaml.safe_load(parts[1])
            current_yaml.update(updates)
            new_yaml = yaml.dump(current_yaml, allow_unicode=True)
            with open(filepath, 'w', encoding='utf-8') as f_out:
                f_out.write(f"---\n{new_yaml}---\n{parts[2]}")
