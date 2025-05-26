"""
🔗 Link Mapper
Maps "related" files based on title, id, alias, or backlinks.
"""

import os
import re

def find_related(file_text, vault_files):
    related = set()
    for vf in vault_files:
        with open(vf, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            if any(token in content for token in extract_reference_tokens(file_text)):
                related.add(vf)
    return list(related)

def extract_reference_tokens(text):
    return list(set(re.findall(r'\b\w{4,}\b', text.lower())))
