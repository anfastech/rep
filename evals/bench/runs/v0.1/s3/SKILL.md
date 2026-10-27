---
name: linkedin-operator-post
description: Use when writing a LinkedIn post for an operator or team lead from a brief (a lesson from a mistake, a data finding, an opinion, a how-to, or an announcement).
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.1
---

# LinkedIn Operator Post

Input: a brief with the author (role, company), the post type, the facts and
numbers, the takeaway, and any call to action. Output: one LinkedIn post as
plain text, ready to paste.

## Template

```
<Hook: 1 or 2 sentences, its own paragraph>

<Context: what happened or how we found it, 2 to 4 sentences>

<Body: why it happened, or the reasons, or the numbered steps>

<Action: what we do now / what we changed, often opening with "So" or "Now">

<Reframe: the lesson as "looks like X, is really Y", or a common belief to drop>

<Optional: one short practical block (a side benefit, or direct advice)>

<Closing question to the reader about their own experience>

#Tag1 #Tag2 #Tag3
```

Blocks may merge or split, but the order holds. Each type in rules 8 to 12
lists its own block order; follow it, and do not add blocks it does not list.

## Rules

Each rule ends with its evidence tag.

### Shape

1. The hook is the first paragraph and stands alone. One or two sentences. [observed 5/5] Length about 8 to 35 words. [range observed 10 to 30, N=5]
2. Pick the hook by post type: [conditional, one output per type]
   - Mistake: what I did, then the cost, with a hard number.
   - Data finding: open on the statistic itself (a percent or count plus the time window).
   - Opinion: start with "Unpopular opinion: " and the claim in one sentence.
   - How-to: "How to <do X> when <constraint>:" ending in a colon.
   - Announcement: a plain statement of the news, starting "We've" or "We're".
3. Write the body as short prose paragraphs of 1 to 4 sentences, one blank line between them. Never put each sentence on its own line. [observed 5/5]
4. Total about 170 to 280 words in about 6 to 10 blocks including the hashtag line. [range observed 181 to 251 words, 6 to 9 blocks, N=5]
5. One block states the takeaway, right after the action: a reframe ("On paper this is slower; against the cleanup it is faster") or the belief readers should drop. Exactly one such block; in an opinion post the recommendation paragraph is the takeaway, and an announcement has none. [conditional 4/5: not announcement]
6. Usually bring the hook's key number (the cost, result, or count) back near the end so the post closes the loop. [tendency 4/5]
7. The paragraph that turns from problem to action usually opens with "So" or "Now". [tendency 3/5]

### Type parts

8. Mistake. Order: hook; the reasoning at the time, told fairly (it seemed sound); what broke and who paid for it; the new practice ("Now ..."); the reframe; a side benefit of the new practice; question. [conditional 1/5: mistake]
9. Data finding. Order: hook; how the data was gathered plus what you expected versus what you found; why the pattern exists; what you changed and the result ("So ..."); the reframe (how you used to see the problem versus now); one paragraph of direct advice, "If your <problem>, <do this> before you <costly default>."; question. [conditional 1/5: data]
10. Opinion. Order: hook; a personal test with its numbers; a lead-in line like "<Number> reasons I think this happens:" on its own line; one paragraph per reason, each opening with the reason as a plain sentence; "What I'd recommend instead ..." with the callback to the test's numbers; question. No extra reframe block. [conditional 1/5: opinion]
11. How-to. Order: hook; one paragraph with the author's role, company size and why the advice still works for them, ending "These <number> moves ..."; numbered items "1. ", "2. " each its own paragraph, an imperative first sentence then 1 to 3 sentences on why it works; one paragraph naming the common assumption the list disproves; question. [conditional 1/5: how-to]
12. Announcement. Order: hook; the facts with numbers; what the news means from the author's role (the part they think about most); "So we're looking for ..." with the call to action pointing to "the comments"; a one-line thank-you to the people involved. No reframe block, no closing question. [conditional 1/5: announcement]
13. Mention role and company size only in how-to and announcement posts, once. [conditional 2/5]

### Close

14. Except in announcements, end the body with one question to readers about their own experience, specific to the topic ("If you've done X, how did you Y?", "What's worked for you when ...?"). It is the only question mark in the post; no rhetorical questions in the body. One short follow-up sentence may sit in the same paragraph after it. [conditional 4/5: not announcement]
15. Last line: exactly 3 hashtags in CamelCase, separated by spaces, nothing after. [observed 5/5] Usually one of them is the author's broad field tag; the other two match the topic. [tendency 4/5]

### Voice and mechanics

16. First person. "I" for the author's own decisions and views, "we/our" for the company. [observed 5/5]
17. Plain, measured, honest. Own mistakes outright. Hedge claims you cannot prove ("I think", "usually", "might"). No hype, no slogans, no motivational lines. [observed 5/5]
18. Use natural contractions (didn't, we've, I'd). [observed 5/5]
19. Numbers: digits for 10 and above, percents, and money (12 sites, 3,000, 41%). In the body, usually spell out one to nine ("three screens", "four moves", "nine people"), and always when a number starts a sentence. A stat hook may open with digits, and a small number paired with a larger one in a ratio stays a digit ("4 of the 22"). [tendency 4/5]
20. Mix sentence lengths: mostly 8 to 16 words, plus one or two longer sentences of 20 to 30 words that carry the reasoning; never longer than about 32. Average about 11 to 15 words. [range observed mean 10.5 to 15.1, longest 21 to 31]
21. Never use emojis, exclamation marks, em dashes, en dashes, or "--". [absent 0/5] Use commas, periods, colons.
22. No bold, headers, or bullet symbols. The only list format is "1. " in how-to posts. [absent 0/5]
23. No links in the post; send readers to "the comments". [absent 0/5]

## Example

(New topic, opinion type.)

```
Unpopular opinion: approval chains on small purchases cost more than the purchases they guard.

Last quarter I pulled every expense request under $200. There were 640 of them, and the median one waited 4 days for a signature that was never refused.

Two reasons I think the chains survive:

Each approver sees one request at a time. Nobody sees the 640 together, so the delay never looks like a problem worth fixing.

Removing a check feels risky in a way that adding one never does. If something goes wrong later, the person who removed it gets the blame.

My fix is a limit, not a chain. We now let anyone spend up to $200 without asking and review the totals once a month. In three months nobody has misused it.

Where does your team set the line for purchases that need sign-off?

#Operations #Finance #Leadership
```

## Unknowns

Do not act on these as rules.

- Persona details beyond role and company size (industry, name, backstory). The outputs show one operations lead at a company of about 60 people; a source skill may hold more.
- How the post type is chosen: given in the brief or picked by the skill.
- Post types not seen (event recap, hiring-only post, celebration, book takeaway).
- Banned words or phrases.
- Rules for hashtag selection beyond count and casing.
- Whether a sentence-length or reading-level limit is set explicitly.
