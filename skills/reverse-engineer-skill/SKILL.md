---
name: reverse-engineer-skill
description: Use when given outputs made by an AI skill, prompt, template, or creator workflow (posts, captions, threads, newsletters, scripts) and asked to recover, reverse engineer, reconstruct, or clone the instructions that produced them, or to build a skill that writes "like these".
metadata:
  version: "0.1-prototype"
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
| Plain text (posts, threads, emails, captions) | built | [references/text.md](references/text.md) |
| Carousels, slides | not built | stop and tell the user |
| Video, audio | not built | stop and tell the user |

Fewer than 3 outputs: say the result will be a guess, then continue.

## Workspace

Create `reverse-runs/<name>/` in the working directory:

```
train/       outputs you study
heldout/     outputs you do not open until step 7
briefs.md    inferred brief per output (the negated part)
ledger.md    one row per feature, with evidence
drafts/v1.md, v2.md ...
replay/v1/, v2/ ...
report.md
SKILL.md     the exported skill
```

Split: hold out 1 output per 4 (min 1). If the user already split them, keep
their split. Do not read held-out files before step 7.

## Method

1. **Negate the content.** For each train output write its brief in
   `briefs.md`: topic, story, facts, numbers, names, takeaway. This is input,
   not skill. It never becomes a rule and never appears in the skill.
2. **Measure the form.** Run `python3 scripts/style_stats.py profile train/`
   (path relative to this skill). Then read each output for what the script
   cannot see: hook type, section roles, voice, conditional parts.
3. **Fill the ledger.** One row per feature, in this shape:

   | Feature | Seen | Class | Rule text |
   |---|---|---|---|
   | Last line is "P.S. ..." | 5/5 | observed | Always end with ... |
   | "Cost" line | 2/5, only failure briefs | conditional | If the brief is a failure ... |
   | Hook length | 8 to 10 words, N=5 | range | Short hook, about 8 to 12 words |
   | Emojis | 0/5 | absent, genre often uses them | No emojis |
   | Banned words | not observable | unknown | (list under Unknowns) |

   Classes and how each becomes a rule:
   - **observed** (N/N across varied briefs): hard rule.
   - **conditional** (present only when a brief property holds): if/then rule
     naming the property. Cite which outputs.
   - **tendency** (k/N, no brief property explains it): "usually".
   - **range** (a number): write the observed range, then widen it. N outputs
     under-sample the true bound. Never turn a sample range into a hard limit.
   - **absent**: a hard "never" only if the genre commonly has the feature
     (emojis and hashtags on LinkedIn). Otherwise a tendency, or unknown.
   - **unknown**: anything a source skill could hold that outputs cannot show
     (banned word lists, persona backstory, rules for briefs you have not
     seen). List it; do not guess it into a rule.
4. **Draft** `drafts/v1.md` from the ledger using
   [templates/reconstructed-skill.md](templates/reconstructed-skill.md).
   Any example in the draft must be new, on a topic none of the outputs use.
   Never paste or lightly edit an original.
5. **Replay blind.** Generate one output per train brief from the draft alone.
   Use a subagent given only the draft and the briefs. Without subagents, write
   each replay without looking at the original. Save to `replay/vN/`.
6. **Score and revise.** Run `python3 scripts/style_stats.py compare train/ replay/vN/`,
   then diff each replay against its original section by section. For each
   difference, fix the draft rule that caused it. A flag is a lead, not a
   verdict. Stop after 3 rounds or when a round fixes nothing.
7. **Held-out test.** Now open `heldout/`. Infer their briefs, replay with the
   final draft, run `compare heldout/ replay/heldout/`, and diff. Also replay
   one brief with a generic prompt ("write a LinkedIn post about X") as a
   negative control: it must look clearly worse. If it does not, your
   comparison is not discriminating; say so.
8. **Leak check.** Run `python3 scripts/style_stats.py leak SKILL.md train/`.
   Only lines repeated in every original (sign-offs, fixed CTAs) may match.
   Remove any other match.
9. **Export.** Copy the final draft to `SKILL.md`. Write `report.md`: ledger,
   per-round flags, held-out result, negative control, leak count, unknowns.

## Finish

Report to the user:
- Each rule's class and evidence count, so they know what is proven.
- Held-out result per check. Never merge checks into one "pass". A check that
  was skipped or unknown is reported as such.
- The unknowns list, as questions the user can answer or test.

## Common mistakes

| Mistake | Fix |
|---|---|
| Copying originals as examples | Write a new example on an unused topic; run the leak check |
| "8 to 10 words" from 5 samples becomes a hard rule | Class it as range; widen it |
| Never testing the draft | Steps 5 to 7 are the method, not extras |
| Topic words in rules ("for SaaS founders") | Topic is brief, unless it holds in N/N across varied topics |
| Confidence only in the chat reply | Evidence goes in the skill and report |
| Inventing a banned-word list | Unknown, listed, not guessed |
