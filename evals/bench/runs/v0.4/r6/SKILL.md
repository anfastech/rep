---
name: target
description: Use when turning a user's raw notes (a result, a mistake, a playbook, an announcement) into a ready-to-post LinkedIn caption with first-line alternatives.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# LinkedIn caption writer

Input: raw notes (what happened, the numbers, the point, any link). Output: the caption saved to a markdown file, and a reply in the fixed format below.

## Template

Reply with exactly these blocks, in this order:

**Saved to `~/captions/<YYYY-MM-DD>-<topic-slug>.md`**

**Platform:** LinkedIn
**Shape:** <Shape name>. <One sentence on why this shape fits, citing the fact that decided it.>
**First line pick:** <One sentence on why this first line stops the scroll.>

```
<caption>
```

**Runner-up first lines:**
- "<alternative first line>"
- "<alternative first line>"

**Comment keyword:** none (no link)

**Next action:** Post it, and reply to every comment within the first hour.

## Shape menu

Check in this order and take the first that fits.

1. **The lesson from a mistake**: the notes describe something that went wrong, with a cost and a lesson about doing it differently next time. The highest-trust shape. Moves: the decision and the damage; the cost; what I believed vs what happened; what I'd do now, one short step per line; question. (Seen once; trigger and skeleton unconfirmed.)
2. **Before and after**: the notes hold a real, measured contrast (a before number and an after number). Moves: the contrast or its strangest number; how you found it or what you did; the change; the result; optionally a one-line takeaway; question. [2/5]
3. **Show the thing**: no mistake and no measured contrast; there is a playbook, launch, office or offer to show. State the thing plainly and name the audience it serves. A playbook goes: a claim line, an intro line ending in ":", then one imperative step per line. An announcement goes: the news, the numbers, why it matters, the ask as the closing question. [2/5]

## Rules

1. Output exactly the template, blocks in order, fixed lines verbatim. [observed 5/5]
2. Saved line: today's date, then a 3 to 6 word kebab-case topic slug. [observed 5/5]
3. Shape line: the shape name, a full stop, then one sentence (about 10 to 25 words) of justification. When a higher shape was ruled out, say so briefly. [observed 5/5]
4. First line pick: one sentence about the hook; do not quote the hook again. [observed 5/5]
5. Caption: every sentence on its own line (two or three short ones may share a line), a blank line between lines. Plain text: no markdown, no bullets, no numbered steps. [observed 5/5]
6. First line: the most concrete fact or a flipped assumption, about 12 to 16 words, under about 100 characters, no warm-up. [range 12 to 16 words, N=5]
7. Second line: short, adds the stakes or the proof. [tendency 5/5]
8. Last line: one specific question asking readers about their own experience or for help. It is the only question in the caption. [observed 5/5]
9. Runner-up first lines: exactly 2, quoted, each a different angle (for example one number-led, one lesson-led), about 8 to 15 words. Usually one of the two (not both) is two short sentences, or a question then its answer; the other is a single sentence. [observed 5/5; two-sentence form tendency 4/5]
10. Comment keyword: "none (no link)" when the notes have no link. [conditional 5/5, all no-link]

## Defaults

1. Caption length about 55 to 100 words, 5 to 10 lines. Don't pad to fill it. [range 58 to 92 words, 5 to 9 lines, N=5]
2. Use only the notes' facts. No added setup lines ("most teams..."), no invented numbers. [tendency]
3. Digits for numbers, words at the start of a sentence. [tendency]
4. First person (I or we), contractions, short plain sentences. [tendency]
5. No emojis, hashtags, exclamation marks or dashes. [absent 0/5]
6. At most 2 contrast lines ("not X", "X. It was Y") and at most 1 closing takeaway line. [capped max 2 / max 1]

## Example

Notes: our bakery stopped baking to a fixed list and started baking to yesterday's sell-out times; waste fell from 30 loaves a day to 8. No link.

```
We used to throw away 30 loaves of bread every single day.

Now it's 8.

We stopped baking from a fixed list each morning.

Instead we bake to the time each loaf sold out yesterday.

The ovens and the team stayed the same.

What would you change if you planned tomorrow from yesterday's last sale?
```

## Unknowns

- Are there more shapes, and what is the full order? Is "The lesson from a mistake" skeleton fixed (labels like "What I believed:")?
- What happens when the notes include a link (comment keyword, link in first comment)?
- Does the skill support platforms other than LinkedIn, with their own limits?
- Is there a per-user voice file? Banned words? Length tiers?
- Are AI-tell devices (contrast reveals, aphorisms) banned or capped? Dashes absent: skill rule or generator setting?
- Is the "Next action" ever different (scheduling, timing advice)?
