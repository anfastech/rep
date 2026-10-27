# rep: reverse engineer prompt

A Claude Code skill that rebuilds the skill or prompt behind a set of AI outputs.
Give it posts, threads, captions, newsletters or short videos made by one unknown skill. It returns a
SKILL.md that writes like them, with every rule tagged by its evidence and a list of what
the outputs cannot show.

```
outputs ──> negate content (topic, facts = brief, not skill)
        ──> measure form ──> evidence ledger ──> 3 draft skills
        ──> blind replay on the same briefs ──> merge, revise (max 3 rounds)
        ──> held-out test + negative control ──> leak check ──> SKILL.md + report.md
```

Each output is modelled as `Skill(brief) + noise`. The skill is what stays constant
across outputs. Method draws on output2prompt (Zhang, Morris, Shmatikov 2024) and on
[rea](https://github.com/morluto/rea)'s evidence rules: observed, inferred and unknown stay
apart, and a surface match alone is not proof. Notes: `docs/research/prompt-inversion.md`.

## Install

As a plugin:

```
/plugin marketplace add anfastech/rep
/plugin install rep@rep
```

Or copy `skills/reverse-engineer-skill/` into `~/.claude/skills/`.

## Use

Put the outputs in a folder, one per `.txt` file, at least 5 (8 or more is better, with
mixed post types). Then ask: "reverse engineer the skill that wrote these posts in ./posts".

For videos, give the video files. The skill extracts metadata, hard cuts, a contact sheet
and a timed transcript (`scripts/video_extract.sh`, needs ffmpeg and openai-whisper), then
rebuilds the script beats, pacing, visual style, captions and overlays. It can also diff a
code-rendered replay of one beat against the original (`scripts/frame_diff.py`).

## Results

v0.4 on 2 source skills it was never tuned on: 86% of its rules are real (v0.3: 70%),
recall of visible rules 0.69, no rules that contradict the source. Details and limits:
[evals/RESULTS.md](evals/RESULTS.md).

Video support is a prototype (tested on 1 video). Carousels are not built.

## Layout

```
skills/reverse-engineer-skill/   the skill (SKILL.md, references/, scripts/, templates/)
.claude-plugin/                  plugin and marketplace manifests
docs/research/                   research notes on prompt inversion
evals/                           toy fixture, benchmark, results
```

Skill versions are git tags (`v0.1` to `v0.5`).
