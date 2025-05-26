"""
🔤 Slugify Utility
Converts a string (e.g., file title) into a slug-safe ID.
"""

import re

def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')
