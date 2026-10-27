---
name: x-thread-writer
description: Use when turning a brief (a story, result, opinion, how-to, or announcement) into a ready-to-post X (Twitter) thread with an outline, the full thread, alternate hooks, and posting instructions.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out); 1 rule added after the held-out test
  method: reverse-engineer-skill v0.1
---

# X Thread Writer

Input: a brief with the author (role, company, audience), the topic, the facts and numbers, and the point. Output: one Markdown document with exactly four sections: outline, full thread, 4 hook variations, posting instructions.

## Step 1: Pick the template

Match the brief to one template. The tweet count comes from the template; adjust by one or two if the brief has more or fewer steps. The beat lists are defaults: when the brief is built from its own parts (for example 3 changes, 4 steps), swap the middle beats for those parts and label them `Change 1`, `Change 2` and so on, keeping Hook, Context, Lesson, Apply, TL;DR, and CTA. [held-out 1/2; added after the held-out test, so untested]

| Brief type | Outline first line | Beats, one per tweet |
|---|---|---|
| Personal story, usually a mistake or turning point | `Template: Story Thread (10 tweets)` | Hook, Context, Problem, Turning point, Action, Obstacle, Lesson, Apply, TL;DR, CTA |
| A project with a measured result | `Template: Case Study Thread (11 tweets)` | Hook, Background, Before, Strategy, Implementation, Challenge, Results, Takeaway 1, Takeaway 2, Replicate (a numbered playbook that doubles as the summary), CTA |
| An opinion against common practice, backed by a test or data | `Template: Contrarian Take (10 tweets)` | Hook, Common wisdom, Why it's wrong, Evidence, More evidence, What to do instead, Expected results, Objection, Conclusion + summary, CTA |
| How to do something, in steps | `Template: Tutorial Thread (N tweets)` | Hook, Context, Step 1 ... Step N, Common mistakes, Expected results, TL;DR, CTA |
| News: launch, office, hire, milestone | `Format: Short announcement thread (N tweets)`, 7 to 9 tweets | Hook, Context, Why now, 2 or 3 detail beats, why it matters to the reader, TL;DR, CTA |

## Template

```
## 1. Thread Outline

Template: <Template name> (<N> tweets)
- Hook: <the hook's facts in a compressed phrase>
- <Beat>: <one short phrase on what this tweet says>
...
- CTA: follow + retweet + reply

## 2. Full Thread

Tweet 1 (<chars> chars)

<line>

<line>

<line>

Tweet 2 (<chars> chars)

<line>
...

## 3. Hook Variations

A. <Hook type>
<line>

<line>

B. <Hook type>
<line>
...

## 4. Posting Instructions

- Suggested posting time: <Day or days>, <time> ET. <One sentence on why: what the target audience is doing then.>
- Post all at once as a native thread. No delays between tweets.
- Recommended first reply: <a bonus asset or tip: a template, a checklist line, a screenshot description, a link>
- Engagement plan for the first hour:
  - Stay online for 60 minutes after posting.
  - <specific reply tactic for this thread>
  - <specific reply tactic>
  - <quote-tweet or re-share tactic>
```

## Rules

### Structure

1. Output exactly the four sections with these headers, in this order: `## 1. Thread Outline`, `## 2. Full Thread`, `## 3. Hook Variations`, `## 4. Posting Instructions`. No title, no preamble, nothing after section 4. [observed 5/5]
2. The outline is the template line, then one `- Label: note` bullet per tweet. Bullet count equals tweet count. Notes are short phrases, not sentences. The TL;DR beat is just `- TL;DR`. [observed 5/5]
3. The CTA beat is written `CTA: follow + retweet + reply`, reordered or extended when the CTA differs (for example `CTA: tag a friend + link + retweet + follow`). [observed 5/5, verbatim 3/5]
4. Thread length: about 8 to 12 tweets. [range observed 8 to 11, N=5]
5. Each tweet starts with a header line `Tweet N (X chars)`, then a blank line, then the body. X is the exact character count of the body, counting line breaks. Count it; do not estimate. [observed 50/50 tweets]
6. Keep tweets short. Most land between 110 and 230 characters; never go above 250, even though X allows 280. Each tweet has 3 to 7 lines. [range observed 111 to 231 chars, 3 to 7 lines, N=50]

### Line style

7. One sentence or fragment per line. A blank line between every line. [observed 5/5]
8. Lists are the exception: list items sit on consecutive lines with no blank lines between them. Use `→ ` for unordered lists and `1. ` for ordered ones. Put a short lead-in line ending in a colon above the list. [observed 5/5]
9. Lines are short: most are 4 to 11 words, and no line goes past 14 words. Mean sentence length is about 9 to 10 words. Fragments are fine ("Not bugs." "Same product."). Use parallel repetition for rhythm ("Same customers. Same product. Same team."). [range: mean sentence 9.1 to 9.8 words, longest line 10 to 14 words, N=5]
10. Write every count and measure as digits, even small ones: "1 site", "4 moves", "2 weeks". Use `%` and commas in thousands. "One" is fine as a pronoun or for emphasis ("every single one", "one decision"). [observed 5/5]
11. Use contractions. Plain words, no jargon. First person ("I" for personal stories and opinions, "we" for team results and company news). Speak to the reader as "you" in lessons and steps. [observed 5/5]
12. Never use hashtags, em dashes, en dashes, or exclamation marks. [absent 0/5]
13. No emojis, with one exception: a company announcement may use a single relevant emoji (such as a country flag) in tweet 1. [conditional 1/5: announcement]

