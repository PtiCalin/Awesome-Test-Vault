import os
from pathlib import Path
import re

root = Path('Vault/Notes/Personal Encyclopedia')

# slugify helper
_slug_re = re.compile(r'[^a-z0-9]+')

def slugify(text):
    text = text.lower()
    text = _slug_re.sub('-', text)
    return text.strip('-')

# simple YAML parser for this repo's straightforward front matter

def parse_yaml(text):
    data = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()
        if val.startswith('[') and val.endswith(']'):
            items = [v.strip().strip('"') for v in val[1:-1].split(',') if v.strip()]
            data[key] = items
        else:
            data[key] = val.strip('"')
    return data

# value formatter
_value_special = re.compile(r'[\s:#\[\],]')

def format_value(v):
    if isinstance(v, list):
        return '[' + ', '.join(v) + ']'
    if v == "":
        return '""'
    if _value_special.search(v):
        return f'"{v}"'
    return v

def build_yaml(data):
    lines = ['---']
    for k, v in data.items():
        lines.append(f"{k}: {format_value(v)}")
    lines.append('---')
    return '\n'.join(lines)

def update_file(path: Path):
    text = path.read_text()
    if not text.startswith('---'):
        return
    parts = text.split('---', 2)
    if len(parts) < 3:
        return
    front, body = parts[1], parts[2].lstrip('\n')
    old = parse_yaml(front)
    title = old.get('title', path.stem)
    created = old.get('created', '')
    parent = old.get('parent', '')
    children = old.get('children', [])
    tags = old.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip().strip('"') for t in tags.strip('[]').split(',') if t.strip()]
    dir_parts = path.parent.relative_to('Vault').parts
    element = dir_parts[0] if len(dir_parts) > 0 else ''
    typ = dir_parts[1] if len(dir_parts) > 1 else ''
    category = dir_parts[2] if len(dir_parts) > 2 else ''
    section = dir_parts[3] if len(dir_parts) > 3 else ''
    topic = dir_parts[4] if len(dir_parts) > 4 else ''
    new_data = {
        'id': slugify(title),
        'title': title,
        'aliases': [],
        'tags': tags,
        'author(s)': 'PtiCalin',
        'version': '1.3',
        'status': 'draft',
        'visibility': 'public',
        'created': created,
        'updated': created,
        'summary': '',
        'element': element,
        'type': typ,
        'category': category,
        'section': section,
        'topic': topic,
        'parent': parent,
        'children': children,
        'siblings': [],
        'friends': [],
    }
    new_front = build_yaml(new_data)
    path.write_text(new_front + '\n' + body)

for md in root.rglob('*.md'):
    update_file(md)
