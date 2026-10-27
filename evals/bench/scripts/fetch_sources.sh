#!/usr/bin/env bash
# Download the source skills listed in sources.tsv into hidden/<id>/ (gitignored).
# Text files only, at the commit pinned in sources.tsv (empty: default branch).
set -euo pipefail
cd "$(dirname "$0")/.."
grep -v '^#' sources.tsv | while IFS=$'\t' read -r id repo dir ref _; do
  [ -n "$id" ] || continue
  [ -n "$ref" ] || ref=$(gh api "repos/$repo" --jq .default_branch)
  rm -rf "hidden/$id"
  gh api "repos/$repo/git/trees/$ref?recursive=1" \
    --jq ".tree[] | select(.type==\"blob\") | select(.path | startswith(\"$dir/\")) | .path" |
  while read -r fp; do
    rel=${fp#"$dir"/}
    case "$rel" in *.md|*.txt) ;; *) continue ;; esac
    case "$rel" in README.md|evals/*|scripts/*|tests/*) continue ;; esac
    mkdir -p "hidden/$id/$(dirname "$rel")"
    gh api "repos/$repo/contents/$fp?ref=$ref" --jq .content | base64 -d > "hidden/$id/$rel"
  done
  echo "$id: $(find "hidden/$id" -type f | wc -l | tr -d ' ') files"
done
