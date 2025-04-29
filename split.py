import os
import subprocess
import sys
import time
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from tqdm import tqdm

# --------------------- CONFIGURATION ---------------------
MAX_PARALLEL = 32    # 最大并发数
BUILD_ROOT = Path("_book")  # 输出目录
# ---------------------------------------------------------

def find_valid_volumes(base_dir):
    """递归查找同时有 book.json 和 SUMMARY.md 的目录"""
    valid = []
    for root, dirs, files in os.walk(base_dir):
        if "book.json" in files and "SUMMARY.md" in files:
            valid.append(Path(root))
    return valid

def count_md_files(summary_path):
    """统计SUMMARY.md中链接到的md文件数量"""
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
    """build单个卷，并根据SUMMARY内容更新进度条"""
    relative_path = volume_path.relative_to(Path.cwd())
    output_path = BUILD_ROOT / relative_path

    os.makedirs(output_path, exist_ok=True)

    cmd = [
        "npx", "honkit", "build",
        str(volume_path),
        str(output_path)
    ]
    log_file = BUILD_ROOT / f"{str(relative_path).replace(os.sep, '_')}.log"
    try:
        with open(log_file, "w", encoding="utf-8") as log:
            process = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
            process.wait()
        result = (str(relative_path), process.returncode == 0)
    except Exception:
        result = (str(relative_path), False)

    # 每个md文件编译完一个卷就整体更新一次
    md_count = count_md_files(volume_path / "SUMMARY.md")
    pbar.update(md_count)
    return result

def main():
    base_dir = Path(".").resolve()
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)

    volumes = find_valid_volumes(base_dir)
    if not volumes:
        print("❗ No valid volumes found.")
        sys.exit(1)

    # 先统计总md数量
    total_md_files = sum(count_md_files(vol / "SUMMARY.md") for vol in volumes)

    print(f"✅ Found {len(volumes)} volumes to build, {total_md_files} md pages in total.\n")

    success = []
    failed = []

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as executor:
        with tqdm(total=total_md_files, desc="Building .md files", unit="md") as pbar:
            futures = {executor.submit(build_volume, vol, pbar): vol for vol in volumes}
            for future in as_completed(futures):
                vol_name, result = future.result()
                if result:
                    success.append(vol_name)
                else:
                    failed.append(vol_name)

    # Summary
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

