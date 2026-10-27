---
name: operator-linkedin-post
description: Use when writing a LinkedIn post in the first-person voice of a hands-on operator (a story, data finding, experiment, framework, or announcement) from a brief of facts.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out; rules 19a and 19b use held-out evidence)
  method: reverse-engineer-skill v0.1
---

# Operator LinkedIn Post

Input: a brief with the author's role, the facts (what happened, numbers, names), the takeaway, and optionally a link/CTA or hashtags. Output: one plain-text LinkedIn post, about 200 words.

## Template

```
<Hook: one statement, the sharpest number, result, or admission>

<Setup: what I believed, decided, or wanted, and why it seemed right>

<What happened: concrete events and numbers>

<Result: short block, often one sentence>

<Why: the cause or the insight, plain>

<So ...: what we changed or the rule now>

<Honest cost: what it costs, what is unsolved, or what I got wrong>

<Closing question about the reader's own version of this>

[P.S. <CTA pointing to the first comment>]      only if the brief has a link/CTA

[#tag #tag]                                     only if the brief gives hashtags
```

Blocks may merge or repeat; the order hook, setup, events, insight, change, cost, question holds.

## Rules

Format
1. Plain text. Every paragraph is its own block, separated by one blank line. [observed 5/5]
2. Paragraphs are 1 to 3 sentences, most of them 2. A list item may reach 4. [range observed 1 to 4, N=5]
3. Length about 170 to 250 words. Keep it to about 8 to 10 prose blocks, not counting list lines, P.S., or hashtags. Fewer, fuller paragraphs beat many tiny ones. [range observed 181 to 235 words, 9 to 10 blocks, N=5]
3a. Sentences average about 11 to 16 words. Mix medium sentences joined with "and", "but", or a comma with a few short ones; one long sentence (25+ words) per post is normal. Do not stack fragments or one-line zingers; at most 2 sentences under 6 words in the whole post. [range observed mean 10 to 17, max 21 to 46, N=5]
4. No emojis, no exclamation marks, no em or en dashes, no bold, headers, quotes, parentheses, or semicolons. [absent 0/5]
5. No URLs in the post. [absent 0/5]

Hook
6. Line 1 is a single statement, never a question. [observed 5/5]
7. It leads with the most concrete thing in the brief: a number ("<N> of our <X>..."), the result, or a plain admission of a mistake. If the brief has no number, use the admission, or a claim about what most people in the reader's role do. Do not warm up. [tendency 4/5 have a number in the first two lines]
8. Hook length about 10 to 25 words; a two-line announcement hook counts as one. Up to 2 sentences. [range observed 11 to 21, N=5]

Body
9. Write in first person singular for decisions and feelings ("I decided", "I assumed"), "we" for the company or team. [observed 5/5]
9a. Mention the author's role only in passing, when it explains why the problem was theirs. Never open with it. [tendency: role stated 2/7]
10. Usually state what you expected or believed before the facts, then show how reality differed (a line on what you believed, then the fact that broke it; or "The part I didn't see coming ..."). [tendency 4/5]
11. Use digits for counts and stats (12, 41%, 3,000) and reuse the same figures across the post so the numbers carry the story. [observed 5/5, 5 to 10 numbers per post]
12. Give the key result its own short block, often one sentence. Only one such block per post (two only for a split before/after pair). [tendency 3/5]
13. When the brief has a change or decision, introduce it with one paragraph starting "So": "So now, ...", "So we ...". At most one "So" paragraph per post. If the brief has no change, skip it; do not invent one. [tendency 3/5, max 1 per post]
14. State the lesson as a decision, a rule, or a plain claim. Never label it ("lesson", "key takeaway", "here's what I learned"). [absent 0/5]
15. Include exactly one honest beat: the cost of the change, what is still unsolved, what the author got wrong, or the author's own weak position. Write it fresh each time; do not reuse a stock opener across posts. In story posts it sits just before the question; in framework posts it sits just before the list, to earn the advice. [observed 5/5]
16. Use contractions. Plain, concrete words, short declarative sentences, calm tone, no hype. [observed 5/5]

Conditional shapes
17. If the brief has several findings from data: one block that ends in a colon ("The <analysis> showed this:"), a blank line, then 3 lines starting with "→ " on consecutive lines (no blank lines between them). Each arrow line is a lowercase fragment with no final period, except when it starts with a number. Use findings that are in the brief or follow directly from it. [conditional 1/5: data finding]
18. If the brief is a framework or set of moves: open on what most people do and why it fails, announce the count in words at the end of the lead-in line, ending with a colon, then numbered items "1. ", each its own block: a short imperative sentence, then 1 to 3 sentences of explanation. Each item is one line: the imperative sentence and its explanation on the same line. Address the reader as "you" in this type. After the list, one short paragraph that reframes why the moves work, then the question; no extra advice blocks. [conditional 1/5: how-to]
19. If the brief is an announcement: the hook may be two one-line blocks contrasting before and now (a past state in one block, the present state in the next). Then the plan, the hard parts (not all solved), and what surprised you. [conditional 1/5: announcement]
19a. If the brief is a personal change with several parts: one short line announcing how many things changed, then one paragraph per change, each opening with a short first-person claim followed by 1 or 2 sentences of why. No list markers. [conditional 1/7: held-out 06, added after the test]
19b. If the brief thanks a colleague: lead with the result their work produced, thank them directly in one short early block, explain before and after, and close by widening to the reader's own team. [conditional 1/7: held-out 07, added after the test]

Close
20. End with exactly one question, the only question mark in the post. It asks about the reader's own parallel situation in specific terms. Usually ask about their real past experience ("What ... would you do differently if you could ...?", "When you've ..., what ...?", "If you've ..., what do you wish ...?"); sometimes a hypothetical ("Which of your ... would still ... if ...?"). Do not default to "tomorrow" hypotheticals. Never "What do you think?". [observed 5/5; 3/5 past experience, 2/5 hypothetical; length 12 to 19 words]
21. If the brief has a link or CTA: after the question, add a blank line and "P.S. <the thing> is in the first comment." [conditional 1/5: CTA]
22. If the brief gives hashtags: last line, at most 2, after a blank line. Otherwise none. [conditional 2/5: brief supplied, unverified]

## Example

(New topic, not from the sources.)

We stopped giving candidates a take-home test 6 months ago. 4 of our last 5 hires would have failed it.

I liked the take-home. It was cheap for us, and I believed it filtered out people who couldn't do the work.

Then we looked at who actually performed in their first 90 days. The best 4 people we'd hired that year had all scored in the bottom half.

The test measured how much free time someone had on a weekend.

So we replaced it with a paid half day. The candidate works on a real problem with the person they'd report to, and we pay them for it.

It costs us about $400 per finalist and a lot more calendar time. I'd still rather pay that than keep rejecting the people we most want.

If you looked at your best hire from last year, would they have passed your current process?

## Unknowns

What the source skill may contain that the outputs cannot show. Do not act on these as rules.

- Whether the operations-leader persona is fixed in the skill or came from each brief.
- Any banned word or phrase list beyond what is absent above.
- When hashtags are added (brief-supplied, a topic rule, or random).
- Rules for brief types not seen: personal milestones, hot takes with no data, reposts, polls.
- Whether a target length or reading level was stated.
- Whether the source has stock phrases for the honest beat (one such opener appears in 2 of 7 outputs).
- Whether hashtag count is capped (seen 0, 1, or 2).
