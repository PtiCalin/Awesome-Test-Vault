"""
📄 Summary Engine
Heuristically generates a summary field for markdown files.
"""

def generate_summary_from_text(text, max_length=500):
    import re
    # Remove Markdown formatting and reduce to clean text
    clean_text = re.sub(r"(\[.*?\]\(.*?\))|(```.*?```)|(`.*?`)|(^#.*$)", "", text, flags=re.MULTILINE|re.DOTALL)
    paragraphs = [p.strip() for p in clean_text.split("\n") if p.strip()]
    summary = " ".join(paragraphs[:3])
    return summary[:max_length] + ("..." if len(summary) > max_length else "")
