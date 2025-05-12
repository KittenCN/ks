#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Multi-threaded script to insert YAML front-matter descriptions into Markdown files
- 递归遍历当前目录及所有子目录中的 .md 文件
- 跳过文件名前缀为 '_' 的文件，以及名为 'SUMMARY.md' 的文件
- 如果本目录下没有 book.json，则向上查找父目录，依次类推
- 使用多线程并行，并显示进度条
"""

import json, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

MAX_WORKERS  = 4
BOOK_NAME    = 'book.json'
ENCODING     = 'utf-8'

def find_description_for_md(md_path: Path):
    dir_path = md_path.parent
    while True:
        book = dir_path / BOOK_NAME
        if book.is_file():
            data = json.loads(book.read_text(encoding=ENCODING))
            return data.get('description')
        if dir_path.parent == dir_path:
            break
        dir_path = dir_path.parent
    return None

def process_md(md_path: Path):
    desc = find_description_for_md(md_path)
    if not desc:
        return f"NO_DESC: {md_path}"
    content = md_path.read_text(encoding=ENCODING)
    front = f"---\ndescription: {desc.strip()}\n---\n\n"
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) == 3:
            content = parts[2].lstrip('\r\n')
    md_path.write_text(front + content, encoding=ENCODING)
    return f"OK: {md_path}"

def main(base_dir: Path):
    # 1. 递归查找所有 .md
    md_files = list(base_dir.rglob('*.md'))
    # 2. 排除：以 '_' 开头 或 名为 'SUMMARY.md'
    md_files = [
        p for p in md_files
        if not p.name.startswith('_')
        and p.name.lower() != 'summary.md'
    ]
    total = len(md_files)
    if total == 0:
        print("⚠️ 没有找到任何符合条件的 Markdown 文件。")
        return

    print(f"🔍 发现 {total} 个 Markdown 文件，使用 {MAX_WORKERS} 个线程处理...\n")
    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_md, p): p for p in md_files}
        for future in tqdm(as_completed(futures), total=total, desc="Updating MD", unit="file"):
            results.append(future.result())

    ok      = [r for r in results if r.startswith("OK")]
    no_desc = [r for r in results if r.startswith("NO_DESC")]

    print(f"\n✅ 完成：更新成功 {len(ok)} 个文件；缺少 description 的 {len(no_desc)} 个。")
    if no_desc:
        print("缺少 description 的文件：")
        for r in no_desc:
            print(" ", r)

if __name__ == '__main__':
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    main(base)
