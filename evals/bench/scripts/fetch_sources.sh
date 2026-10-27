#!/usr/bin/env bash
# Download the source skills listed in sources.tsv into hidden/<id>/ (gitignored).
# Text files only. Sources are fetched at their current default branch.
set -euo pipefail
cd "$(dirname "$0")/.."
grep -v '^#' sources.tsv | while IFS=$'\t' read -r id repo dir _; do
  [ -n "$id" ] || continue
  branch=$(gh api "repos/$repo" --jq .default_branch)
  gh api "repos/$repo/git/trees/$branch?recursive=1" \
    --jq ".tree[] | select(.type==\"blob\") | select(.path | startswith(\"$dir/\")) | .path" |
  while read -r fp; do
    rel=${fp#"$dir"/}
    case "$rel" in *.md|*.txt) ;; *) continue ;; esac
    case "$rel" in README.md|evals/*|scripts/*) continue ;; esac
    mkdir -p "hidden/$id/$(dirname "$rel")"
    gh api "repos/$repo/contents/$fp" --jq .content | base64 -d > "hidden/$id/$rel"
  done
  echo "$id: $(find "hidden/$id" -type f | wc -l | tr -d ' ') files"
done
