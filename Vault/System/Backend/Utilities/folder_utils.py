"""
📁 Folder Utilities
Helper functions to work with folder layers and indexes.
"""

import os

def get_folder_levels(filepath, base_path):
    rel_path = os.path.relpath(filepath, base_path)
    parts = rel_path.split(os.sep)
    return parts[:-1]  # exclude file itself

def get_folder_name(filepath):
    return os.path.basename(os.path.dirname(filepath))

def has_index_file(folder_path):
    return any(f in ["index.md", "_index.md", "README.md"] for f in os.listdir(folder_path))
