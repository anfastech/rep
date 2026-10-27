---
name: instagram-caption
description: Use when writing an Instagram caption for a reel, carousel or single image from a brief.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# Instagram caption

Input: brief (topic, facts, numbers, takeaway, post format, goal, any link). Output: fenced caption, optional alt-text line, fenced CAPTION READY card.

## Step 1: pick the job

- **A, reel carries the hook**: the video shows/says the hook in the first two seconds. Caption line 1 = the ask.
- **B, line one is the hook**: carousel cover, single image, single photo. Caption line 1 = the hook: 1-2 sentences, never over 125 characters, and use most of that space (usually about 75-115 characters). A common shape is the fact, then a short turn ("We tried X for a week. Only one thing survived.").
- In job A, line 1 also uses most of the visible space: the keyword, what they get, and who it is for or when it's used.

## Step 2: pick the shape (blank line between every paragraph)

**Story-to-lesson** (something happened, we changed). Trigger: failure, experiment or data story.
```
<hook: the result or number, 1-2 sentences>            (A: Comment KEYWORD and I'll send you <thing>.)
<what we did / what we found, 1-3 sentences>
<what happened, 1-2 short sentences with the numbers>
<the real cause or the change, 1-3 sentences>
<takeaway: e.g. "If you want to ..., ..." or "Before you ..., ..." (examples, not fixed)>   (A: the new practice, "Now every ...", is the last paragraph; no second ask)
<ask>                                                    (B only)
#tag #tag #tag
```

**Numbered list** (tactics, steps). Trigger: how-to or advice brief.
```
<hook: reader's situation as a question + the promise, e.g. "You have N ...">
<1-2 sentence framing of why usual advice misses>
1. <Label sentence.> <1-2 sentences.>
2. ...   (each item is its own paragraph, blank line between items)
<ask: Save this before your next ...>
#tag #tag #tag
```

**Announcement** (launch, office, hiring). Trigger: news brief.
```
<hook: the news + the forward number, 1-2 sentences>
<progress so far, 1 sentence>
<who we are + what's next, 1-2 sentences>
<ask addressed to the reader it is for (e.g. people looking for these jobs), pointing them to the bio link>
#tag #tag #tag
```

## Step 3: pick the ask (exactly one)

| Goal | Ask |
|---|---|
| Lead magnet | Comment KEYWORD and I'll send you ... (job A: line 1) |
| Reference value | Save this for/before ... |
| Opinion / debate | A direct question + "Tell me in the comments." |
| Link (jobs, product) | Point the right reader to the bio link |

## Mechanics (defaults)

No emojis, no em or en dashes (normal hyphenated words like follow-up are fine), no exclamation marks, no markdown, no links. Digits for data. Contractions fine. At most 3 sentences per paragraph. Caption about 60-160 words (observed 74-138). At most 2 contrast lines ("not X", "X. What failed was Y") per caption (cap unconfirmed). Close on a concrete ask, not an aphorism. Hashtags: exactly 3, lowercase, last line. Work in 2 different search phrases (exact strings people would search), one early (line 1 or 3), one later (often the takeaway or ask line).

## Alt text

Carousel: `Alt text (cover slide): ...`. Single image/photo: `Alt text: ...`. Reel: none.
Describe what is visible, including the key result a chart shows. If the cover lists items, name each item. One or two sentences.

## Card

```
CAPTION READY
job:        A - the reel carries the hook (<who> on camera, "<hook>" in the first two seconds)
job:        B - <carousel cover | single image | single photo>, line one is the hook
visible:    <chars of line 1> of 125 characters used before the cut
ask:        one, <short lowercase paraphrase: "save it", "comment KEYWORD", "reply to the question in comments", "<thing> via the link in bio">   (A: add " (say KEYWORD out loud in the video too)")
hashtags:   3
search:     "<phrase>" in line <n>, "<phrase>" in line <n>
first comment: none, no link   | with a link: none, the link lives in the bio, not the caption
linter:     READY, checked by hand against caption.py's rules
```
Use one job line. Line numbers count every caption line including blank lines, so paragraphs sit on lines 1, 3, 5, 7... If a phrase appears twice, write "in line 1 and line 3".

## Example (new topic)

```
Our clinic had 1 in 5 dental appointments end as a no-show. One change to the reminder text cut that in half.

We used to send a reminder the day before with the date and time. Patients read it and still forgot.

Now the reminder goes out two days ahead and asks them to reply 1 to confirm or 2 to move the slot.

No-shows went from 20% to 9% in three months.

If your patient no-shows keep climbing, change what the reminder asks for before you change the schedule.

Save this for your next front-desk meeting.

#dentalpractice #clinicmanagement #healthcare
```

Alt text: A phone screen showing an appointment reminder text with the options reply 1 to confirm or 2 to reschedule.

```
CAPTION READY
job:        B - single image, line one is the hook
visible:    109 of 125 characters used before the cut
ask:        one, save it
hashtags:   3
search:     "dental appointments" in line 1, "patient no-shows" in line 9
first comment: none, no link
linter:     READY, checked by hand against caption.py's rules
```

## Unknowns

- Is "linter: READY, checked by hand ..." the fallback wording when caption.py could not run? What does caption.py check, and what does the line say when it runs or fails?
- Are there jobs other than A and B (for example a caption-only post, or a reel where the caption carries the hook)?
- Are 3 hashtags fixed, or a setting? Is the 125-character cut the only length limit?
- Are em dashes, rule-of-three lists, closing aphorisms, "Here's the thing" bridges and engagement bait banned, or just absent? Could the no-dash habit come from the generator's own settings?
- Is there a per-brand voice file (tone, banned words, CTA keywords)?
- What happens with a link the brief wants in the caption, or a real first comment?
- How is the deliverable handed over beyond these three blocks (alternatives, notes)?
