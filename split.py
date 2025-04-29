#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from tqdm import tqdm  # ⭐ 需要提前 pip install tqdm

# --------------------- CONFIGURATION ---------------------
MAX_PARALLEL = 32    # 最大并发数，根据你的CPU核心数设置
BUILD_ROOT = Path("_book")  # 输出目录
# ---------------------------------------------------------

def find_valid_volumes(base_dir):
    """递归查找同时有 book.json 和 SUMMARY.md 的目录"""
    valid = []
    for root, dirs, files in os.walk(base_dir):
        if "book.json" in files and "SUMMARY.md" in files:
            valid.append(Path(root))
    return valid

def build_volume(volume_path):
    """build单个卷"""
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
            subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, check=True)
        return (str(relative_path), True)
    except subprocess.CalledProcessError:
        return (str(relative_path), False)

def main():
    base_dir = Path(".").resolve()
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)

    volumes = find_valid_volumes(base_dir)
    if not volumes:
        print("❗ No valid volumes found.")
        sys.exit(1)

    print(f"✅ Found {len(volumes)} volumes to build.\n")

    success = []
    failed = []

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as executor:
        futures = {executor.submit(build_volume, vol): vol for vol in volumes}
        with tqdm(total=len(futures), desc="Building volumes", unit="vol") as pbar:
            for future in as_completed(futures):
                vol_name, result = future.result()
                if result:
                    success.append(vol_name)
                else:
                    failed.append(vol_name)
                pbar.update(1)

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
