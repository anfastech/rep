---
name: target
description: Use when turning a short brief (a story, data finding, experiment, set of tips, or announcement) into a plain, first-person LinkedIn-style post, followed by a short note to the requester about the choices made.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# Plain first-person post with a note to the requester

Input: a brief with the facts, numbers, people and takeaway for one post.
Output: the post as plain text, then a blank line, then a 2 to 3 sentence note to the requester.

## Template

Pick one shape by brief type.

**Narrative** (story, mistake, data finding, experiment, opinion):

```
<Opening: 1-3 plain first-person sentences, about 20-30 words: what happened or what was done, plus one bit of context or what you expected>

<Optional one-line turn, only when the result broke the expectation stated in the opening>

<Longer paragraph, about 40-75 words: what was really going on>

<Paragraph: what changed, the fix, or what you'd do now>

<Optional short paragraph: perspective or a limit ("I'm not suggesting...", "I don't think...")>

<Closing: one short plain paragraph, about 12-25 words: the takeaway, or "If you..., try..." advice>

<Note to the requester>
```

**Tips** (brief is several separate moves):

```
<1-2 sentences of first-person context>

<Intro line ending with a colon>

1. <Imperative sentence.> <1-3 sentences of reason.>

2. <...>

<One short closing paragraph>

<Note to the requester>
```

**Announcement** (news, launch, hiring):

```
<The plain fact first>

<One concrete observation>

<The ask and where to act>

<Optional one-line thanks>

<Note to the requester>
```

## Rules

1. The output is the post, then a blank line, then a note to the requester. The note has no separator line and no heading. [observed 5/5]
2. The note is 2 to 3 sentences, starts with "I", names the one main craft choice (opening, order, tone, shape) and why. [observed 5/5; range observed 24 to 37 words, N=5, write about 25 to 40]
3. The note usually ends with one offer to adjust ("Tell me if you'd rather...", "I can make it..."). [tendency 4/5]
4. Open with the plain fact or situation in first person. No question opener and no "excited to announce" opener. [observed 5/5]
5. End the post with a short plain takeaway or a practical next step. [observed 5/5; range 13 to 23 words]
6. If the brief is a set of separate moves, use the Tips shape. [conditional 1/5: list brief]
7. If the brief has an ask (hiring, sign-up), state it with where to act. [conditional 1/5: announcement brief]
8. If the brief has a result that broke an expectation, a one-line turn paragraph may follow the opening. [conditional 2/5: surprising-result briefs]
9. Do not invent facts the brief does not give. If the brief is thin, keep the post short instead of padding it. Mention a missing fact in the note only if it changed the post. [conditional 2/5: notes flag missing detail]

## Defaults

1. Calm, modest, plain tone, self-critical where the brief is a mistake. [5/5]
2. Normal contractions, a few per post. [range 2 to 6 per post, N=5]
3. Sentences short to medium, each under about 26 words. [range max 21 to 26, N=5]
4. Post body about 120 to 200 words in 4 to 8 paragraphs; whole output about 150 to 240 words. [range body 126 to 199, whole 163 to 227, N=5]
5. Digits for numbers; spell a number out at the start of a sentence. [5/5]
6. No questions, exclamation marks, emojis, hashtags, dashes used as punctuation, bold or headers. [absent 0/5; emojis and hashtags are strong evidence for this genre]
7. At most 2 contrast lines per post. No "not X, it's Y", "X, not Y" or "it was really X" reveals, no "Here's the thing" bridges, no engagement bait. [capped max 2; reveals 0/5]

## Example

Brief: a library branch manager ran Saturday story hours with no sign-up for one season; attendance went from 15 to 40; staff had to add a second reader; the takeaway is to drop the form.

```
For one season we stopped asking parents to sign up for Saturday story hour at our branch. I expected a few more families and some chaos at the door.

Attendance went from about 15 children to 40.

The form had been doing more than we thought. Parents told us they'd skipped story hour because they didn't know by Thursday whether Saturday would work. Signing up felt like a promise. Without it, they could decide that morning, and a lot of them did. The chaos never showed up. People found a spot on the rug and waited.

We did have to add a second reader by the third week. That was the only change the staff needed.

If a free event at your branch needs a sign-up, ask what the form is protecting before you keep it.

I opened with the change and held the number for its own line so it lands after the setup. I can make the closing less like advice if you'd rather keep it to our branch.
```

## Unknowns

Questions the outputs cannot answer. Do not act on these as rules.

- Are AI-tell devices banned outright (rule-of-three triples, closing aphorisms, "not X, it's Y")? The sample has none of the strict reveal forms but does have mild contrast closers.
- Is there a per-user voice file (tone, banned words, CTAs), or is the calm style fixed?
- Is the no-dash, no-question pattern from the skill or from the generator's global settings?
- Is there a character limit or a "see more" cut target for the opening?
- Are there length tiers (short, standard, long), or is this one band?
- How are links, tables, code or very long briefs handled? None appear.
- Is the note ever skipped, or ever replaced by alternatives (other hooks, versions)?
- Are there voice-protection rules (do not over-polish, never use words the author doesn't use)?
- Is the platform always LinkedIn?
