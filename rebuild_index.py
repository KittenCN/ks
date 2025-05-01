#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild_nav.py

Traverses all subdirectories to find folders containing book.json and SUMMARY.md,
rebuilds a full SUMMARY.md including all nested SUMMARY.md files (recursively),
and updates the index HTML navigation menu based on the provided index_model.html template.

Usage:
    python rebuild_nav.py
"""
import os
import re

# Directories to skip during traversal
EXCLUDE_DIRS = {
    '_archive', 'drafts', '.git', '.github',
    'node_modules', 'build', 'dist', '_book', '_layouts',
    'lib', 'img', 'imgs'
}
# File names
ROOT_SUMMARY = 'SUMMARY.md'
INDEX_TEMPLATE = 'index_model.html'
OUT_SUMMARY = 'summary_auto_full.md'
OUT_INDEX = 'index_rebuild.html'
PROJECT_ROOT = os.getcwd()


def adjust_link(link_path, parent_dir):
    """
    Normalize markdown link path to a relative path (no './').
    External or absolute links unchanged.
    """
    if '://' in link_path or link_path.startswith(('/', '#')):
        return link_path
    abs_path = os.path.normpath(os.path.join(parent_dir, link_path))
    rel = os.path.relpath(abs_path, PROJECT_ROOT).replace('\\', '/')
    return rel.lstrip('./')


def adjust_md_links(text, parent_dir):
    """Adjust markdown links in a SUMMARY line."""
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  lambda m: f"[{m.group(1)}]({adjust_link(m.group(2), parent_dir)})",
                  text)


def get_file_depth(summary_path):
    """
    Compute directory depth of SUMMARY.md relative to project root.
    Root directory is depth 0.
    """
    dir_path = os.path.dirname(os.path.abspath(summary_path))
    rel = os.path.relpath(dir_path, PROJECT_ROOT)
    if rel == '.':
        return 0
    return len(rel.split(os.sep))


def extract_entries(summary_path, ignore_link=None):
    """
    Read SUMMARY.md and return list of (text, link) tuples.
    """
    entries = []
    parent_dir = os.path.dirname(summary_path)
    with open(summary_path, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*-\s+(.*)', line)
            if not m:
                continue
            raw = m.group(1).strip()
            adj = adjust_md_links(raw, parent_dir)
            link_m = re.search(r'\(([^)]+)\)', adj)
            link = link_m.group(1) if link_m else None
            if ignore_link and link == ignore_link:
                continue
            entries.append((adj, link))
    return entries


def build_entries(summary_path, ignore_link=None, visited=None):
    """
    Recursively build list lines using tab indentation per folder depth.
    """
    if visited is None:
        visited = set()
    real = os.path.realpath(summary_path)
    if real in visited:
        return []
    visited.add(real)

    depth = get_file_depth(summary_path)
    indent_tabs = '\t' * depth
    flat = []

    for text, link in extract_entries(summary_path, ignore_link):
        line = f"{indent_tabs}-\t{text}"
        flat.append(line)
        # recurse nested
        if link and not link.startswith(('http://', 'https://', '/', '#')):
            dirp = os.path.normpath(os.path.join(PROJECT_ROOT, os.path.dirname(link)))
            if os.path.basename(dirp) in EXCLUDE_DIRS:
                continue
            summary_file = os.path.join(dirp, ROOT_SUMMARY)
            book_file = os.path.join(dirp, 'book.json')
            if os.path.isdir(dirp) and os.path.exists(summary_file) and os.path.exists(book_file):
                flat.extend(build_entries(summary_file, ignore_link=link, visited=visited))
    return flat


def build_full_summary():
    root = os.path.join(PROJECT_ROOT, ROOT_SUMMARY)
    if not os.path.exists(root):
        raise FileNotFoundError(f"Root summary '{ROOT_SUMMARY}' not found.")
    header = []
    with open(root, encoding='utf-8') as f:
        first = f.readline()
        if first.startswith('#'):
            header.append(first.rstrip('\n'))
            header.append('')
    entries = build_entries(root)
    return header, entries


def convert_md_to_html(md_lines):
    html = ['<ul class="summary">']
    depth = 0
    for line in md_lines:
        # count leading tabs
        leading = len(line) - len(line.lstrip('\t'))
        level = leading
        while level < depth:
            html.append('  ' * depth + '</ul>')
            depth -= 1
        while level > depth:
            html.append('  ' * depth + '<ul>')
            depth += 1
        content = line.lstrip('\t')
        if not content.startswith('-\t'):
            continue
        content = content[2:]
        m = re.match(r'\[([^\]]+)\]\(([^)]+)\)', content)
        if m:
            title, link = m.group(1), m.group(2)
            html.append('  ' * (level + 1) + f'<li class="chapter"><a href="{link}">{title}</a></li>')
    while depth > 0:
        html.append('  ' * depth + '</ul>')
        depth -= 1
    html.append('</ul>')
    return '\n'.join(html)


def rebuild_index(template, nav_html):
    with open(template, encoding='utf-8') as f:
        content = f.read()
    start = content.find('<ul class="summary">')
    if start < 0:
        raise RuntimeError('No summary block')
    divider = content.find('<li class="divider"', start)
    if divider < 0:
        raise RuntimeError('No divider')
    end = content.find('</ul>', divider) + len('</ul>')
    return content[:start] + nav_html + content[end:]


def main():
    header, entries = build_full_summary()
    with open(OUT_SUMMARY, 'w', encoding='utf-8') as f:
        for h in header:
            f.write(h + '\n')
        for e in entries:
            f.write(e + '\n')
    print(f"Generated: {OUT_SUMMARY}")
    nav_html = convert_md_to_html(entries)
    new_html = rebuild_index(INDEX_TEMPLATE, nav_html)
    with open(OUT_INDEX, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Generated: {OUT_INDEX}")

if __name__ == '__main__':
    main()
