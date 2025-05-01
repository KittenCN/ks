#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild_nav.py

Traverses all subdirectories to find folders containing book.json and SUMMARY.md,
rebuilds a full SUMMARY.md including all nested SUMMARY.md files (recursively),
and updates the index HTML navigation menu based on the provided index_model.html template.
Additionally, copies the rebuilt index to the _book directory as index.html.
Only the navigation menu block (<ul class="summary">…</ul>) is modified, all other template content is preserved.
Navigation links open in the right panel (iframe named "contentFrame"), summary retains .md links, HTML nav uses .html.

Usage:
    python rebuild_nav.py
"""
import os
import re
import shutil

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
BOOK_DIR = os.path.join(PROJECT_ROOT, '_book')
BOOK_INDEX = os.path.join(BOOK_DIR, 'index.html')

# Collapsible nav script and style injected into HTML nav block
STYLE_JS = '''
<style>
.summary ul { display: none; }
.summary li.chapter { cursor: pointer; }
.summary li.chapter.open > ul { display: block; }
</style>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var items = document.querySelectorAll('.summary li.chapter');
    items.forEach(function(li) {
        li.addEventListener('click', function(e) {
            // toggle collapse state
            var sub = li.querySelector('ul');
            if (!sub) return;
            if (li.classList.contains('open')) {
                li.classList.remove('open');
                sub.style.display = 'none';
            } else {
                li.classList.add('open');
                sub.style.display = 'block';
            }
        });
    });
});
</script>
<style>
.summary ul { display: none; }
.summary li.chapter { cursor: pointer; }
.summary li.chapter.open > ul { display: block; }
</style>
<script>
window.addEventListener('DOMContentLoaded', function() {
    var nav = document.querySelector('.summary');
    if (!nav) return;
    nav.addEventListener('click', function(e) {
        var li = e.target.closest('li.chapter');
        if (!li) return;
        // toggle collapse state for this item
        var sub = li.querySelector('ul');
        if (sub) {
            if (li.classList.contains('open')) {
                li.classList.remove('open');
                sub.style.display = 'none';
            } else {
                li.classList.add('open');
                sub.style.display = 'block';
            }
        }
        // allow link navigation; prevent default only if clicking non-link
        if (e.target.tagName !== 'A') {
            e.preventDefault();
        }
    });
});
</script>
<style>
.summary ul { display: none; }
.summary li.chapter { cursor: pointer; }
.summary li.chapter.open > ul { display: block; }
</style>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var nav = document.querySelector('.summary');
    if (!nav) return;
    nav.addEventListener('click', function(e) {
        var li = e.target.closest('li.chapter');
        if (!li) return;
        var sub = li.querySelector('ul');
        if (!sub) return;
        // toggle collapse state
        e.preventDefault();
        if (li.classList.contains('open')) {
            li.classList.remove('open');
            sub.style.display = 'none';
        } else {
            li.classList.add('open');
            sub.style.display = 'block';
        }
        // if clicked on link, allow navigation
        if (e.target.tagName === 'A') {
            return;
        }
    });
});
</script>
<style>
.summary ul { display: none; }
.summary li.chapter { cursor: pointer; }
.summary li.chapter.open > ul { display: block; }
</style>
<script>
document.addEventListener('DOMContentLoaded', function() {
    var nav = document.querySelector('.summary');
    if (!nav) return;
    nav.addEventListener('click', function(e) {
        var li = e.target.closest('li.chapter');
        if (!li) return;
        // if clicked inside an anchor, allow navigation and do not toggle
        if (e.target.closest('a')) {
            e.stopPropagation();
            return;
        }
        var sub = li.querySelector('ul');
        if (!sub) return;
        e.preventDefault();
        if (li.classList.contains('open')) {
            li.classList.remove('open');
            sub.style.display = 'none';
        } else {
            li.classList.add('open');
            sub.style.display = 'block';
        }
    });
});
</script>
'''


def adjust_link(link_path, parent_dir):
    if '://' in link_path or link_path.startswith(('/', '#')):
        return link_path
    abs_path = os.path.normpath(os.path.join(parent_dir, link_path))
    rel = os.path.relpath(abs_path, PROJECT_ROOT).replace('\\', '/')
    return rel.lstrip('./')


def adjust_md_links(text, parent_dir):
    return re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        lambda m: f"[{m.group(1)}]({adjust_link(m.group(2), parent_dir)})",
        text
    )


def get_file_depth(path):
    dir_path = os.path.dirname(os.path.abspath(path))
    rel = os.path.relpath(dir_path, PROJECT_ROOT)
    return 0 if rel == '.' else len(rel.split(os.sep))


def extract_entries(summary_path, ignore_link=None):
    entries = []
    parent_dir = os.path.dirname(summary_path)
    with open(summary_path, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\s*-\s+(.*)', line)
            if not m:
                continue
            raw = m.group(1).strip()
            adj = adjust_md_links(raw, parent_dir)
            link_match = re.search(r'\(([^)]+)\)', adj)
            link = link_match.group(1) if link_match else None
            if ignore_link and link == ignore_link:
                continue
            entries.append((adj, link))
    return entries


def build_entries(summary_path, ignore_link=None, visited=None):
    if visited is None:
        visited = set()
    real = os.path.realpath(summary_path)
    if real in visited:
        return []
    visited.add(real)

    depth = get_file_depth(summary_path)
    indent = '\t' * depth
    lines = []
    for text, link in extract_entries(summary_path, ignore_link):
        lines.append(f"{indent}-\t{text}")
        if link and not link.startswith(('http://', 'https://', '/', '#')):
            dirp = os.path.normpath(os.path.join(PROJECT_ROOT, os.path.dirname(link)))
            if os.path.basename(dirp) in EXCLUDE_DIRS:
                continue
            sub_summary = os.path.join(dirp, ROOT_SUMMARY)
            sub_book = os.path.join(dirp, 'book.json')
            if os.path.isdir(dirp) and os.path.exists(sub_summary) and os.path.exists(sub_book):
                lines += build_entries(sub_summary, ignore_link=link, visited=visited)
    return lines


def build_full_summary():
    root = os.path.join(PROJECT_ROOT, ROOT_SUMMARY)
    if not os.path.exists(root):
        raise FileNotFoundError(f"Missing {ROOT_SUMMARY}")
    header = []
    with open(root, encoding='utf-8') as f:
        first = f.readline()
        if first.startswith('#'):
            header.extend([first.rstrip('\n'), ''])
    entries = build_entries(root)
    return header, entries


def convert_md_to_html(md_lines):
    """
    Convert summary .md-list into HonKit-style HTML <ul> with data-level and data-path,
    nested <ul class="articles">, and collapsible behavior.
    """
    html = ['<ul class="summary">']
    depth = 0
    # counters for numbering each level
    counters = []
    for line in md_lines:
        lvl = len(line) - len(line.lstrip('	'))
        # close deeper levels
        while lvl < depth:
            html.append('  ' * depth + '</ul>')
            html.append('  ' * depth + '</li>')
            depth -= 1
            counters.pop()
        # open new nested level
        if lvl > depth:
            html.append('  ' * depth + '<ul class="articles">')
            depth += 1
            counters.append(0)
        # ensure counters length
        if len(counters) <= lvl:
            counters.extend([0] * (lvl - len(counters) + 1))
        # increment counter for this level
        counters[lvl] += 1
        # reset deeper levels
        for i in range(lvl+1, len(counters)):
            counters[i] = 0
        # compute data-level string
        data_level = '.'.join(str(counters[i]) for i in range(lvl+1))
        content = line.lstrip('	')[2:]
        m = re.match(r'\[([^\]]+)\]\(([^)]+)\)', content)
        if m:
            title, link = m.group(1), m.group(2)
            # adjust README.md to index.html in data-path
            path = link
            if path.endswith('README.md'):
                path = path[:-len('README.md')] + 'index.html'
            # link for anchor
            href = path if path.endswith('.html') else (path[:-3] + '.html') if path.endswith('.md') else path
            # open <li>
            html.append(
                '  ' * depth +
                f'<li class="chapter" data-level="{data_level}" data-path="{path}">'
                + f'<a href="{href}" target="contentFrame">{title}</a>'
            )
    # close any remaining open tags
    while depth > 0:
        html.append('  ' * depth + '</ul>')
        html.append('  ' * depth + '</li>')
        depth -= 1
    html.append('</ul>')
    return STYLE_JS + '\n'.join(html)


def rebuild_index(template, nav_html):
    tpl = open(template, encoding='utf-8').read()
    start = tpl.find('<ul class="summary">')
    if start < 0:
        raise RuntimeError('No summary block')
    mid = tpl.find('<li class="divider"', start)
    if mid < 0:
        raise RuntimeError('No divider')
    end = tpl.find('</ul>', mid) + len('</ul>')
    return tpl[:start] + nav_html + tpl[end:]


def main():
    header, entries = build_full_summary()
    with open(OUT_SUMMARY, 'w', encoding='utf-8') as f:
        for h in header:
            f.write(h + '\n')
        for e in entries:
            f.write(e + '\n')
    print(f"Generated: {OUT_SUMMARY}")

    nav_html = convert_md_to_html(entries)
    new_index = rebuild_index(INDEX_TEMPLATE, nav_html)
    with open(OUT_INDEX, 'w', encoding='utf-8') as f:
        f.write(new_index)
    print(f"Generated: {OUT_INDEX}")

    os.makedirs(BOOK_DIR, exist_ok=True)
    shutil.copyfile(OUT_INDEX, BOOK_INDEX)
    print(f"Copied: {BOOK_INDEX}")

if __name__ == '__main__':
    main()
