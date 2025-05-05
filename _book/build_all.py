#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
并行编译 Honkit 各卷（跨平台 Windows/Linux 兼容）
- 递归查找所有同时包含 book.json 与 SUMMARY.md 或 summary.md 的目录
- 跳过指定的无关目录
- 使用最多 MAX_PARALLEL 线程并行执行 npx honkit build
- 将输出统一写入根目录 _book/<relative_path>（通过临时 _book_temp 合并）
- 错误日志汇总至 build_errors.log
- 合并与链接修复阶段增加进度条
"""
import os
import sys
import shutil
import subprocess
import time
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# --------------------- CONFIGURATION ---------------------
MAX_PARALLEL = 2
BUILD_ROOT = Path("_book")           # 最终输出目录
TEMP_BUILD_NAME = TEMP_DIR_NAME = "_book_temp"         # 临时构建目录名
EXCLUDED_DIRS = {d.lower() for d in (
    '_archive', 'drafts', '.git', '.github', 'node_modules',
    'build', 'dist', '_book', '_layouts', 'lib', 'img', 'imgs'
)}
# ---------------------------------------------------------

def find_valid_volumes(base_dir):
    volumes = []
    # 使用 rglob 遍历，避免 os.walk 在混合挂载路径下失败
    for book_file in base_dir.rglob('book.json'):
        volume_dir = book_file.parent
        # 排除无关目录
        if any(part.lower() in EXCLUDED_DIRS for part in volume_dir.parts):
            continue
        # 确保存在 SUMMARY.md 或 summary.md
        if (volume_dir / 'SUMMARY.md').is_file() or (volume_dir / 'summary.md').is_file():
            volumes.append(volume_dir)
    return volumes

def count_md_files(summary_path):
    count = 0
    md_link_pattern = re.compile(r'\(([^)]+\.md)\)')
    try:
        with open(summary_path, 'r', encoding='utf-8') as f:
            for line in f:
                if md_link_pattern.search(line):
                    count += 1
    except Exception:
        pass
    return count


def build_volume(src: Path, errors_log: Path):
    rel = src.relative_to(Path.cwd())
    temp_output = src / TEMP_DIR_NAME / rel
    temp_output.mkdir(parents=True, exist_ok=True)

    if os.name == 'nt':
        cmd = f'npx honkit build "{src}" "{temp_output}"'
        shell_flag = True
    else:
        cmd = ['npx', 'honkit', 'build', str(src), str(temp_output)]
        shell_flag = False

    try:
        subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            shell=shell_flag
        )
        return True
    except subprocess.CalledProcessError as e:
        with errors_log.open('a', encoding='utf-8') as log:
            log.write(f"--- Error building {rel} ---\n")
            log.write(e.stderr.decode('utf-8', errors='ignore'))
            log.write("\n")
        return False


def merge_all_outputs(volumes, base_dir):
    print("\n📦 正在从根向深一层层合并构建内容...")
    sorted_volumes = sorted(volumes, key=lambda v: len(v.relative_to(base_dir).parts))
    total_to_merge = sum(
        1 for vol in sorted_volumes
        if (vol / TEMP_BUILD_NAME / vol.relative_to(base_dir)).exists()
    )

    with tqdm(total=total_to_merge, desc="Merging volumes", unit="卷") as pbar:
        for vol in sorted_volumes:
            relative_path = vol.relative_to(base_dir)
            temp_path = vol / TEMP_BUILD_NAME / relative_path
            target_path = BUILD_ROOT / relative_path

            if temp_path.exists():
                if target_path.exists():
                    shutil.rmtree(target_path)
                shutil.copytree(temp_path, target_path)
                shutil.rmtree(vol / TEMP_BUILD_NAME, ignore_errors=True)
                pbar.update(1)

    print("🧹 正在清理 _book 中的 .md 文件...")
    for md in BUILD_ROOT.rglob("*.md"):
        try:
            md.unlink()
        except Exception:
            pass

def fix_md_links_in_html():
    print("\n🔗 正在修复 HTML 文件中的 .md 链接为 .html ...")
    html_files = list(BUILD_ROOT.rglob("*.html"))
    md_link_pattern = re.compile(r'href="([^"]+?\.md)(#[^"]*)?"')
    updated_count = 0

    with tqdm(total=len(html_files), desc="Fixing links", unit="文件") as pbar:
        for html_path in html_files:
            try:
                with open(html_path, "r", encoding="utf-8") as f:
                    content = f.read()
                new_content, count = md_link_pattern.subn(lambda m: f'href="{m.group(1).rsplit(".", 1)[0]}.html{m.group(2) or ""}"', content)
                if count > 0:
                    with open(html_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    updated_count += 1
            except Exception:
                pass
            pbar.update(1)

    print(f"✅ 链接修复完成，共更新了 {updated_count} 个 HTML 文件。")


def main():
    start = time.time()
    base = Path.cwd()
    if BUILD_ROOT.exists(): shutil.rmtree(BUILD_ROOT)
    BUILD_ROOT.mkdir()
    errors_log = base / 'build_errors.log'
    if errors_log.exists(): errors_log.unlink()

    volumes = find_valid_volumes(base)
    if not volumes:
        print("❗ 未找到有效卷目录，请检查配置。")
        sys.exit(1)

    total_md = sum(count_md_files(vol / "SUMMARY.md") for vol in volumes)
    print(f"✅ 共 {len(volumes)} 卷，约 {total_md} 页待编译。\n")

    success, failed = [], []
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as exe:
        futures = {exe.submit(build_volume, vol, errors_log): vol for vol in volumes}
        for fut in tqdm(as_completed(futures), total=len(futures), desc="Building volumes", unit="卷"):
            vol = futures[fut]
            rel = vol.relative_to(base)
            try:
                ok = fut.result()
            except:
                ok = False
            (success if ok else failed).append(rel)

    merge_all_outputs(volumes, base)
    fix_md_links_in_html()

    print("\n=== Build Summary ===")
    print(f"Total volumes: {len(volumes)}")
    print(f"Success: {len(success)}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("❗ Failed volumes:")
        for v in failed: print(f"  - {v}")
    if errors_log.exists() and errors_log.stat().st_size > 0:
        print(f"\n❗ 查看错误日志：{errors_log}")
    else:
        print("✅ 全部卷编译成功，无错误日志。")

    print(f"\n⏱ 耗时 {time.time() - start:.2f} 秒。")

if __name__ == '__main__':
    main()
