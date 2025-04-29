#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
BUILD_ROOT="$REPO_ROOT/build"
SESSION="honkit-parallel-build"
WINDOW="main"
MAX_PARALLEL=4  # 修改这里控制最大并发数，比如 4

# Parse volumes
if [[ $# -gt 0 ]]; then
  VOLUMES=("$@")
else
  VOLUMES=()
  for d in "$REPO_ROOT"/*; do
    if [[ -d "$d" && -f "$d/book.json" ]]; then
      VOLUMES+=("$(basename "$d")")
    fi
  done
fi

[[ ${#VOLUMES[@]} -eq 0 ]] && { echo "No volume found."; exit 1; }

# Kill previous session if exists
if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "Killing old tmux session [$SESSION]"
  tmux kill-session -t "$SESSION"
fi

# Create new session
tmux new-session -d -s "$SESSION" -n "$WINDOW" -c "$REPO_ROOT" "echo 'Parallel Honkit Build Session'; bash"

# Layout counter
i=0
batch=0

for VOL in "${VOLUMES[@]}"; do
  SRC="$REPO_ROOT/$VOL"
  OUT="$BUILD_ROOT/$VOL"
  LOG="$BUILD_ROOT/${VOL}.log"

  [[ -f "$SRC/book.json" ]] || { echo "skip $VOL (no book.json)"; continue; }

  CMD="echo '▶ Building [$VOL]...'; mkdir -p \"$OUT\" && npx honkit build \"$SRC\" \"$OUT\" 2>&1 | tee \"$LOG\"; \
if [ \${PIPESTATUS[0]} -eq 0 ]; then echo '✔ Build success [$VOL]'; else echo '✖ Build failed [$VOL]'; fi; exec bash"

  # 如果是第一个，直接用初始pane
  if [[ $i -eq 0 ]]; then
    tmux send-keys -t "$SESSION:$WINDOW.0" "$CMD" 'C-m'
  else
    # 分割出新的pane
    tmux split-window -t "$SESSION:$WINDOW" -c "$REPO_ROOT" bash
    tmux send-keys -t "$SESSION:$WINDOW.$i" "$CMD" 'C-m'
  fi

  ((i++))
  
  # 每到最大并发数，就新开一个window
  if (( i % MAX_PARALLEL == 0 )); then
    tmux select-layout -t "$SESSION:$WINDOW" tiled
    ((batch++))
    tmux new-window -t "$SESSION" -n "batch-$batch" -c "$REPO_ROOT" bash
    WINDOW="batch-$batch"
    i=0
  fi
done

# 最后一次布局整理
tmux select-layout -t "$SESSION" tiled

echo
echo "✅ All build commands queued in tmux session [$SESSION]."
echo "   Attach with: tmux attach -t $SESSION"
echo "   Ctrl-b d to detach anytime."
