#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
BUILD_ROOT="$REPO_ROOT/build"
SESSION="honkit-build"
WINDOW="build"

# -------- parse volumes --------
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

# -------- tmux session/window --------
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
  tmux new-session -d -s "$SESSION" -n "$WINDOW" -c "$REPO_ROOT" "echo 'tmux build session started'; bash"
fi

if ! tmux list-windows -t "$SESSION" | grep -q "$WINDOW"; then
  tmux new-window -t "$SESSION" -n "$WINDOW" -c "$REPO_ROOT" bash
fi

# -------- send build commands --------
for VOL in "${VOLUMES[@]}"; do
  SRC="$REPO_ROOT/$VOL"
  OUT="$BUILD_ROOT/$VOL"
  LOG="$BUILD_ROOT/${VOL}.log"
  [[ -f "$SRC/book.json" ]] || { echo "skip $VOL (no book.json)"; continue; }

  CMD="echo '▶ Start building [$VOL]' && mkdir -p \"$OUT\" && npx honkit build \"$SRC\" \"$OUT\" 2>&1 | tee \"$LOG\" && if [ \${PIPESTATUS[0]} -eq 0 ]; then echo '✔ Build success [$VOL]'; else echo '✖ Build failed [$VOL]'; fi"

  echo "Queueing CMD: $CMD"
  tmux send-keys -t "$SESSION:$WINDOW" "$CMD" 'C-m'
done

echo
echo "✅ Commands queued in tmux session [$SESSION]."
echo "   You can manually attach by: tmux attach -t $SESSION"
echo "   Or ctrl-b d to detach later."
