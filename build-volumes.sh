#!/usr/bin/env bash
# =============================================
# build-volumes.sh
#   在 tmux 会话中按卷编译 HonKit 书籍
#   - 无参数：自动扫描顶层含 book.json 的目录
#   - 指定参数：仅编译给出的卷
# =============================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
BUILD_ROOT="$REPO_ROOT/_book"
SESSION="honkit-build"            # tmux 会话名，可自行修改
WINDOW="build"                    # 会话内用于执行任务的窗口名

# ---------- 1. 解析待编译卷 ----------
if [[ $# -gt 0 ]]; then
  VOLUMES=("$@")
else
  mapfile -t VOLUMES < <(
    find "$REPO_ROOT" -maxdepth 1 -mindepth 1 -type d \
      -exec test -f "{}/book.json" \; -print | xargs -n1 basename
  )
fi

[[ ${#VOLUMES[@]} -eq 0 ]] && {
  echo "⚠ 未检测到任何卷，退出！"; exit 1; }

echo "📚 待编译卷：${VOLUMES[*]}"

# ---------- 2. 创建 / 复用 tmux 会话 ----------
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -c "$REPO_ROOT" -n "$WINDOW" \
    "echo '🚀 HonKit build session started in $REPO_ROOT'; bash"
  echo "🆕 已创建 tmux 会话 $SESSION"
fi

# 如果窗口不存在（可能会话有其他窗口），创建
if ! tmux list-windows -t "$SESSION" | grep -q "^0:$WINDOW"; then
  tmux new-window -t "$SESSION" -n "$WINDOW" -c "$REPO_ROOT" bash
fi

# ---------- 3. 发送构建命令 ----------
for VOL in "${VOLUMES[@]}"; do
  SRC="$REPO_ROOT/$VOL"
  OUT="$BUILD_ROOT/$VOL"
  LOG="$BUILD_ROOT/${VOL}.log"

  if [[ ! -f "$SRC/book.json" ]]; then
    echo "❌ [$VOL] 缺少 book.json，跳过"; continue
  fi

  CMD=$(
    cat <<EOF
echo '▶ 开始构建 $VOL'; \
mkdir -p "$OUT"; \
npx honkit build "$SRC" "$OUT" 2>&1 | tee "$LOG"; \
echo '✔ 完成 $VOL';
EOF
  )

  tmux send-keys -t "$SESSION:$WINDOW" "$CMD" Enter
done

echo -e "\n✅ 编译命令已派发到 tmux 会话：$SESSION"
echo   "   输入  tmux attach -t $SESSION  查看实时输出。"
echo   "   在会话内可 Ctrl-b d 脱离，进程依旧运行。"

# 自动附加（如不想自动 attach，请注释以下行）
tmux attach -t "$SESSION"