### Tweet roles

14. Tweet 1 (hook): 3 to 5 short lines, about 120 to 160 characters, the shortest or near-shortest tweet in the thread. Lead with the most concrete number or result in the brief. Usually it ends with a line that points into the thread and ends in a colon: "Here's what happened:", "Here's how:". A tutorial hook may open with "How to <do X>:". An announcement hook states the news plainly. [tendency 3/5 colon ending]
15. Tweet 2 (context): opens with a short framing line such as "Some context." or "Some background.", then states who the author is (role, company size, industry from the brief) and the situation. Describe the author once, in tweet 2 only; do not repeat the company description in the outline, later tweets, hooks, or posting notes. A personal reflection may skip the framing line and open with how the author used to work. A contrarian thread instead opens tweet 2 with "The common belief:". [tendency 4/5]
16. Middle tweets each carry one beat. Open beat tweets with a short label line when the template has numbered parts: "Step 1: <action>.", "Takeaway 1: <claim>.", "The lesson: <claim>.", "What to do instead:", "Common mistakes to avoid:", "What to expect:". [observed where the beat exists]
17. A contrarian thread includes an objection tweet that opens with the objection as a quoted question, then answers it. [conditional 1/1: contrarian]
18. The second-to-last tweet is a numbered summary. It opens `TL;DR:` (or, for a case study, `How to run this yourself:`), lists 4 or 5 numbered points, then usually one closing line such as "Save this before your next <thing>." [observed 5/5 numbered summary; TL;DR label 4/5; save line 3/5]
19. The last tweet is the CTA, one line each, blank lines between: [observed 5/5]
    - "Follow me for more <kind of content the author posts>."
    - "Retweet the first tweet <so / to / if> <reason tied to the topic>."
    - A question tied to the topic, ending "Reply below." or "Reply with <what>."
    Order may change. Always "Follow me", never "Follow us", even for company news. An announcement swaps the question for an action (tag someone, share a link). The CTA tweet is 3 or 4 lines.
20. If the brief mentions a link that was not supplied, write `[link]`. [observed 1/1]

### Hook variations

21. Exactly 4 alternatives, labeled `A. <Type>` to `D. <Type>`. The hook text starts on the line right after the label; blank lines between its lines. Each is 1 to 4 lines. [observed 5/5]
22. Use different types. Pick from: Story opener, Bold claim, Contrarian, Stat, Stat + insight, Result, Result + Timeframe, Curiosity, Challenge, Listicle, Do this not that, Behind-the-scenes, or a type named after the brief (for example Hiring-led). Include a Contrarian one unless the brief is an announcement. [tendency 4/5 contrarian]
23. Most variations end with a colon that points into the thread. [tendency 15/20]

### Posting instructions

24. Exactly four bullets, in this order and with these labels: `Suggested posting time:`, the fixed line `Post all at once as a native thread. No delays between tweets.`, `Recommended first reply:`, `Engagement plan for the first hour:`. [observed 5/5]
25. Posting time names a weekday (or two) and a time in ET written like `9:00am ET` or `8:30am ET`, then one sentence on why it suits this audience. Add a local time in parentheses when the brief has a non-US audience. [observed 5/5]
26. The first reply is a concrete bonus: a quoted one-line tip, a template, a screenshot description, or the link again. [observed 5/5]
27. The engagement plan has 4 sub-bullets. The first is always `Stay online for 60 minutes after posting.` The other 3 are one tactic each, specific to the thread: which questions to answer in detail, what to ask repliers, quote-tweet the best reply, or re-share the hook from your own account once, half an hour in, if replies are slow. [observed 5/5; re-share line 3/5]

## Example (new topic; shows form only)

```
Tweet 1 (141 chars)

Our team stopped using shared inboxes for 6 weeks.

Response time fell from 9 hours to 2.

Nobody missed the old setup.

Here's what changed:
```

```
A. Curiosity
There's one setting in every shared inbox that slows your whole team down.

Most teams never touch it:
```

## Unknowns

Things the source skill may hold that the outputs cannot show. Do not act on these as rules.

- Whether the author persona is fixed in the skill or comes from the brief. All 7 sources share one author (same first name, role, and company in every source; the name appears in 2 outlines).
- Templates the skill may have that the sources never triggered (for example a listicle or tool-roundup thread) and their beat lists.
- Exact tweet count rules per template, and whether long briefs split into more tweets.
- Any banned word or phrase list.
- Whether the skill asks clarifying questions or adds anything when the brief is thin.
- How it handles images, polls, or links inside the thread.
