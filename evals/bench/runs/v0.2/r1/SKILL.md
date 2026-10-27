---
name: linkedin-post-ghostwriter
description: Use when asked to draft a LinkedIn post for a named person from a brief (a story, a result, an opinion, advice, or an announcement), with no invented facts and a claims check before anyone posts.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.2
---

# LinkedIn post ghostwriter

Input: a brief naming the person, their role, the facts or story, any opinion
they hold, the sign-off scope, and optionally a voice card or past posts.
Output: one plain-text deliverable, saved as a draft, that the person edits
and posts themselves.

## Template

```
<Working title> · content/drafts/<YYYY-MM-DD>-<slug>.md
Single post · LinkedIn · <Name>'s profile (first person) · voice <provisional|from voice card>

Hook (used below):
<hook>

Alternative hooks:
1. <alt hook, different angle>
2. <alt hook, different angle>

Post:

<hook, verbatim>

<body paragraphs>

<closing action>

#<tag> #<tag> #<tag>

First comment: <none (no link in this post).|<label>: <link or slot>>

Edit note
- One argument: <the single point every paragraph serves>
- Fakes: <what was not invented and which slots stand in for it>
- Intent and CTA: <post type>; <why the close fits>
- Swap test: <passes/weak, and on what>
- Skeptic: <strongest objection and whether the post answers it>
- Readability: <where the key facts land against the ~140 character cut; paragraph shape; ending>
- AI-tell check: removed <N> <tell> (<quote>), ... No banned words. No dashes. <Any tell kept on purpose, and why.>
- Voice: <status (provisional or from a voice card), reason, offer>

Claims and facts: <Working title>   (sign-off: <scope from the brief>)
- Kept: <each fact used, and whose account it is>
- Softened: <wording made less specific, and why, or none.>
- Cut: <what was removed, and how to restore it, or none.>
- Sourced: <public sources opened, or none with the reason>
- Disclaimers added: <list, or none.>
- Person yes needed: <Name>.

Open gaps
- PERSON YES NEEDED (<Name>)
- <each slot from the post, in order, short form>

Nothing is published. You edit and post. If you want the social pieces in a two-week posting calendar, ask for it next.
```

## Post shapes (pick by the brief's intent)

| Intent | Trigger in brief | Body (about 3 slots) | Close |
|---|---|---|---|
| Lesson | Something went wrong or right, plus a takeaway | What happened, the person's decision, the cost, the lesson, how it works, what changes next | "If you're <in the same spot>, <one step>." |
| Data insight | A measured finding | The number restated plainly, what it pointed at, what was done, the result, what it taught | "If your <problem>, try this <before X>. <Concrete steps>." |
| Contrarian | The person holds a view against common practice | Result first, the view stated as theirs, why, what happened, concede the exception with their own number | "If <reader situation>, try the same test. <How>." |
| How-to list | Several parallel moves or steps | One-line setup, then a numbered list: `1. <Move as a short imperative.>` on its own line, 1 to 2 sentences under it; one line on why they work | "Save this for <next occasion>." |
| Announcement | News about the company, often with hiring | What is new and the key numbers, why it matters, slots for the why and the team, the person's own role in it | The ask, with "the <link> is in the first comment" |

## Rules

1. Output every block of the Template in that order, with these labels
   verbatim. [observed 5/5]
2. Header line 2 states format, platform, whose profile and person, and voice
   status. If the post speaks for the company from a person's profile, write
   that the person speaks for the company, in the brackets after "first person", and use "we" for the company,
   "I" only for the person's own role. [observed 5/5; conditional 1/5:
   company announcement]
3. The hook is 2 to 3 short sentences that land the key fact or numbers
   within roughly 140 characters, ahead of LinkedIn's "see more" cut. It
   opens the post verbatim. [range observed 89 to 141 chars, 17 to 29 words, N=5]
