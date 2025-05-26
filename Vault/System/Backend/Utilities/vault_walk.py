"""
🚶 Vault Walk Utility
Walks the vault structure and yields all markdown file paths.
"""

import os

def walk_vault(base_path):
    for root, dirs, files in os.walk(base_path):
        for f in files:
            if f.endswith('.md'):
                yield os.path.join(root, f)
