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
| Picture | Overlays | labels, numbers, disclaimers ("Magnified illustration"), source lines |
| Sound | Voice and music | synthetic or human voice, music bed, sound effects |

Beats are the video's skeleton. Write them as a time-coded template, like a text
skeleton. A beat seen in every video is observed; with one video, every beat is a guess.

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

## What cannot be recovered from the video

Prompts to a 3D or image model, the render tool's settings, the voice model, and
any rule for content the videos never show. Write them as Unknowns.
