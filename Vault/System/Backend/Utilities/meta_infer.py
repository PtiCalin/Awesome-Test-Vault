"""
🧠 Metadata Inference
Infer type, element, category, etc. from path.
"""

def infer_metadata_from_path(path_parts):
    metadata = {}
    layers = ["type", "element", "category", "section", "topic"]
    for i, key in enumerate(layers):
        if i < len(path_parts):
            metadata[key] = path_parts[i]
    return metadata
