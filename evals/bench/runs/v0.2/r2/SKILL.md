---
name: x-thread-writer
description: Use when turning a brief (story, result, opinion, how-to, or announcement) into a ready-to-post X (Twitter) thread package with outline, tweets, alternate hooks, and posting plan.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.2
---

# X Thread Writer

Input: a brief with the author's role, the topic, facts, numbers, and the goal. Output: one Markdown package with 4 sections, nothing before or after it.

## Template

```
## 1. Thread Outline

Template: <Template name> (<N> tweets)
- <Role>: <short note, a fragment, on what this tweet says>
  (one bullet per tweet, same order, same count as the thread)

## 2. Full Thread

Tweet 1 (<chars> chars)

<line>

<line>

...

Tweet 2 (<chars> chars)

...

## 3. Hook Variations

A. <Hook type>
<line>

<line>

B. <Hook type>
...

C. <Hook type>
...

D. <Hook type>
...

## 4. Posting Instructions

- Suggested posting time: <Day or days>, <time> ET. <Why this audience is scrolling then.>
- Post all at once as a native thread. No delays between tweets.
- Recommended first reply: <bonus asset: one-line checklist, template, screenshot, link, or tip>
- Engagement plan for the first hour:
  - Stay online for 60 minutes after posting.
  - <specific reply tactic for this thread>
  - <specific reply tactic>
  - <specific reply tactic>
```

## Template menu

These are starting points. Adapt the roles to the brief; add or drop a tweet when the content needs it.

| Template | Trigger | Skeleton (one role per tweet) |
|---|---|---|
| Story Thread | a personal story, mistake, or turning point | Hook, Context, Problem, Turning point, Action, Obstacle, Lesson, Apply, TL;DR, CTA |
| Case Study Thread | a measured result from a project | Hook, Background, Before, Strategy, Implementation, Challenge, Results, Takeaway 1, Takeaway 2, Replicate (doubles as summary), CTA |
| Contrarian Take | an opinion against common wisdom | Hook, Common wisdom, Why it's wrong, Evidence, More evidence, What to do instead, Expected results, Objection, Conclusion + summary, CTA |
| Tutorial Thread | how to do something in steps | Hook, Context, Step 1 ... Step N, Common mistakes (as an arrow list), Expected results, TL;DR, CTA |
| (no match) | announcement, launch, news | Write "Format: <short description> (<N> tweets)" instead of "Template:", and build a short skeleton: Hook, Context, Why now, details, What's next, TL;DR, CTA |

## Rules

1. Output exactly the 4 sections with the headers shown, in order. No preamble, no closing note. [observed 5/5]
2. The outline has one bullet per tweet, in thread order, each "Role: note". [observed 5/5]
3. Each tweet header is "Tweet N (X chars)" where X is the real character count of that tweet's text, newlines included as 1. Count it; do not estimate. Every tweet stays under 280. [observed 49/49]
4. Inside a tweet, each sentence is its own line, separated by a blank line. Never put two full sentences on one line ("Some context." is its own line). Only a short fragment pair may share a line ("Same team. New result."), at most 3 such lines per thread. No thread numbering like "1/". [observed 5/5; fragment lines 1 to 5 per thread]
5. Tweet 1 is the hook: 3 to 4 short lines, the most concrete number or result first. [range 3 to 4, N=5]
6. The second-to-last tweet is the summary. Its first line is exactly "TL;DR:" (no label before it), then a numbered list "1." to "N." with no blank lines between items, then usually 1 or 2 closing lines. In a Case Study the "How to run this yourself:" playbook list replaces the TL;DR. [conditional 4/5 TL;DR, 1/5 case study playbook]
7. The last tweet is the CTA, each ask on its own line: "Follow me for more <topic> ..." , "Retweet the first tweet <so/to/if ...>", and a question or action for replies ("... Reply below."). Order may vary. For hiring or launches, the ask can be to tag someone or visit a link; write links as [link]. [observed 5/5 follow and retweet-first-tweet; question 4/5]
8. Hook Variations: exactly 4, labeled "A." to "D.", each with a type label (Story opener, Bold claim, Contrarian, Stat, Result, Curiosity, Challenge, Listicle, Do this not that, Behind-the-scenes...). Each takes a different angle from Tweet 1. The label line is followed directly by the hook lines. [observed 5/5]
9. Posting Instructions has the 4 bullets shown. Write times as "8:30am ET" or "9:00am ET" (lowercase am, no space); add the local time in brackets when the audience is abroad. The second bullet and the first engagement sub-bullet are fixed text. The other 3 engagement tactics are specific to the topic and audience. [observed 5/5]
10. Thread length: 10 to 12 tweets for a template thread; 7 to 9 for a short announcement. [range 10 to 11 and 8, N=5]

## Defaults

1. Tweets are 100 to 240 characters. [range 111 to 231, N=49]
2. Sentences are short, about 6 to 12 words. [range mean 9.1 to 9.8]
3. The hook usually ends with a colon teaser: "Here's how ...:", "Here's what ...:". Hook variations also often end with ":". [tendency 3/5, 14/20]
4. The context tweet often opens "Some context." or "Some background." on its own line, then states the author's role in one line. [tendency 3/5]
5. Usually include exactly 1 arrow list per thread ("→ item" lines, no blank lines between), 2 to 4 items, for a process, a set of options, or a list of mistakes. Never more than 1. [tendency 4/5, capped max 1]
6. The summary tweet usually ends with a save prompt: "Save this ...". [tendency 3/5]
7. First person, plain words. Short contrast pairs ("The menu was fine. The wait was not.") and repeated openers ("Same X. Same Y.") are used. [tendency 5/5]
8. Use contractions (it's, don't, wasn't, we're), about 10 to 18 per package. [range 10 to 18, N=5]
9. List items (numbered and arrow) are fragments with no period at the end. [observed 0 periods, 5/5]
10. Write counts and amounts as digits ("3 sites", "1 month", "41%"). Keep "one" as a word in phrases: "each one", "one rule", "one decision". [default 5/5]
11. Include a Contrarian option among the hook variations. [tendency 4/5]
12. No hashtags, no em dashes, no exclamation marks, no bold. At most 1 emoji, only when it adds meaning (a flag for a location). [absent 0/5; emoji 1 total]
13. The engagement tactics usually include a 30-minute fallback (retweet the hook when replies stall) or quote-tweeting the best reply. [tendency 4/5]

## Example (one tweet, new topic)

Tweet 3 (118 chars)

So we sent a text 2 days before each due date.

Nothing fancy.

Just the title and a link to renew.

Late returns fell by half.

## Unknowns

- Are there more templates in the menu than the 4 seen (e.g., listicle, thread of tools, personal update)?
- Is the author persona from a per-user voice file or from the brief?
- Are there banned words or banned devices? The outputs use contrast and triples freely.
- Is there a length tier setting (short, standard, long)?
- Do the absent dashes and emojis come from the skill or from the generator's settings?
- How are images, links, and polls handled when the brief has them?

## Untested changes

Added after the held-out test. Not replayed.

- When the brief carries a short list of items (2 to 4 changes, lessons, moves), give each item its own tweet that opens with its number ("1. <item>." then 2 to 3 supporting lines), in place of the middle roles of the template. Do not squeeze them into an arrow list. (Held-out 06: the original used 3 numbered tweets; the replay used one arrow tweet.)
