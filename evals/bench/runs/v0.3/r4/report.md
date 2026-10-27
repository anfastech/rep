# Report: target

Source: 7 outputs from one unknown skill (5 train: 01-05, 2 held out: 06-07, the user's split). The outputs are short first-person LinkedIn-style posts with a comment-keyword lead magnet, a "PS - " line and a hook-formula tracking footer. Final skill: `SKILL.md`, exported from the frozen draft `drafts/final.md` (= v3). The only change after freezing was the leak-check edit described below.

## Rules and evidence (from train, N=5)

| Rule | Class | Evidence |
|---|---|---|
| Line 1 is an "I ..." first-person claim | observed | 5/5 train; **held-out 1/2** (07 opens "A junior analyst on my team ...") |
| "Here's ...:" bridge right after the hook | observed | 5/5 train, 2/2 held out |
| Bridge wording by type (what happened / what we did / why I did it / the N-step playbook I use / where we are) | conditional | one wording per type in train; held out uses 2 new wordings ("what changed", "what they built") |
| Body menu: story lines / "→ " arrow list / "1/" playbook steps | conditional (menu) | 01,03 story; 02,05 arrows; 04 playbook; held out 06 arrows, 07 story |
| Arrow lines consecutive with no blank lines | observed | 2/2 train, 1/1 held out |
| Arrow lines have no closing period | observed (2/2) | **held out 06 breaks it** (two-sentence items with periods) |
| Two-line reframe before the resource line | observed | 5/5 train, 2/2 held out |
| Resource line + `Comment "<KEYWORD>" and I'll send you the link.` | observed, fixed string | 7/7 |
| KEYWORD = one ALL-CAPS unrelated noun | observed | 7/7 |
| "PS - " line, 2 sentences, to the reader | observed | 7/7 |
| `---` + `Hook formula used: <Name> — for A/B tracking. Strip before publishing.` | observed, fixed string | 7/7; 7 distinct formula names, all Title Case and joined with "/" or "+" |
| Second hook line | tendency | 2/5 train, 0/2 held out |
| "Most ..." setup line | tendency | 3/5 train, 0/2 held out |
| "No X. No Y. Just Z." | capped, max 1 | 2/5 train, 1/2 held out |
| 135 to 170 words, 16 to 20 non-blank lines | range (widened) | train 135-164 / 17-19; held out 139-144 / 15-16 |
| No ? ! emoji hashtag bold, no body em dash; contractions; digits | default/absent | 0/7 for each absent feature |

## Held-out result, per check (final draft replayed on the inferred briefs 06, 07)

| Check | Originals obey the skill? | Replay matches original? |
|---|---|---|
| Hook starts with "I" | 1/2 (07 fails) | 1/2 (replay 07 forced "I watched ...") |
| Second hook line | n/a (none in either) | 1/2 (replay 06 added one) |
| "Here's ...:" bridge present | 2/2 | 2/2 |
| Bridge wording from the skill's list | 0/2 | 1/2 (replay 06 chose "what changed" on its own) |
| Body shape | 2/2 | 2/2 |
| Arrow format (consecutive, no periods) | 0/1 (periods used) | 0/1 |
| Reframe pair before resource | 2/2 | 2/2 |
| "No X. No Y. Just Z." count | orig 1/2 | 0/2 match (replay used it in both) |
| Resource + CTA fixed string | 2/2 | 2/2 |
| Keyword style | 2/2 | 2/2 |
| PS - line, 2 sentences | 2/2 | 2/2 |
| Footer verbatim + formula-name style | 2/2 | 2/2 |
| Words (orig 139-144) | inside skill range 2/2 | replay 164-169, longer, 0/2 within ±10% of original |
| Non-blank lines (orig 15-16) | 1/2 inside 16-20 | replay 17-18, 0/2 |
| Absent mechanics | 2/2 | 2/2 |

`compare heldout/ replay/heldout/` flagged 12 features. With N=2 the original range is very narrow, so most flags are small. The real ones are length (+25 words) and line count (+2).

## Negative control

A subagent got the brief for 03 and a plain "write a LinkedIn post offering the resource" prompt, with no skill (`replay/control/03.txt`). It came out at 246 words with 3 questions, multi-sentence paragraphs, no "Here's ...:" bridge, no PS, no footer, a different CTA wording and a closing engagement question. `compare train/ replay/control/` flagged words, questions, sentence length and dashes. The skill replays match the originals far more closely, so the comparison discriminates.

## Leak check

The first run of `leak SKILL.md train/` found 27 shared 6-word runs. Two kinds were not fixed strings that repeat in every original:
- The example's footer reused a train formula name. It was replaced with an invented name.
- One formula name from the library ("DON'T Do ..." in 03) appears in only one output. It was replaced with a description.

The final count is 4 distinct runs. All come from the two lines present in all 7 outputs: the CTA string and the footer string. These are expected.

## Untested changes (suggested by the held-out set; NOT applied to SKILL.md)

1. The hook may open with someone on the author's team instead of "I" ("A junior analyst on my team ..."). Change rule 1 to "first-person point of view; usually opens with I".
2. The bridge wording is open: "Here's what <changed / they built / ...>:". Treat the listed wordings as examples, not a closed set.
3. Arrow items may be two full sentences with periods ("I delegate more. The team was ready ...").
4. The length target should go lower: about 130 to 165 words and 15 to 19 non-blank lines. Replays ran long on held-out and on 2 train briefs.
5. Use "No X. No Y. Just Z." in about 1 post in 3, not "up to half".
6. Make the formula library open-ended. Both held-out names were new ("Authority Proof + Bold Claim", "Results-First + Permission Removal"), and "Results-First" recurs as a prefix.

## Unknowns (questions for the user)

- Must the hook start with "I", or is any first-person-perspective opener allowed?
- What is the full hook-formula library, and how is a formula picked (goal, post type, A/B rotation)?
- Is there a per-user voice file that sets tone, CTA wording, keyword style or banned words?
- Is the resource/CTA block ever skipped, for example when there is no resource?
- Are there length tiers? All 7 outputs sit in one band.
- Are em dashes, questions, emojis and hashtags banned, or only absent? They may come from the generator's own settings.
- What are the rules for links, images, tagging people, threads, and other content types the sample does not cover?
- How is the deliverable handed over: one draft, or several formula variants for the A/B test?
- Is the keyword random, or taken from a list? Two replays reproduced original keywords by chance (PRETZEL, TEAPOT), so the space of "obvious" nouns is small.
- The AI-tell devices (contrast reveals, the "No X. No Y. Just Z." triple, the "Here's" bridge, aphoristic closers, the comment-bait CTA) all appear in the outputs, so the source does not ban them. Is anything else banned?

---

# Appendix A: Ledger

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| F1 | Line 1 is a first-person claim starting with "I" (action or result, usually with a number) | 5/5 | observed | Open with an "I ..." sentence stating what you did or found |
| F2 | Hook length (line 1) | 8 to 16 words, N=5 | range | About 8 to 18 words |
| F3 | Optional 1-line hook follow-up before the bridge (the reveal/second fact) | 2/5 (03, 05) | tendency | Optionally a short second hook line (a surprising number or the key detail) |
| F4 | Bridge line "Here's <what happened / what we did / why I did it / the N-step playbook I use / where we are>:" ending in colon | 5/5 | observed | Always a "Here's ...:" bridge line right after the hook |
| F5 | Bridge wording matches type: story "what happened", process "what we did", experiment "why I did it", list "the N-step playbook I use", announcement "where we are" | 5/5 one per type | conditional | Pick bridge wording by brief type |
| F6 | Context/setup 1-2 lines after bridge; "Most ..." common-belief opener | 3/5 (02,03,04) | tendency | Usually set up with what most people think/do |
| F7 | Body shape: story = short single-sentence lines chronological (01,03); results/process/announcement = "→ " arrow list 4-6 items (02,05); how-to = numbered "1/" steps, each a bold-less title line + 1-2 sentence explanation line (04) | 5/5 split by type | conditional (menu) | Template menu by brief type |
| F8 | Arrow list length | 4 to 6 items, N=2 | range | About 3 to 7 arrows |
| F9 | Numbered steps | 4 steps, N=1; count announced in bridge | range | 3 to 5 steps; count in bridge |
| F10 | Lesson/reframe: two short lines, contrast "X isn't/wasn't the problem. Y is/was." or "X is just ... The Y is what ..." | 5/5 (some form) | observed | One reframe/lesson pair before the CTA |
| F11 | Aphoristic closer / directive line before CTA ("One site down is a bad day...", "Don't trim... Cancel them all...") | 2/5 (01, 03) | tendency | Optional |
| F12 | "No X. No Y. Just Z." triple | 2/5 (02 inside list, 04), max 1 | capped | At most 1 per post |
| F13 | Resource line: "I <wrote up / put ... into / turned this into> <the resource>." | 5/5 | observed | Always offer a resource tied to the post |
| F14 | CTA fixed string: Comment "<WORD>" and I'll send you the link. | 5/5 | observed (fixed string) | Verbatim |
| F15 | Keyword is one ALL-CAPS common noun unrelated to topic (PRETZEL, OTTER, TEAPOT, MANGO, CACTUS) | 5/5 | observed | Random unrelated concrete noun, all caps, in double quotes |
| F16 | "PS - " line (hyphen with spaces), 2 sentences, speaks to reader (you) with a nudge or reframe; 05 splits readers into two groups | 5/5 | observed | Always end post with "PS - ..." 2 sentences |
| F17 | Footer: "---" then "Hook formula used: <Formula name> — for A/B tracking. Strip before publishing." | 5/5 | observed (fixed string) | Verbatim, formula name from a library |
| F18 | Formula names: "Confession / Gap Reveal", "Results-First / Before-After Transformation", "DON'T Do X — Do Y Instead", "Effort Proof + Free Resource", "Breaking News + Speed Flex" — Title Case, joined with " / " or " + " | 5 distinct names | unknown (library) | Name the formula; full library unknown |
| F19 | One sentence or two per line; blank line between every line | 5/5 | observed (format) | Every line its own paragraph |
| F20 | Total words | 135 to 164 incl. footer, N=5 | range | About 120 to 190 words |
| F21 | Nonblank lines | 17 to 19, N=5 | range | About 15 to 22 |
| F22 | Sentence length mean 6 to 10 words | N=5 | range | Short sentences |
| F23 | Questions, exclamations, emojis, hashtags | 0/5 each | absent | Default none |
| F24 | Contractions | 4 to 7 per post | tendency | Use contractions |
| F25 | Em dashes in post body | 0/5 (only in footer) | absent | Default none in body (P11: may be generator setting) |
| F26 | Markdown bold/headers | 0/5 | absent | Plain text |
| F27 | Voice: first person I/we, past tense for story, present for lesson; plain words, grade-school level | 5/5 | default | |
| F28 | Numbers as digits (12, 3,000, 41%, 22, 4/) | 5/5 | default | Digits for numbers |
| F29 | "So I ..." decision line in story | 2/5 (01, 03 — both story/experiment) | conditional | In stories, a "So I ..." pivot line |
| F30 | Owning-the-mistake line ("my call") | 1/5, failure brief | conditional (weak) | If failure, own it |

## Pattern walk (references/patterns.md)
- P1 AI-tells: contrast reveal 5/5 (F10), triple "No X. No Y. Just Z." 2/5, reveal bridge "Here's ...:" 5/5, aphorism 2/5, engagement bait (comment keyword) 5/5. The source does NOT ban these; they are part of its form. Commenting on post itself: 0/5.
- P2 caps: triple max 1; arrow list max 1 per post; contrast pairs 1-3 per post (uncapped evidence). Sentences per line max 2 (except PS, 2).
- P3 menu: yes — 3 body shapes (story, arrow, numbered) plus hook-formula library.
- P4 voice file: unknown — ask.
- P5 platform units: LinkedIn-like; "see more" cut likely around line 2-3 (bridge sits at line 2-3). Characters unmeasured as rule. Unknown.
- P6 optional sections: resource/CTA might be optional if no resource exists; 5/5 present → "usually"? Fixed string 5/5 so kept observed, with question.
- P7 length tiers: all in one band; unknown.
- P8 content-triggered: no links, code, tables seen. Unknown.
- P9 packaging: footer meta-line is packaging ("Strip before publishing") — captured. Other packaging unknown.
- P10 defaults: no hashtags/emojis are defaults.
- P11 generator: body em-dash absence and "PS -" hyphen may come from settings.
- P12 voice protection: unknown.

# Appendix B: History

Checks (per replay set vs train, 5 files). "k/5" = files matching the original on that check.

## Round 1: A1 (strict), B1 (menu), C1 (loose)

| Check | A1 | B1 | C1 |
|---|---|---|---|
| C1 Hook "I ..." line 1 | 5/5 | 5/5 | 5/5 |
| C2 Second hook line where original has one (03,05) / none elsewhere | 0/5 match (never uses it) | 3/5 (adds it to 01,02 too) | 2/5 |
| C3 "Here's ...:" bridge wording by type | 5/5 | 5/5 | 3/5 ("Here's how:", missing type wording) |
| C4 "Most ..." setup position (after bridge) | 0/3 (04 put it after the list) | 3/3 | 3/3 |
| C5 Body shape by type (story/arrow/numbered) | 5/5 | 5/5 | 2/5 (03 numbered, 02 prose, 01 mixed arrows) |
| C6 Arrow lines consecutive, no blank lines, no end period | 0/2 (blank lines, periods) | 0/2 | 0/2 |
| C7 Numbered step = title line, blank, explanation line | 1/1 | 1/1 | 0/1 (inline) |
| C8 Two-line reframe lesson before resource | 4/5 | 5/5 | 4/5 |
| C9 "No X. No Y. Just Z." count (orig 2/5, max 1) | 1/5 partial (02, no "Just") | 2/5, max 1 | 0/5 |
| C10 Resource line + exact CTA string | 5/5 | 5/5 | 5/5 |
| C11 Keyword ALL-CAPS unrelated noun | 5/5 | 5/5 | 5/5 |
| C12 "PS - " 2 sentences | 5/5 | 5/5 | 5/5 |
| C13 Blank line then "---" then footer verbatim | 5/5 | 5/5 | 0/5 (no blank before ---) |
| C14 Formula name style (Title Case, two ideas joined by " / " or " + ") | 0/5 (single names) | 5/5 | 3/5 |
| C15 Words in 135-164 (stats) | 3/5 (114-158) | 1/5 (163-185) | 2/5 |
| C16 Nonblank lines 17-19 | 1/5 | 3/5 | 4/5 |
| C17 No ?, !, emoji, hashtag, body em dash | 5/5 | 5/5 | 5/5 |
| C18 PS tone: hard truth / reframe to reader, not a how-to tip | 2/5 | 3/5 | 3/5 |

Winners: B1 on structure (C2-C9, C14); A1 on length (C15); C1 on line count (C16). None fixed C6.

Rule causes:
- C6: no draft said arrow lines sit together with no blank lines and no closing period.
- C2: B1 makes the second hook line sound like a default; originals use it only when the hook needs a reveal (03 result, 05 the place).
- C15: B1 agent counted words without the footer; the 135-164 range includes the footer. Need a total-word target that includes everything, and fewer body lines (B1 story bodies ran 10-12 lines vs 6-10).
- C18: PS in originals is a blunt observation about the reader or a two-sided split, not instructions.

## Round 2: v2 (B1 structure + A1 length target + fixes for C6, C2, C15, C18)

| Check | v2 |
|---|---|
| C1 Hook "I ..." | 5/5 |
| C2 Second hook line matches originals (03, 05 have one) | 3/5 (never used; 03 and 05 miss it) |
| C3 Bridge wording by type | 5/5 |
| C4 "Most ..." setup after bridge | 3/3 (02, 03 inside context, 04) |
| C5 Body shape by type | 5/5 |
| C6 Arrow lines consecutive, no periods | 2/2 (fixed) |
| C7 Numbered step layout | 1/1 |
| C8 Reframe before resource | 5/5, but "X wasn't the problem. Y was." form in 4/5 vs 2/5 in originals |
| C9 "No X. No Y. Just Z." | 1/5, max 1 (orig 2/5) |
| C10 Resource + CTA string | 5/5 |
| C11 Keyword | 5/5 |
| C12 PS 2 sentences | 5/5 |
| C13 Footer verbatim with blank line before --- | 5/5 |
| C14 Formula name style | 5/5 |
| C15 Words 135-164 | 4/5 (168) |
| C16 Nonblank lines 17-19 | 5/5 |
| C17 No ?/!/emoji/hashtag/body em dash | 5/5 |
| C18 PS tone | 4/5 (05 is advice) |

Fixes for v3: C2 (second hook line too restricted: "Only if" reads as rare), C8 (one reframe form dominates; originals vary it).

## Round 3: v3 (v2 + varied reframe forms, second hook line as ~2/5 tendency)

| Check | v3 |
|---|---|
| C1 Hook | 5/5 |
| C2 Second hook line | used 2/5 (02, 05) vs originals 2/5 (03, 05); 3/5 files match exactly. No brief property predicts it; stays a tendency |
| C3 Bridge | 5/5 |
| C4 "Most" setup | 3/3 |
| C5 Body shape | 5/5 |
| C6 Arrow format | 2/2 |
| C7 Numbered layout | 1/1 |
| C8 Reframe before resource; form mix | 5/5; "wasn't the problem" form 2/5 (matches originals 2/5) |
| C9 "No X. No Y. Just Z." | 2/5, max 1 (matches) |
| C10 Resource + CTA | 5/5 |
| C11 Keyword | 5/5 |
| C12 PS 2 sentences | 5/5 |
| C13 Footer | 5/5 |
| C14 Formula name | 5/5 |
| C15 Words 135-164 | 4/5 (170) |
| C16 Nonblank 17-19 | 5/5 |
| C17 Absent mechanics | 5/5 |
| C18 PS tone | 4/5 (05 advice again) |

Round 3 is the last allowed round. v3 frozen as final candidate. Remaining: C15 slight overrun (default range already loose), C18 on announcement briefs.
