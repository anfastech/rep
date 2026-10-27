#!/usr/bin/env bash
# One benchmark round: compare two skill versions (git tags) on held-out source skills.
#   usage: scripts/run_round.sh v0.3 v0.4 r6 r7
# Needs: claude CLI, gh, sources fetched (scripts/fetch_sources.sh).
# Every claude call runs with --setting-sources project from an empty dir, so the
# operator's own CLAUDE.md and plugins do not leak into outputs or scores.
set -uo pipefail
VA=$1; VB=$2; shift 2; IDS=("$@")
BENCH=$(cd "$(dirname "$0")/.." && pwd)
REPO=$(git -C "$BENCH" rev-parse --show-toplevel)
WORK=${WORK:-$(mktemp -d -t rep-round)}
ISO=$WORK/iso; mkdir -p "$ISO"
CLAUDE=(claude -p --setting-sources project)
echo "work dir: $WORK"

# 1. Generate 7 outputs per source skill (skipped when outputs already exist).
gen() {
  local id=$1 out=$BENCH/outputs/$1
  [ -d "$out/train" ] && return
  { cat "$BENCH/prompts/generate.md"; echo
    (cd "$BENCH/hidden/$id" && find . -type f | sort) | while read -r f; do
      echo "----- SKILL FILE: ${f#./} -----"; cat "$BENCH/hidden/$id/$f"; echo; done
    echo "----- BRIEFS -----"; cat "$BENCH/briefs.md"; } > "$WORK/$id.gen.txt"
  (cd "$ISO" && "${CLAUDE[@]}" --tools "" < "$WORK/$id.gen.txt" > "$WORK/$id.out.txt")
  python3 - "$WORK/$id.out.txt" "$out" <<'PY'
import os, re, sys
text, out = open(sys.argv[1]).read(), sys.argv[2]
parts = re.split(r'^===(0\d)===\s*$', text, flags=re.M)
posts = {parts[i]: parts[i + 1].strip() + "\n" for i in range(1, len(parts), 2)}
assert sorted(posts) == [f"0{i}" for i in range(1, 8)], sorted(posts)
for k, v in posts.items():
    d = f"{out}/{'train' if int(k) <= 5 else 'heldout'}"
    os.makedirs(d, exist_ok=True)
    open(f"{d}/{k}.txt", "w").write(v)
PY
}

# 2. Reconstruct with one skill version, blind to the source.
#    claude -p can hang after finishing, so stop it 5 minutes after report.md appears.
recon() {
  local id=$1 v=$2 d=$WORK/$1-$2
  mkdir -p "$d/.claude/skills"
  git -C "$REPO" archive "$v" skills/reverse-engineer-skill | tar -x -C "$d/.claude"
  cp -R "$BENCH/outputs/$id" "$d/outputs"
  (cd "$d" && "${CLAUDE[@]}" --permission-mode bypassPermissions \
     < "$BENCH/prompts/reconstruct.md" > "$WORK/$id-$v.log" 2>&1) &
  local pid=$! t=0
  while kill -0 $pid 2>/dev/null; do
    if [ -f "$d/reverse-runs/target/report.md" ]; then t=$((t + 10)); [ $t -ge 300 ] && kill $pid; fi
    sleep 10
  done
  mkdir -p "$BENCH/runs/$v/$id"
  for f in SKILL.md report.md ledger.md history.md; do
    [ -f "$d/reverse-runs/target/$f" ] && cp "$d/reverse-runs/target/$f" "$BENCH/runs/$v/$id/"
  done
  [ -f "$BENCH/runs/$v/$id/SKILL.md" ] || echo "MISSING SKILL.md: $id $v (see $WORK/$id-$v.log)"
}

# 3. Paired blind scoring: one scorer sees both versions as X and Y.
score() {
  local id=$1 x y
  if [ $((RANDOM % 2)) = 0 ]; then x=$VA; y=$VB; else x=$VB; y=$VA; fi
  mkdir -p "$BENCH/blind/$id"
  cp "$BENCH/runs/$x/$id/SKILL.md" "$BENCH/blind/$id/X.md"
  cp "$BENCH/runs/$y/$id/SKILL.md" "$BENCH/blind/$id/Y.md"
  sed -i '' "/^$id:/d" "$BENCH/blind/MAPPING.txt" 2>/dev/null || sed -i "/^$id:/d" "$BENCH/blind/MAPPING.txt"
  echo "$id: X=$x Y=$y" >> "$BENCH/blind/MAPPING.txt"
  sed -e "s#{BENCH}#$BENCH#g" -e "s#{ID}#$id#g" "$BENCH/prompts/score-paired.md" > "$WORK/$id.score.txt"
  (cd "$ISO" && "${CLAUDE[@]}" --permission-mode bypassPermissions < "$WORK/$id.score.txt" > "$WORK/$id.score.log" 2>&1)
}

for id in "${IDS[@]}"; do gen "$id" & done; wait
for id in "${IDS[@]}"; do for v in "$VA" "$VB"; do recon "$id" "$v" & done; done; wait
for id in "${IDS[@]}"; do score "$id" & done; wait
python3 "$BENCH/scripts/sum_paired.py" "${IDS[@]}"
