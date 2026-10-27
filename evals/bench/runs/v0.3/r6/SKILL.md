---
name: target
description: Use when turning a brief (a mistake, a measured result, a playbook or an announcement) into a short LinkedIn caption that is saved to a file and handed over with the shape choice, alternative first lines and a next action.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# Caption writer

Input: a brief: what happened, the facts and numbers, the platform, any link. Output: one caption saved to a file, shown in a code block, wrapped in a short handover note.

## Template

Output exactly this, nothing before or after:

**Saved to `~/captions/<YYYY-MM-DD>-<topic-slug>.md`**

**Platform:** <platform>
**Shape:** <shape name, copied exactly from the menu>. <1-2 sentences: why this brief fits, naming its key fact or number.>
**First line pick:** <1-2 sentences: why this first line stops the scroll on its own.>

```
<caption, built from the chosen shape>
```

**Runner-up first lines:**
- "<alternative first line>"
- "<alternative first line>"

**Comment keyword:** none (no link)

**Next action:** Post it, and reply to every comment within the first hour.

## Shape menu

Check the shapes in this order and use the first whose trigger holds. Copy the name exactly.

1. **The lesson from a mistake** (the highest-trust shape). Trigger: something went wrong with real damage, and the brief says what you would change next time.
   ```
   <What I did, plainly.>
   <The damage, one fact per line, 1-2 lines.>
   What I believed: <the assumption>.
   What actually happened: <the cost, restated concretely>.
   What I'd do now: <the change>.
   <1-2 short follow-on steps, one per line.>
   <Question>
   ```
2. **Before and after**. Trigger: a real, measured contrast (a number before, a number after).
   ```
   <The contrast or the surprising number, in one line.>
   <How you found it or what you tried.>
   <Optional: one line that sharpens the point.>
   <What changed, with the after number.>
   <Optional: one plain line on what it means.>
   <Question>
   ```
3. **Show the thing**. Trigger: no mistake and no measured contrast; the thing itself (a playbook, an opening, a launch) is the content.
   ```
   <The thing stated plainly, or the usual assumption flipped.>
   Playbook: "Here's how I <do it>:" then one tactic per line, unnumbered, as "<Imperative tactic>. <One short reason.>"
   News: the facts, one per line, then one line on why it matters.
   <Question; for hiring, ask who to talk to.>
   ```

## Rules

1. Fields in template order; the Next action line verbatim. [observed 5/5]
2. Date = today; slug = 3 to 5 kebab words naming the topic. [observed 5/5]
3. Caption: one line per paragraph, blank line between every line. [observed 5/5]
4. Most lines are one short sentence, usually under 15 words. At most 2 sentences on a line, rarely 3 when they are very short. Do not join an action and its result with "and": the result, with its number, gets its own line. [capped max 3; mean sentence 11 to 15 words, N=5]
5. Caption about 55 to 100 words and 5 to 10 lines; stop early rather than add a line. [range 58 to 92 words, 5 to 9 lines, N=5]
6. First line about 11 to 17 words, makes sense with no context, leads with the most concrete number or fact. [range 12 to 16, N=5]
7. Last line: one specific question to the reader about their own experience. [observed 5/5]
8. First person: I for your own decisions, we for team results. [observed 5/5]
9. Two runner-up first lines, quoted, each a different angle from the pick (number-led, lesson-led, tactic-led). [observed 5/5]
10. If there is no link, the comment keyword is "none (no link)". [conditional 5/5: no link]

## Defaults

1. No emojis, hashtags, exclamation marks, em or en dashes, or markdown in the caption. Hyphenated words ("10-person") are fine. [absent 0/5; hyphens 6 to 8 per output]
2. Numbers as digits. [5/5]
3. Contractions (2 to 5 per caption) and plain spoken sentences. [range 2 to 5, N=5]
4. At most 2 contrast moves ("not X", "didn't ... It did ...") and at most 1 triple per caption. [capped max 2 / max 1]
5. No slogan-style closing line; any lesson line stays plain and specific. [tendency]

## Example (new topic)

Caption only, built with the mistake shape; the wrapper is filled as in the template.

```
I raised prices at our bakery by 15% overnight and lost 40 regulars in a month.

Nobody was told in advance.

What I believed: people would barely notice a few cents.

What actually happened: the regulars noticed first and felt surprised.

What I'd do now: tell them two weeks ahead.

Put a note at the register explaining why flour costs went up.

Then change the prices.

How do you tell loyal customers that prices are going up?
```

Runner-ups for it: "40 regulars stopped coming after one silent price change." and "Tell customers before you raise prices. I skipped that step."

## Unknowns

- Are there more shapes than these three (contrarian take, how-to, story)?
- With a link, what does the comment keyword look like?
- Are "Here's the thing" bridges, engagement bait, closing aphorisms banned?
- Other platforms? A character or "see more" limit? Length tiers? A per-user voice file?
