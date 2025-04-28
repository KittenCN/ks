#!/usr/bin/env bash
# build-volumes.sh
# ------------------------------------------
# 用法：
#   ./build-volumes.sh                # 自动扫描所有卷
#   ./build-volumes.sh algorithms math docs   # 只构建指定卷
# ------------------------------------------

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
BUILD_ROOT="$REPO_ROOT/build"
SESSION="honkit-build"                 # tmux 会话名，可修改

# 1. 解析待构建卷
if [[ $# -gt 0 ]]; then
  VOLUMES=("$@")
else
  mapfile -t VOLUMES < <(find "$REPO_ROOT" -maxdepth 1 -mindepth 1 -type d \
                         -exec test -f "{}/book.json" \; -print | xargs -n1 basename)
fi

if [[ ${#VOLUMES[@]} -eq 0 ]]; then
  echo "⚠ 没有检测到任何带 book.json 的卷，退出"; exit 1
fi

# 2. 创建 tmux 会话（若不存在）
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -c "$REPO_ROOT" \
    "echo '🔧 HonKit build session started in $(pwd)'; bash"   # 默认打开一个 shell
fi

# 3. 在 tmux 中依次编译每个卷
for VOL in "${VOLUMES[@]}"; do
  VOL_SRC="$REPO_ROOT/$VOL"
  VOL_OUT="$BUILD_ROOT/$VOL"
  LOG="$BUILD_ROOT/${VOL}.log"

  if [[ ! -f "$VOL_SRC/book.json" ]]; then
    echo "❌ [$VOL] 路径下找不到 book.json，跳过"
    continue
  fi

  CMD="echo '▶ 开始构建 $VOL'; \
       mkdir -p \"$VOL_OUT\"; \
       npx honkit build \"$VOL_SRC\" \"$VOL_OUT\" 2>&1 | tee \"$LOG\"; \
       echo '✔ 完成 $VOL';"

  # 把命令发送到 tmux 会话
  tmux send-keys -t "$SESSION" "$CMD" C-m
done

echo -e "\n✅ 所有构建任务已派发到 tmux 会话：$SESSION"
echo   "   - 退出当前 SSH 前，可按 Ctrl-b d 脱离会话，编译仍将继续"
echo   "   - 重新登录后运行：tmux attach -t $SESSION 查看进度"

# 自动附加到会话（如你想手动 attach，注释掉下面一行）
tmux attach -t "$SESSION"
