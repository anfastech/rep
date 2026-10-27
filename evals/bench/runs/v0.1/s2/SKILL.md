---
name: operator-linkedin-post
description: Use when writing a LinkedIn post in a plain, first-person operator voice from a brief (a lesson, a data finding, an experiment, a how-to, or a company announcement).
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out; rules 7, 8, 20b, 23 revised after the held-out test)
  method: reverse-engineer-skill v0.1
---

# Operator LinkedIn Post

Input: a brief with the author's role, the topic, the facts and numbers, and the takeaway. Output: one plain-text LinkedIn post, about 220 words, in short blocks separated by blank lines.

## Template

```
<Hook: one sentence. The most striking fact, number, or claim.>

<One short line that sharpens the hook.>

<Optional third short line: the cost, the number, or the twist.>

<Context: what happened or what you did. 2 to 4 sentences, one of them long (18 to 30 words).>

<Reframe: a short contrast line, worded fresh for the brief.>

<Optional pivot line, sometimes "Here is what ...">

<Core: the specifics. Story beats, findings, or a list.>

<What changed, with the result as a number when the brief has one.>

<Optional: one parallel triple line.>

<The lesson, stated plainly. "Now the rule is ...", "My take: ...", or "If you ..., do not ...">

<Closing line: short imperative or balanced aphorism. 1 to 2 sentences.>
```

## Rules

1. Plain text only. No headings, no bold, no bullet symbols, no links. [observed 7/7]
2. Never use emojis or hashtags. [absent 0/7]
3. Never use contractions. Write "did not", "it is", "do not", "we are". [absent 0/7]
4. Never use em dashes, en dashes, or double hyphens. Use periods and commas. [absent 0/7]
5. Never use exclamation marks. [absent 0/7]
6. Never end on a question, a poll, or "Agree?" / "Thoughts?". No request to comment or share. [absent 0/7]
7. Length about 205 to 265 words; aim for about 225 to 240. Do not stop under 210. [range observed 211 to 242, N=7 incl. held-out]
8. 14 to 19 blocks; aim for 15 to 18. Put a blank line between every block. Most blocks are one or two sentences; none longer than four. [range observed 14 to 18 blocks, N=7 incl. held-out]
9. Short sentences, average about 8 to 10 words. Mix them: fragments and 3-word lines ("It was not.") sit next to fuller sentences. Every post has at least two sentences of 18 to 30 words, and none longer than 30, usually in the context and explanation blocks, often carrying a comma list of three items. Do not write a post made only of short lines. [range observed mean 7.6 to 9.7, max 19 to 30, N=5]
10. Line 1 is the hook: exactly one sentence, alone, about 7 to 20 words. It states a fact, a number, or a flat claim. It is not a question. Keep it to one clause: do not join two facts with "and" or a comma to fit them on line 1. The next fact goes on line 2. [observed 7/7; length range 8 to 18]
11. Line 2 is one short standalone sentence that sharpens or explains the hook. Often lines 2 and 3 are both single short lines. [observed 5/5]
12. Put the brief's key number in the first three lines when there is one. [tendency 4/5]
13. Write numbers from the brief as digits (12, 3,000, 41%, 22). Small numbers may be spelled out at the start of a sentence. [observed 5/5]
14. Include at least one contrast reframe, worded for this brief, not copied from a formula. Shapes seen: a fragment pair ("Not A. Not B. From C."), two short opposed sentences, "We had been treating it as X. It was Y.", "not X, Y" inside a sentence. Use a given shape at most once. [observed 5/5, held-out 2/2]
15. Write in first person. "I" for the author's own choices and mistakes, "we" for the team or company. Address the reader as "you" mainly near the end. [observed 5/5]
16. Admit what you got wrong, expected, or used to do, when the brief contains it. Do not invent a mistake, a worry, or facts the brief does not give. [tendency 3/5]
17. In about half of posts, open the core section with a pivot line starting "Here is what ...". Skip it when the story flows without it. [tendency 3/5]
18. Use one parallel triple or repeated word somewhere, in a shape that fits the post: a fragment run ("Same A. Same B. Same C."), an in-sentence run ("one A, one B, one C"), or repeated adjectives ("real A, real B, real C"). Vary the shape; do not default to "Same". [tendency 4/5]
19. If the brief has 3 to 4 parallel items (benefits, changes), write each as its own plain line, one after another with no blank lines and no bullets, each a full phrase of 6 to 12 words; or, for short items, as fragments together on one line ("Clearer A. Fewer B. Plain C."). [conditional 2/5: brief has a short parallel set]
20. If the brief is a how-to or set of tactics, use a numbered list: "1. Short imperative title." on one line, then 1 to 2 explanation sentences on the next line, blank line between items. 3 to 5 items. Before the list, one line naming who it is for and a "Here is what works ..." pivot. After the list, one line saying what the reader does not need. [conditional 1/5: tactics brief]
20b. If the brief is a set of personal changes or habits ("what I do differently now"), announce the count in one short line, then write each change as a short first-person statement line, with 1 to 3 sentences of explanation on the next line. No numbers, no bullets, blank line between items. [conditional 1/7: personal-change brief, seen only in held-out]
21. If the brief is a company announcement or hiring news, state the news in the hook, give the reason in a "Why X?" line answered on the next line, say who should reach out and which roles are open, and thank the people involved. Close with a forward-looking line. [conditional 1/5: announcement brief]
22. The block before the close states the lesson plainly, in the form that fits: a team rule ("These days our rule is ..."), a take ("My take: ..."), advice ("If your X ..., do not start with Y."), or a summary of what the tactics need. For an announcement, this is a stance on how you will do it, not a rule. [observed 5/5, form varies]
23. The last line is short and standalone and restates the lesson. Pick the form that fits the post; do not default to one. Forms seen: a two-beat imperative ("Do X first. Then Y."), a single imperative with its reason, a balanced aphorism ("Small A, used well, beats big A never used."), a two-sentence mirror that repeats a phrase with a twist, a forward-looking line for announcements, or advice to the reader plus what they might find. It restates the lesson, it does not add new facts. Save the takeaway and the final result for the second half; do not state either in lines 1 to 3. [observed 7/7, form varies]
24. Keep the tone calm and practical. No hype words, no "game changer", no motivational sign-off. [observed 5/5]

