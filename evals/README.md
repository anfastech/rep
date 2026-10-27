# Evals

Does the skill recover the rules of a real source skill from its outputs alone?

```
source skill ──> 7 outputs (5 train, 2 held out) ──> reconstruct with version A
                                                └──> reconstruct with version B
                                                          │
                        source skill + both reconstructions ──> one blind scorer (X/Y)
                                                          │
                                                          v
                                          recall, precision, wrong items
```

## Layout

```
fixtures/toy-01/     hidden 12-rule skill, checker, outputs (fully self-contained)
bench/
  sources.tsv        source skills (GitHub repo and path); not vendored
  briefs.md          7 shared briefs, one per post type
  outputs/<id>/      the 7 outputs each source skill produced (train/, heldout/)
  runs/<ver>/<id>/   reconstructions: SKILL.md, report.md, ledger.md, history.md
  blind/MAPPING.txt  which version was X or Y per source skill
  scores/            scorer output (JSON)
  prompts/           generate, reconstruct, score-paired
  scripts/           fetch_sources.sh, run_round.sh, sum_paired.py
RESULTS.md           all rounds so far
```

## Run a round

```bash
cd evals/bench
scripts/fetch_sources.sh                 # source skills into hidden/ (gitignored)
scripts/run_round.sh v0.3 v0.4 r6 r7     # versions are git tags
python3 scripts/sum_paired.py r6 r7      # summary again, any time
```

Each claude call runs with `--setting-sources project` from an empty directory, so the
operator's own CLAUDE.md, hooks and plugins stay out of outputs, reconstructions and
scores. A round costs about 20 to 35 subagent replays per reconstruction.

Rules for a fair round:
- Use source skills the skill was never tuned on. Add new ones to `sources.tsv`.
- The reconstructor sees only `outputs/<id>/`, never `hidden/`.
- One scorer scores both versions, blind to which is which.
