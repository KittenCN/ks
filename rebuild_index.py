#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rebuild_nav.py

1. 生成 summary_auto_full.md：合并根 SUMMARY.md 和所有子卷的 SUMMARY.md，任意深度嵌套。
2. 生成 index_rebuild.html：以 index_model.html 为模板，只替换 <ul class="summary">…</ul>，.md → .html。
"""

import os, re, json, sys
from pathlib import Path
from html import escape

# =============== 配置 ===============
EXCLUDE = {
    '_archive','drafts','.git','.github',
    'node_modules','build','dist','_book','_layouts',
    'lib','img','imgs'
}
ROOT_SUMMARY = Path('SUMMARY.md')
INDEX_MODEL  = Path('index_model.html')
OUT_SUMMARY  = Path('summary_auto_full.md')
OUT_INDEX    = Path('index_rebuild.html')

# 匹配 Markdown 列表项：[标题](链接)
MD_LINK = re.compile(r'^(\s*)[-*]\s+\[([^\]]+)]\(([^)]*)\)')

# =============== 工具函数 ===============
def parse_md(path: Path):
    """
    解析一个 SUMMARY.md，返回 [(indent_spaces, text, href), ...]
    """
    res = []
    text = path.read_text(encoding='utf-8').replace('\t', '    ')
    for ln in text.splitlines():
        m = MD_LINK.match(ln)
        if m:
            res.append((len(m.group(1)), m.group(2), m.group(3)))
    return res

def find_volumes(root='.'):
    """
    递归查找有 book.json & SUMMARY.md 的子目录，排除 EXCLUDE。
    """
    for d, dirs, files in os.walk(root):
        # 如果路径中包含排除项，就不再深入
        if any(p in EXCLUDE for p in Path(d).parts):
            dirs[:] = []
            continue
        if 'book.json' in files and 'SUMMARY.md' in files:
            yield Path(d)

def get_book_title(d: Path):
    """
    读取 book.json 中的 title，失败则用目录名。
    """
    try:
        with open(d/'book.json', encoding='utf-8') as f:
            return json.load(f).get('title') or d.name
    except:
        return d.name

# =============== 构建树结构 ===============
# 树节点格式：{ 'title': str, 'link': str, 'chapters': [(ind,text,href)...], 'children': { child_link: node, ... } }
tree = {}
node_map = {}  # link -> node 引用
root_order = []

# 1) 先把根 SUMMARY.md 的第一层导入
if not ROOT_SUMMARY.exists():
    sys.exit("❌ 找不到根 SUMMARY.md")
for indent, text, href in parse_md(ROOT_SUMMARY):
    # 跳过空标题或主页 README
    if not text and href.lower().endswith('readme.md'):
        continue
    node = {
        'title': text,
        'link': href,
        'chapters': [],
        'children': {}
    }
    tree[href] = node
    node_map[href] = node
    root_order.append(href)

# 2) 递归导入所有子卷
for vol in find_volumes('.'):
    if vol == Path('.'):
        continue
    rel = vol.as_posix()
    main_link = f"{rel}/README.md"
    # 创建或复用节点
    if main_link in node_map:
        node = node_map[main_link]
    elif get_book_title(vol) != '':
        node = {
            'title': get_book_title(vol),
            'link': main_link,
            'chapters': [],
            'children': {}
        }
        # 确定父节点
        parent = vol.parent
        parent_link = None
        if parent != Path('.'):
            parent_link = f"{parent.as_posix()}/README.md"
        if parent_link and parent_link in node_map:
            node_map[parent_link]['children'][main_link] = node
        elif node['title'] != '':
            tree[main_link] = node
            # root_order.append(main_link)
            node_map[main_link] = node

        # 解析该卷 SUMMARY.md 中的章节项目，挂到 node['chapters']
        if node['title'] != '':
            for ind, txt, href in parse_md(vol/'SUMMARY.md'):
                if vol.name == node['title']:
                    node['chapters'].append((ind, txt, f"{rel}/{href}"))
                else:
                    print(f"❌ {vol.name} 的章节 {txt} 不在根目录下，跳过")
                    continue

# =============== 导出 summary_auto_full.md ===============
lines = []

def emit(node, depth=0):
    # 当前节点
    lines.append('    '*depth + f"- [{node['title']}]({node['link']})")
    # 该页下的章节
    for _, txt, href in node['chapters']:
        lines.append('    '*(depth+1) + f"- [{txt}]({href})")
    # 子节点
    for child in sorted(node['children'].values(), key=lambda x: x['title']):
        emit(child, depth+1)

# for root_node in sorted(tree.values(), key=lambda x: x['title']):
#     emit(root_node, 0)
for href in root_order:
    emit(tree[href], 0)

OUT_SUMMARY.write_text("\n".join(lines)+"\n", encoding='utf-8')
print("✅ 已生成 summary_auto_full.md")

# =============== 生成 index_rebuild.html ===============
def md_to_nested_ul(md_lines):
    html = []
    stack = [-1]
    for ln in md_lines:
        m = MD_LINK.match(ln.replace('\t','    '))
        if not m:
            continue
        indent = len(m.group(1))
        text, href = m.group(2), m.group(3)
        # 关闭多余层级
        while indent <= stack[-1]:
            html.append('    '*len(stack) + '</li></ul>')
            stack.pop()
        # 开新层级
        html.append('    '*len(stack) + '<ul>')
        stack.append(indent)
        # .md → .html
        href_html = str(Path(href).with_suffix('.html'))
        html.append('    '*len(stack) + f'<li><a href="{escape(href_html)}">{escape(text)}</a>')
    # 关闭剩余层级
    while len(stack) > 1:
        html.append('    '*len(stack) + '</li></ul>')
        stack.pop()
    return "\n".join(html)

html_ul = '<ul class="summary">\n' + md_to_nested_ul(lines) + '\n</ul>'

tpl = INDEX_MODEL.read_text(encoding='utf-8')
# 用回调避免反斜线转义错误
out = re.sub(r'<ul class="summary">.*?</ul>', lambda m: html_ul, tpl, flags=re.S)
OUT_INDEX.write_text(out, encoding='utf-8')
print("✅ 已生成 index_rebuild.html")