## Example

Brief: author runs a field service team. Moved shift handovers from a 30-minute call to a written note. Handover calls had 8 people; half had nothing to report. Written note takes 5 minutes. Missed jobs at shift change fell from 14 a month to 3.

```
We stopped doing shift handover calls in March.

The call was not the safety net I thought it was.

Every shift change, 8 people joined for 30 minutes. Half of them had nothing to say.

The other half talked through jobs that the next shift would forget by lunch, because nothing was written anywhere.

I kept it because it felt careful. Talking things through felt safer than writing them down. I had run that call for three years.

It was not safer. It was just louder.

Here is what we do now:

One written note per shift, owned by one named person.
Open jobs first, then risks, then anything odd.
5 minutes to write, and 2 minutes for the next shift to read.

The next shift reads it before they start. If something is unclear, they ask the one person who wrote it.

Missed jobs went from 14 a month to 3. Nobody has asked for the call back.

The note works because it forces a choice. You cannot write down everything, so you write down what matters.

Same team. Same jobs. Fewer surprises.

If your handovers run long, do not shorten the call. Replace it with a note for two weeks and watch what happens.

Write it down. Then hand it over.
```

## Unknowns

What the source skill may contain that the outputs cannot show. Do not act on these as rules.

- A banned word or phrase list.
- The author persona. All 7 outputs read as a head of operations at a logistics software company; this may be fixed in the source skill or passed in each brief.
- Whether British spelling is required (one instance seen: "favours").
- Behaviour for briefs unlike the five seen (for example, a celebration, a hot take with no data, a book review).
- Whether a hook formula list exists in the source.
- Exact length limits; the source may state a word count.
