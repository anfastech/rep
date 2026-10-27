---
name: reverse-engineer-skill
description: Use when given outputs made by an AI skill, prompt, template, or creator workflow (posts, captions, threads, newsletters, scripts) and asked to recover, reverse engineer, reconstruct, or clone the instructions that produced them, or to build a skill that writes "like these".
metadata:
  version: "0.2-prototype"
  modalities: text (carousel and video not built yet)
---

# Reverse Engineer a Skill

Model every output as `output_i = Skill(brief_i) + noise`. The skill is what
stays constant across outputs. The brief (topic, facts, names, numbers) and the
noise (one-off wording) change. Recover the constant part, prove it by
regenerating, and say plainly what stays unknown.

## Route the target first

| Outputs | Status | Guide |
|---|---|---|
| Plain text (posts, threads, emails, captions, newsletters) | built | [references/text.md](references/text.md) |
| Carousels, slides | not built | stop and tell the user |
| Video, audio | not built | stop and tell the user |

Fewer than 3 outputs: say the result will be a guess, then continue.

If you can run the source skill or tool yourself, collect more outputs first:
varied brief types (story, list, opinion, announcement, data), not more of the
same. Variety exposes what is constant; repetition does not.

## Workspace

Create `reverse-runs/<name>/` in the working directory:

```
train/       outputs you study
heldout/     outputs you do not open until step 8
briefs.md    inferred brief per output (the negated part)
ledger.md    one row per feature, with evidence
history.md   every draft with its per-check scores
drafts/      A1.md, B1.md, C1.md, then v2.md ...
replay/      one folder per draft and round
report.md
SKILL.md     the exported skill
```

Split: hold out 1 output per 4 (min 1). If the user already split them, keep
their split. Do not read held-out files before step 8.

## Method

1. **Negate the content.** For each train output write its brief in
   `briefs.md`: topic, story, facts, numbers, names, takeaway, and its type
   (story, list, opinion...). This is input, not skill. It never becomes a rule
   and never appears in the skill.
2. **Measure the form.** Run `python3 scripts/style_stats.py profile train/`
   (path relative to this skill). Then read each output for what the script
   cannot see: hook type, section roles, voice, conditional parts.
3. **Fill the ledger.** One row per feature:

   | Feature | Seen | Class | Rule text |
   |---|---|---|---|
   | Last line is "P.S. ..." | 5/5 | observed | Always end with ... |
   | "Cost" line | 2/5, only failure briefs | conditional | If the brief is a failure ... |
   | Hook length | 8 to 10 words, N=5 | range | Short hook, about 8 to 12 words |
   | Contrast lines | max 1 per output | capped | At most 1 (cap unconfirmed) |
   | Emojis | 0/5 | absent | Default: none |
   | Banned words | not observable | unknown | (Unknowns) |

   Classes:
   - **observed** (N/N across varied briefs): rule, but only for skeleton,
     section order, fixed strings and required parts. A punctuation or
     wording habit seen N/N is a default, not a rule.
   - **conditional** (present only when a brief property holds): if/then rule
     naming the property. Cite the outputs.
   - **tendency** (k/N, no brief property explains it): "usually".
   - **range** (a number): write the observed range, then widen it. N outputs
     under-sample the true bound.
   - **capped** (a device used 0 to k times per output): "at most k".
   - **absent**: a default, not a ban, unless the genre usually has it.
   - **unknown**: anything outputs cannot show. Goes under Unknowns as a
     question the user can answer.
4. **Walk the patterns.** Go through every row of
   [references/patterns.md](references/patterns.md). For each, add evidence to
   the ledger or a question to Unknowns. Most missed rules in real skills are
   in that list.
5. **Draft three candidates** from the ledger, using
   [templates/reconstructed-skill.md](templates/reconstructed-skill.md):
   - A **strict**: only observed and conditional rules.
   - B **menu**: different shapes become a named template menu with triggers.
   - C **loose**: ranges widened, habits as defaults.
   Any example must be new, on a topic none of the outputs use. Never paste or
   lightly edit an original.
6. **Replay blind and score.** For each candidate, generate one output per
   train brief from the draft alone: a subagent given only the draft and the
   briefs, or, without subagents, write each without looking at the original.
   Run `python3 scripts/style_stats.py compare train/ replay/<draft>/` and diff
   each replay against its original block by block. Log every draft's
   per-check results in `history.md`.
7. **Merge and revise.** Read `history.md` first. Build the next draft from the
   checks each candidate won; do not average checks into one score. Fix the
   rule behind each remaining difference. Stop after 3 rounds or when a round
   fixes nothing.
8. **Held-out test, then freeze.** Open `heldout/`. Infer their briefs, replay
   with the final draft, run `compare heldout/ replay/heldout/`, and diff. Also
   replay one brief with a generic prompt as a negative control: it must look
   clearly worse, or say the comparison does not discriminate. After this
   step the rules are frozen. Any later change goes under "Untested changes"
   in the skill and the report.
9. **Leak check.** Run `python3 scripts/style_stats.py leak SKILL.md train/`.
   Only lines repeated in every original (sign-offs, fixed CTAs, headers) may
   match. Remove any other match.
10. **Export.** Write `SKILL.md` from the final draft and `report.md`: ledger,
    history, held-out result per check, negative control, leak count,
    unknowns.

## Finish

Report to the user:
- Each rule's class and evidence count, so they know what is proven.
- Held-out result per check. Never merge checks into one "pass".
- The Unknowns, as questions the user can answer or test.

## Common mistakes

| Mistake | Fix |
|---|---|
| Copying originals as examples | New example on an unused topic; leak check |
| A habit seen in 5 of 5 becomes a hard rule | Class it as a default |
| A sample range becomes a hard limit | Class it as range or capped; widen it |
| Writing a device the source likely bans into the template | Check it against P1 first |
| Each brief type gets its own rule | One template menu with triggers |
| "Always include" for a section that could be optional | "Usually", plus a question |
| Editing rules after the held-out test as if tested | Freeze; list as Untested changes |
| Topic words in rules | Topic is brief, unless it holds N/N across varied topics |