4. Give exactly 2 alternative hooks, each a different angle (number first,
   blunt admission, the reader's problem, the claim), each about 13 to 25
   words, usually the second shorter. [range observed 13 to 22 words, N=10] If an alternative adds
   anything not in the brief, flag it in Claims and Open gaps. [observed 5/5]
5. Never invent facts, events, numbers, feelings or quotes. Where the post
   needs a missing story or specific, leave a typed slot inline, written to
   the editor with the person named in the third person and a hint if
   useful: `[STORY NEEDED: <what, e.g. ...>]` for an anecdote or the
   person's reason ("why Lisbon, in Maya's words"), `[NAME: <specific
   name, number or rule>]` for a missing specific, `[PROOF NEEDED: <link or
   confirmation>]` for a URL or a claim to verify. A slot can be its own
   paragraph or end a sentence. Use slots for the few gaps that matter most:
   about 3 in a post built on a full brief, more only when the brief is thin
   (an announcement with no reasons given). [observed 5/5; range 3 to 6
   slots, 3 in 4/5]
6. Plain reasoning that follows from the brief's own facts may be written
   out without a slot (how a pilot contains damage, why a habit persists). If it
   reads as a stance the person did not state, keep it but flag it in Fakes
   for their yes. [observed 5/5; flagged 2/5]
7. One argument per post. Every paragraph serves it. [observed 5/5]
8. Body paragraphs are 1 to 3 sentences. The post, from hook to the close
   and counting slots, is about 150 to 200 words before hashtags.
   [range observed 163 to 180 words, 7 to 8 paragraphs, N=5]
9. Draft the post once, then edit it against rules 15 and 16. The Edit note
   and Claims report what that edit changed, quoting removed lines from the
   first draft. If a check found nothing, say "none". [observed 5/5:
   every output reports removals]
10. End on an action the reader can take, matched to the intent (see Post
    shapes). Never end on a recap or a moral. [observed 5/5]
11. Use a numbered list only for parallel items. [conditional 1/5: how-to]
12. Hashtags: one line after the body, 2 to 3 tags, lowercase except proper
    nouns, one of them the person's field. [range observed 2 to 3, N=5]
13. Links never go in the body. With a link or an ask that needs one (open
    roles, sign-up), the first comment holds it (`First comment: <label>:
    <URL or [PROOF NEEDED: ...]>`) and the post says it is there. Without
    one, write `First comment: none (no link in this post).`
    [conditional 1/5: hiring ask]
14. Edit note bullets, terse, about 15 to 30 words each (Fakes and AI-tell
    check may run to 50), Edit note about 160 to 220 words in all, in this order: One argument,
    Fakes, Intent and CTA, Swap test, Skeptic, Readability, AI-tell check,
    Voice. One argument, Fakes, Intent and CTA, AI-tell check and Voice are
    always there. Swap test (does the post only work for this person: name
    the specifics that make it theirs, or "weak" and why) is skipped when
    the post is news with no claim to own. Skeptic (the strongest objection
    and whether the post answers it) appears when the post argues a lesson
    or opinion. Readability is usually there. [observed 5/5; Swap 4/5,
    Skeptic 2/5, Readability 4/5; range 9 to 57 words per bullet, N=34]
15. AI-tell check: remove and count these from the first draft, quoting each
    removed line: colon reveals ("The result? 4.", "The lesson is plain:"),
    rhetorical-question openers, "not X, it's Y" (keep at most 1), reveal
    bridges ("Here's the kicker"), invented feelings or attitudes, hype
    ("thrilled to announce", "exciting new chapter", "journey"), world facts
    lacking a source checked during this run, opinions the person did not supply
    (cut them; rule 6 reasoning drawn from the brief stays, flagged).
    Format: "removed 1 <tell> (<quote>), 1 <tell> (<quote>)." Then "No
    banned words. No dashes." [observed 5/5]
16. Claims and facts: six one-line rows, Kept, Softened, Cut, Sourced,
    Disclaimers added, Person yes needed, in that order, each ending with a
    period, "none." when empty. Kept names whose account the facts are.
    Cut says how to restore what was cut. A world fact needs a dated public
    source opened this run, or it is cut. Facts the brief says are not
    public stay out and are noted under Softened. Person yes needed is just
    the name. [observed 5/5]
17. Open gaps: `- PERSON YES NEEDED (<Name>)` first, then one line per slot
    in post order, in short form (the slot's label and subject, no "e.g."
    hint), then any `[PROOF NEEDED: ...]` for an alt hook or first comment.
    [observed 5/5]
18. Voice: with no voice card or past posts, mark the voice "provisional",
    write plainly, first person, using the brief's own words, and offer:
    "Offer: paste 5 to 10 of <Name>'s LinkedIn posts and I'll build <her or
    his> voice card." With a voice card, follow it and say so. [observed 5/5]
19. End with the fixed closing line from the Template. Never publish.
    [observed 5/5]

## Defaults

1. Plain, concrete sentences, mean about 12 to 17 words; contractions are
   fine. [range observed, N=5]
2. No emojis, no exclamation marks, no questions in the body, no em or en
   dashes or double hyphens (hyphenated words are fine).
   [absent 0/5]
3. The close usually starts "If you ..." [tendency 4/5]
4. The person's own numbers are repeated or restated once in the body
   ("two out of every five" for 41%). [tendency 3/5]

## Example (new topic; a fragment)

```
Hook (used below):
Our clinic moved every appointment reminder from phone calls to texts. No-shows fell from 1 in 8 to 1 in 20.
```

## Unknowns

- What is on the banned word list?
- Other formats exist ("Single post", "social pieces", "two-week posting
  calendar"). What are their skeletons?
- Is there a voice card format, and which slots (hooks, CTAs, banned words,
  hashtags) does it control?
- Are 2 alternative hooks fixed or configurable?
- Are length tiers available (short, long)?
- What are the sign-off scopes, and how does each change Claims and facts?
- Is the dash ban from this skill or from the generator's settings?
- How do sign-off scopes (a scope taken from the brief, a scope limited to product
  facts) change what may be said?
- Is the first draft (whose tells get "removed") kept anywhere, or only
  summarised in the Edit note?
- Is "content/drafts/" a fixed folder, and is the file actually written?

## Untested changes

Found in the held-out test after the rules were frozen. Not replayed.

1. Rule 3: a hook can also be 1 sentence, and can run to about 150
   characters. [held-out 06: 1 sentence; 07: 151 chars]
2. Post shapes: add a Reflection row (a personal change, e.g. returning
   from leave): what changed, one slot per change, why, then close on a
   genuine question inviting readers' own experience. [held-out 06]
3. Rule 14: Swap test and Skeptic are optional; skip both on a personal
   reflection. Six bullets is common. [held-out 6 and 6 bullets; replay 8]
4. At most 1 rule-of-three list per post, and vary sentence shapes to avoid
   one. If an alt hook uses a triplet or a "not X, it's Y", note in the
   AI-tell check that the post keeps no other one. [held-out 06, 07]
5. When the post credits or would name another person, add a second
   `PERSON YES NEEDED (<that person>)` line in Open gaps and name them under
   Person yes needed. [held-out 07]

(Wording only, no rule changes, was also edited after the held-out test to
pass the leak check.)
