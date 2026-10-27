# Reverse-engineering report: target

Input: 7 plain-text LinkedIn-style posts (5 train, 2 held out, user's split). Route: text (built).
Final skill: `SKILL.md` (= `drafts/final.md`). Ledger: `ledger.md`. Briefs: `briefs.md`.

## Ledger summary
See `ledger.md`. Strongest findings:
- **observed 7/7**: every output is a post followed by a separate 2-sentence note to the requester ("I <past verb> <craft choice> ..." + an offer to adjust). This is the signature of the skill.
- **observed**: plain factual opener, calm first-person voice, full sentences, digits for stats, explanation of mechanism.
- **absent 0/7**: questions, exclamation marks, emojis, hashtags, markdown, em/en dashes, hype phrases.
- **conditional**: result held to paragraph 2 for narrative briefs (3/3); numbered list only for tips (1/7); changes-as-paragraphs for reflections (1/7); CTA only for hiring (1/7); note mentions a detail missing from the brief (2/7).
- **tendency**: limit-the-claim line (3/7), closing line tied to a concrete fact (4/5 train).
- **range**: 163 to 227 words, 5 to 8 paragraphs, first paragraph 19 to 32 words, mean sentence 9.9 to 14.0 words, max 21 to 31.

## Rounds (train replays, blind subagent given only draft + briefs)
| Round | Flags outside range | Form diffs found | Fix |
|---|---|---|---|
| v1 | 7 | choppy one-liner paragraphs, aphoristic closers, filler paragraph (05), hedge line forced into 01 | rules on full 2-4 sentence paragraphs, no filler, closing tied to facts, hedge = sometimes |
| v2 | 5 | "The short version:" copied from my example into 3/5; posts too short (118-174 words); 02 led with the stat | rewrote example, vary closings, hold result to para 2, add mechanism paragraph, aim ~200 words |
| v3 | 8 (mostly marginal: digits, max sentence 28, 05 at 122 words) | close on structure; 05 lacked a concrete observation; one sentence started with a digit | v4: announcement gets one concrete observation; no digit at sentence start |
Stopped after round 3 per method.

## Held-out test (v4, briefs inferred after opening heldout/)
Per check:
- Final note to requester, correct shape: **pass** 2/2.
- Note cites missing brief detail (07 analyst name): **pass**.
- Plain-fact opener, no hook trick: **pass** 2/2.
- Mechanics (no ?, !, emoji, hashtag, dash, markdown): **pass** 2/2.
- Reflection written as one paragraph per change, not a list (06): **pass**.
- Paragraph count: **fail** 2/2 — replay had 7 non-blank paragraphs vs 6, because it added a limit-the-claim line the originals lacked. Fixed in final (rule 6 narrowed).
- Word count: **marginal** — 214 both vs 191-203 originals (within train range).
- First-line length: **marginal** — 30-38 vs 27-28.
- Number style: **partial** — 06 replay wrote "6 months", original "six months". Rule loosened.
- Max sentence length: originals 27-31 exceeded the train range; range widened.
Note: the final SKILL.md includes edits made after seeing held-out results, so the held-out set is no longer a clean test of the final version; it was clean for v4.

## Negative control
Generic prompt "Write a LinkedIn post about ..." on brief 06 (`replay/control/06.txt`): 340 words, bold-style numbered headers, a question, 5 hashtags, engagement CTA, no note to requester; 13 features outside held-out range vs 9 (mostly marginal) for the skill replay. Clearly worse; the comparison discriminates.

## Leak check
`style_stats.py leak SKILL.md train/`: 0 shared 6-word runs. Same against heldout/: 0. Example is a new topic (bakery 4-day week).

## Unknowns
- Banned word list, persona backstory, platform name.
- Whether the note to requester is always on or a caller option.
- Behavior for briefs unlike these (bad news, very long briefs, multi-author, non-work topics).
- Any hard word limit.
- Whether the "result in paragraph 2" pattern is a rule or a habit (3/3 narrative briefs, small N).
