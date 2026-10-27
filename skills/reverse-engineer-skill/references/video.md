# Video outputs

A video is three tracks: the script (narration), the picture (shots, motion, overlays)
and the sound. Turn each into evidence you can read, then use the same ledger as for text.

## Extract

Run `bash scripts/video_extract.sh VIDEO OUTDIR` (path relative to this skill) for each video.
It writes:

| File | What it holds |
|---|---|
| `meta.txt` | duration, size, fps, codecs |
| `scenes.txt` | hard-cut times (scene score above 0.25) |
| `sheet.jpg` | contact sheet, one frame every 3 s, timestamped |
| `transcript.txt` | narration with segment times (needs `whisper`) |
| `transcript.json` | word timings, for caption sync |
| `script.txt` | narration as plain text, one sentence per line |

Open `sheet.jpg` and read it. Then grab full frames at moments the sheet cannot show:
`ffmpeg -ss T -i VIDEO -frames:v 1 OUT.jpg` (caption detail, labels, small print).

Put each `script.txt` in `train/` or `heldout/` as a text output, so
`style_stats.py profile` measures the narration like any post.

## What is brief (negate)

- The subject and its facts: the device, the numbers, the named example.
- Which objects appear on screen (a finger, a phone, a glove).
- Names in UI mock-ups, one-off jokes, the specific everyday scenario.

## What is form (measure)

| Track | Axis | Look for |
|---|---|---|
| Format | Frame | size, aspect, fps, duration range |
| Script | Beats | role of each block with its time range (hook, question, flip, scenario, mechanism, payoff, CTA) |
| Script | Pacing | words per minute, sentence length, questions, person (you, I) |
| Script | Hook and close | hook type, CTA wording, callback to the opening scenario |
| Picture | Style | render style (3D macro, flat 2D, stock, screen capture), palette, background |
| Picture | Motion | hard cuts per minute versus continuous camera moves, push-ins, tilts |
| Picture | Recurring visual | a diagram or set that returns across the video |
| Picture | Captions | position, words on screen, line count, colour of spoken versus unspoken words, keyword highlight |
| Picture | Overlays | labels, numbers, disclaimers ("Magnified illustration"), source lines, per shot |
| Picture | Framing | where recurring parts sit, as fractions of frame height (see below) |
| Sound | Voice and music | synthetic or human voice, music bed, sound effects |

Beats are the video's skeleton. Write them as a time-coded template, like a text
skeleton. A beat seen in every video is observed; with one video, every beat is a guess.

## Shot table

Beats say what the script does; shots say what the picture does. Write one row per
shot, from the contact sheet plus a full frame at the start and end of each shot:

| Time | Beat | Camera | Objects | Overlays | Framing |
|---|---|---|---|---|---|
| 33.8-40.2 | mechanism | slow push-in, no cut | finger, glass slab, field lines | readout row 100 to 62, "Values illustrative" | glass top 0.48, readout 0.70, caption 0.16 |

Overlays belong to the shot they appear in. A label, disclaimer or readout seen in one
shot is not a rule for every shot: write "in mechanism shots" or "seen once", and add a
question under Unknowns. In testing, labels and a disclaimer copied from one shot into
all shots were the main visual errors a rebuild exposed.

Framing: on a full frame, read the pixel row of each recurring part (a layer edge, the
caption line, a readout row) and divide by the frame height. Record it in the table at
extract time. Measured late, framing cost three rebuild rounds.

## Rebuild inventory

When the user may want the look rebuilt, list what each shot needs before any rendering:

| Object | Build from code or download | License | Needs | Shots blocked without it |
|---|---|---|---|---|
| Fingertip | download (3D model) | CC BY 4.0, credit the author | nothing | 0-12, 30-57, 72-84 |
| Gloved hand gripping a phone | download | CC BY 4.0 | a skeleton (rig) to pose the grip | 12-16 |
| Wire grid, field lines, particles | code | none | nothing | none |

Prefer CC0, then CC BY (keep a credits file). Avoid licenses that restrict reuse.
A static mesh cannot be re-posed: a hand that must grip something needs a rigged model
or one already in that pose. Assets, not method, decide how much of a video can be rebuilt.

## Packaging and tools (pattern P9, P11)

Many videos come from a tool with house defaults (caption style, disclaimers,
render look). Check the title, description and watermark for a tool name. List
"which rules are tool defaults?" under Unknowns.

## Replay

1. Script replay: from the draft skill alone, write the script for each train
   brief. Diff beats, pacing and hook against the original transcript, and run
   `style_stats.py compare` on the scripts.
2. Motion replay (optional, when the user wants the look rebuilt): render one beat
   from code, then run
   `python3 scripts/frame_diff.py ORIGINAL OFFSET REPLAY` to measure layout gaps
   per frame (brightness, gold or accent glow, skin area, caption box, accent-row height).

Every numeric gap is a diagnostic, not acceptance. Always put the two clips
side by side and look: a number can match for the wrong reason (a small finger
and a large dark finger can cover the same area). Record what the eye catches
that the numbers miss.

A rebuild is the video's held-out test. List each rule it disproved (for example an
overlay written as global that only one shot carries) and fix the skill, not only the
render. Render a sampled pass (one frame every 1.5 s) before the full render, but also
check the full render: state that leaks from one shot into the next only shows there.

## Export

For video, the exported SKILL.md carries: the time-coded beat template, the shot table,
rules with evidence tags (overlays scoped per shot), the rebuild inventory, and Unknowns.

## What cannot be recovered from the video

Prompts to a 3D or image model, the render tool's settings, the voice model, and
any rule for content the videos never show. Write them as Unknowns.
