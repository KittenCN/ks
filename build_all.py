import os
import subprocess
import sys
import time
import re
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from tqdm import tqdm

# -*- coding: utf-8 -*-

# --------------------- CONFIGURATION ---------------------
MAX_PARALLEL = 4
BUILD_ROOT = Path("_book")  # 最终合并输出目录
EXCLUDED_DIRS = {'_archive', 'drafts', '.git', '.github', 'node_modules',
                 'build', 'dist', '_book', '_layouts', 'lib', 'img', 'imgs'}
TEMP_BUILD_NAME = "_book_temp"
# ---------------------------------------------------------

def find_valid_volumes(base_dir):
    valid = []
    for root, dirs, files in os.walk(base_dir):
        rel_path = Path(root).relative_to(base_dir)
        if set(rel_path.parts) & EXCLUDED_DIRS:
            continue
        path = Path(root)
        if (path / "book.json").exists() and (path / "SUMMARY.md").exists():
            valid.append(path)
    return valid

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

def build_volume(volume_path, pbar):
    relative_path = volume_path.relative_to(Path.cwd())
    temp_output = volume_path / TEMP_BUILD_NAME / relative_path

    os.makedirs(temp_output, exist_ok=True)

    cmd = ["npx", "honkit", "build", str(volume_path), str(temp_output)]
    log_file = BUILD_ROOT / f"{str(relative_path).replace(os.sep, '_')}.log"

    try:
        with open(log_file, "w", encoding="utf-8") as log:
            process = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
            process.wait()
            success = (process.returncode == 0)
            if not success:
                with open(log_file, encoding='utf-8', errors='ignore') as l:
                    tail = l.readlines()[-10:]
                print(f"\n❌ 构建失败：{relative_path}")
                print("最后 10 行日志：")
                print("".join(tail).rstrip())
                print("--------------------------")
        result = (volume_path, success)
    except Exception:
        result = (volume_path, False)

    md_count = count_md_files(volume_path / "SUMMARY.md")
    pbar.update(md_count)
    return result

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
    base_dir = Path(".").resolve()
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)

    volumes = find_valid_volumes(base_dir)
    if not volumes:
        print("❗ No valid volumes found.")
        sys.exit(1)

    total_md_files = sum(count_md_files(vol / "SUMMARY.md") for vol in volumes)
    print(f"✅ Found {len(volumes)} volumes to build, {total_md_files} md pages in total.\n")

    success = []
    failed = []

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as executor:
        with tqdm(total=total_md_files, desc="Building .md files", unit="md") as pbar:
            futures = {executor.submit(build_volume, vol, pbar): vol for vol in volumes}
            for future in as_completed(futures):
                vol_path, result = future.result()
                vol_name = str(vol_path.relative_to(Path.cwd()))
                if result:
                    success.append(vol_name)
                    log_path = BUILD_ROOT / f"{vol_name.replace(os.sep, '_')}.log"
                    if log_path.exists():
                        log_path.unlink()
                else:
                    failed.append(vol_name)

    merge_all_outputs(volumes, base_dir)
    fix_md_links_in_html()

    print("\n=== Build Summary ===")
    print(f"Total volumes: {len(volumes)}")
    print(f"Success: {len(success)}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("❗ Failed volumes:")
        for f in failed:
            print(f"  - {f}")

if __name__ == "__main__":
    start = time.time()
    main()
    duration = time.time() - start
    print(f"\n⏱ Build completed in {duration:.2f} seconds.")

