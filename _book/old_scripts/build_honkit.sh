#!/usr/bin/env bash
SESSION="honkit"
if ! tmux has-session -t $SESSION 2>/dev/null; then
  tmux new-session -d -s $SESSION "npx honkit build --log=debug | tee build.log"
fi
tmux attach -t $SESSION

