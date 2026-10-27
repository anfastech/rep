# Ledger (train N=5)

## Wrapper / packaging
| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Line 1 `**Saved to \`~/captions/YYYY-MM-DD-<slug>.md\`**` (date = run date, slug = 3-5 kebab topic words) | 5/5 | observed | Save the caption to ~/captions/<date>-<slug>.md and open with the bold "Saved to" line |
| Field order: Platform, Shape, First line pick, code block, Runner-up first lines, Comment keyword, Next action | 5/5 | observed | Fixed skeleton |
| `**Platform:** LinkedIn` | 5/5 (all LinkedIn briefs) | observed (value is brief?) | Name the platform; other platforms unobserved |
| `**Shape:**` = shape name + 1-2 sentences why this brief fits it | 5/5 | observed | Name the shape, justify from the brief's facts |
| `**First line pick:**` = 1-2 sentences on why the first line stops the scroll | 5/5 | observed | Justify the hook |
| Caption inside a bare ``` code block | 5/5 | observed | Paste-ready caption in a code block |
| `**Runner-up first lines:**` with exactly 2 quoted bullet alternatives | 5/5 | observed | Two alternative hooks, quoted, as bullets |
| Runner-ups use different angles (number-led / lesson-led / tactic-led) | 5/5 | tendency | Make the two runner-ups differ from the pick and each other |
| `**Comment keyword:** none (no link)` | 5/5, all briefs had no link | conditional (only no-link branch seen) | If no link: "none (no link)". With a link: unknown (likely a keyword to comment to get the link) |
| `**Next action:** Post it, and reply to every comment within the first hour.` | 5/5 | observed fixed string | Verbatim |
| Shape line mentions ranking ("highest-trust shape"; "no mistake or measured contrast to build on") | 2/5 explicit | observed implication | Shapes are tried in priority order: mistake > before/after > show the thing |

## Shape menu
| Shape | Seen | Trigger (brief property) | Skeleton |
|---|---|---|---|
| The lesson from a mistake | 1/5 (01) | brief is a failure at scale with a clear "what I'd do now" | hook = admission + damage; damage lines; "What I believed:" / "What actually happened:" / "What I'd do now:" labeled lines; short follow-on steps; question |
| Before and after | 2/5 (02, 03) | real measured contrast (number before / after) | hook = the number contrast; how found / what done; result; one interpretation line; question |
| Show the thing | 2/5 (04, 05) | no mistake, no measured contrast: playbook or announcement | hook states the thing plainly (or flips an assumption); the thing itself (list items, or facts); question |
| Other shapes | 0/5 | unknown | Unknowns |

## Caption body
| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Every sentence-group its own line, blank line between every line | 5/5 | observed | One line per paragraph, blank line between |
| Body lines | 5 to 9, N=5 | range | about 5 to 11 lines |
| Body words | 58 to 92, N=5 | range | about 50 to 110 words |
| Body chars | 302 to 485 | range | under ~550 chars (unconfirmed) |
| First line words | 12 to 16, N=5 | range | about 10 to 18 words |
| First line has a concrete number or plain fact | 5/5 (number in 01,02,03; fact in 04,05; 01 also admission) | tendency/observed | Lead with the most concrete fact or number |
| First line standalone (no context needed) | 5/5 | observed | Hook must make sense alone |
| Last line is a question to readers | 5/5 | observed | End with one specific question tied to the post |
| Closing question is specific (not "thoughts?") | 5/5 | observed | |
| Sentences per line | 1 to 3, mostly 1 | capped | At most 3 short sentences per line |
| Voice: first person, operator; I (01,03,04) or we (02,05) | 5/5 first-person | observed | First person; I for personal decisions, we for team results |
| Plain conversational, contractions | 2 to 5 per caption | default | Use contractions |
| Digits for numbers (3,000; 41%; 22) | 5/5 where numbers | default | Numerals, not words |
| Emojis | 0/5 | absent | Default none |
| Hashtags | 0/5 | absent | Default none (LinkedIn usually has some, so moderately strong) |
| Exclamation marks | 0/5 | absent | Default none |
| Em/en dashes in caption | 0/5 | absent (maybe P11) | Default none |
| Markdown in caption | 0/5 | absent | Plain text |
| Contrast devices ("not X", "didn't ... It ...") | 0 to 2 per caption | capped | At most 2 |
| Triples | 0 to 1 | capped | At most 1 |
| Interpretation / lesson line just before question | 3/5 (02, 03; 01 steps) | tendency | Usually one plain lesson line before the question |
| List intro "Here's how I ...:" then items one per line, imperative, 1-2 sentences | 1/5 (04, list brief) | conditional | If the thing is a playbook |
| Labeled lines "What I believed: / What actually happened: / What I'd do now:" | 1/5 (01, mistake) | conditional | Mistake shape |
| Opinion stated as "I think ..." | 1/5 (03) | tendency | |
| Announcement ends with a referral ask question | 1/5 (05) | conditional | If announcement with hiring |
| Links/URLs in caption | 0/5 | absent | Unknown: links go where? (Comment keyword hints at comment-gated link) |

## Unknowns (from pattern walk)
- P1: "Here's the thing" bridges, engagement bait, self-referential lines: 0/5. Likely banned? Contrast not banned (used up to 2).
- P4: voice file? P5: is there a char limit or "see more" target? P7: length tiers? P8: links -> comment keyword format? P11: dash absence from generator? P12: voice protection? Other platforms? Other shapes?
