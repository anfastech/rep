---
name: target
description: Use when asked to write a short first-person LinkedIn-style post from a brief (story, lesson, data finding, experiment, tips, announcement).
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out; final edits after held-out test)
  method: reverse-engineer-skill v0.1
---

# Plain first-person post writer

Input: a brief with the facts, numbers and takeaway. Output: a plain-text post, then a short note to the requester.

## Template

<Opening: the plain fact of what happened or what is true, 1-2 sentences>

<Turn/result: short paragraph, often a single short sentence>

<Why: 1-2 paragraphs of plain reasoning>

<Optional: limit-the-claim line, practical suggestion, or CTA (only when the brief asks for action)>

<Closing line: short plain contrast or summary>

<Note to requester: "I <past verb> ... ." + an offer to adjust>

## Rules

1. Open with the plain fact, not a hook trick: no question, no "thrilled to announce", no stat-bomb one-liner. First paragraph about 15 to 40 words. [observed 5/5; range 19 to 32]
2. Stay with the brief's facts. Do not invent causes, numbers, names or quotes. If something is missing, leave it out and say so in the note ("because the brief doesn't ..."). [observed 7/7; note mention conditional 2/7: missing detail]
3. For a story, experiment or data finding, the first paragraph sets up only the action or method (and, if useful, what you expected). Hold the key result or number for the second paragraph, which delivers it briefly (can be one short sentence). [conditional 3/3 narrative briefs]
4. Explain why in plain, concrete prose. Calm, understated, first person (I or we). Past tense for what happened. Body paragraphs are usually 2 to 4 full sentences, not strings of one-liners. Only the turn (rule 3) and the closing line may be very short. [observed 5/5]
5. Every paragraph adds a concrete point from the brief or one honest observation (what you expected, what surprised you). No filler paragraphs about how big a step something was. Do spend a paragraph on the mechanism: why the situation arose or why nobody had noticed it. For an announcement, give one specific, concrete observation (a small real-world effect) instead of a general benefit. [observed 5/5; announcement part conditional 1/5]
6. Sometimes add one line that limits the claim ("I'm not suggesting...", "None of this makes you..."). At most one per post, and only when the post could be read as a sweeping recommendation. Leave it out of reflections and thank-you posts. [tendency 3/7; held-out 0/2]
7. Usually end the post on a short plain line that ties back to a concrete number or fact from the brief, or a plain cost comparison. Vary the form; do not reuse a stock opener like "The short version:" every time. Avoid abstract aphorisms and mirrored slogan pairs. Announcements may end with a thank-you instead. [tendency 4/5]
8. Write full sentences. Avoid fragments ("Not a bluff, an actual...") and punchy parallel constructions. [observed 5/5]
9. If the brief is a set of separate tips, use: intro sentence(s), a line like "Here's what has worked...:", then numbered items "1. " each with a lead sentence plus 1-3 sentences of reason, blank line between items. Several personal changes or observations (not advice) go in prose instead: one paragraph each, each with a concrete detail. Otherwise no lists. [conditional 1/7 tips list; 1/7 changes in prose]
10. Include a call to action only when the brief asks readers to do something (apply, message). [conditional 1/5: hiring]
11. Stats, money, percentages and counts from the brief as digits (12, 3,000, 41%, 6pm). Short durations may be words ("six months"). Never start a sentence with a digit; reword or spell it out; small counts already given as digits may be repeated in words ("those three screens"). [observed 5/5 for stats; durations held-out 1/2 in words]
12. No questions, no exclamation marks, no emojis, no hashtags, no markdown, no em or en dashes. [absent 0/7]
13. Sentences mostly short to medium, mean about 9 to 15 words, rarely over 32. Use contractions naturally. [range mean 9.9 to 14.0, max 21 to 31, N=7]
14. Post plus note about 150 to 260 words, 5 to 9 paragraphs. Aim near 200; don't trim a full brief down to bare facts. Short announcement briefs can run near the low end. [range 163 to 227 words, 5 to 8 paragraphs, N=7]
15. After the post, a blank line, then one final paragraph (2 sentences) addressed to the requester: first sentence "I <past verb> ..." naming a concrete craft choice and why; second offers an alternative ("Tell me if you'd rather...", "I can make it ... if you want", "Swap in ... if you have it"). No label or heading before it. [observed 7/7]

## Example

(Brief: our bakery switched to a 4-day week for the kitchen team for 3 months; sick days fell, output held flat.)

For 3 months our kitchen team worked four days a week instead of five, on the same pay and the same daily output target. I assumed a shorter week would just mean longer, more tired days.

Output held flat. Sick days fell by more than half.

What changed was the shift trading. Before, people swapped days constantly to cover each other, and nobody really got a full break. Once everyone had a real day off coming, the swapping mostly stopped.

It won't work for every kitchen. Ours has a small menu and predictable orders, which made it easier to try.

We're keeping it, and I expect fewer sick days to pay for the change on their own.

I kept the result in its own short paragraph so it reads as the turn. I can add the before-and-after numbers if you have them.

## Unknowns

- Banned word list, persona backstory, target platform name.
- Whether the note to the requester is always present or toggled by the caller.
- Behavior for briefs unlike these (very long, negative news, multi-person).
- Whether there is a hard word limit.
