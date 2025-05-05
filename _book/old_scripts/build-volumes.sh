#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
DEFAULT_BUILD_ROOT="$REPO_ROOT/build"
MAX_PARALLEL=32    # 根据你的CPU核心数设置

# 读取输出目录
BUILD_ROOT="${1:-$DEFAULT_BUILD_ROOT}"
shift || true

mkdir -p "$BUILD_ROOT"

# 解析主卷列表
VOLUMES=()
if [[ $# -gt 0 ]]; then
  VOLUMES=("$@")
else
  for d in "$REPO_ROOT"/*; do
    if [[ -d "$d" && -f "$d/book.json" ]]; then
      VOLUMES+=("$(basename "$d")")
    fi
  done
fi

[[ ${#VOLUMES[@]} -eq 0 ]] && { echo "❗ No volumes found."; exit 1; }

# 成功/失败卷
SUCCESS_LIST=()
FAILED_LIST=()

# Build单个卷
build_volume() {
  local src="$1"
  local rel="$2"

  local out="$BUILD_ROOT/$rel"
  local log="$BUILD_ROOT/${rel//\//_}.log"

  echo "▶ Building [$rel]..."
  mkdir -p "$out"

  if npx honkit build "$src" "$out" >"$log" 2>&1; then
    echo "✔ Success [$rel]"
    SUCCESS_LIST+=("$rel")
  else
    echo "✖ Failed [$rel]"
    FAILED_LIST+=("$rel")
  fi
}

# 控制最大并发数
job_control() {
  local max_jobs=$1
  while (( $(jobs -r | wc -l) >= max_jobs )); do
    sleep 0.5
  done
}

# 解析SUMMARY.md寻找一层子卷
find_sub_volumes() {
  local base="$1"
  local rel="$2"

  local summary="$base/SUMMARY.md"
  [[ -f "$summary" ]] || return

  local subdirs=()
  while read -r line || [[ -n "$line" ]]; do
    # 抓取Markdown链接里的路径
    target=$(echo "$line" | grep -oP '\(([^)]+)\)' | sed 's/[()]//g' || true)
    if [[ -n "$target" ]]; then
      local target_dir="$base/$(dirname "$target")"
      if [[ -d "$target_dir" && -f "$target_dir/book.json" ]]; then
        subdirs+=("$target_dir|$rel/$(basename "$target_dir")")
      fi
    fi
  done < "$summary"

  for item in "${subdirs[@]}"; do
    echo "$item"
  done
}

# 主逻辑：开始处理
for VOL in "${VOLUMES[@]}"; do
  VOL_PATH="$REPO_ROOT/$VOL"
  REL_PATH="$VOL"

  [[ -f "$VOL_PATH/book.json" ]] || { echo "⚠️  Skip $VOL (no book.json)"; continue; }

  # 先build主卷
  job_control "$MAX_PARALLEL"
  build_volume "$VOL_PATH" "$REL_PATH" &

  # 查找子卷
  while read -r sub || [[ -n "$sub" ]]; do
    [[ -z "$sub" ]] && continue
    SUB_PATH="${sub%%|*}"
    SUB_REL="${sub##*|}"

    if [[ -d "$SUB_PATH" && -f "$SUB_PATH/book.json" ]]; then
      job_control "$MAX_PARALLEL"
      build_volume "$SUB_PATH" "$SUB_REL" &
    else
      echo "⚠️  Subvolume missing: $SUB_REL"
    fi
  done < <(find_sub_volumes "$VOL_PATH" "$REL_PATH")

done

# 等待所有任务完成
wait

# 输出最终总结
echo
echo "✅ Build Summary:"
echo "-------------------------"
echo "Total Volumes (Including Subvolumes): $(( ${#SUCCESS_LIST[@]} + ${#FAILED_LIST[@]} ))"
echo "Success: ${#SUCCESS_LIST[@]}"
echo "Failed: ${#FAILED_LIST[@]}"
if [[ ${#FAILED_LIST[@]} -gt 0 ]]; then
  echo "❗ Failed Volumes: ${FAILED_LIST[*]}"
fi
