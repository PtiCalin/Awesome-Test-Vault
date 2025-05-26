"""
🏷️ Tag Suggester
Suggests tags for a file based on content and backlinks.
"""

import re
from collections import Counter

def suggest_tags(text, existing_tags=None, top_n=5):
    if existing_tags is None:
        existing_tags = []
    # Basic tokenizer: extract words
    words = re.findall(r'\b\w{4,}\b', text.lower())
    common_words = Counter(words).most_common()
    candidates = [word for word, _ in common_words if word not in existing_tags]
    return candidates[:top_n]
