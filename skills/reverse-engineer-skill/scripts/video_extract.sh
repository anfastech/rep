#!/usr/bin/env bash
# Turn one video into readable evidence: metadata, hard cuts, contact sheet, transcript.
#   usage: bash video_extract.sh VIDEO OUTDIR
# Needs ffmpeg and ffprobe. Transcript needs openai-whisper (`whisper` on PATH); skipped without it.
set -euo pipefail
VIDEO=$1; OUT=$2
mkdir -p "$OUT"

ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate \
  -of compact "$VIDEO" > "$OUT/meta.txt"

ffmpeg -i "$VIDEO" -vf "select='gt(scene,0.25)',showinfo" -f null - 2>&1 |
  grep -o 'pts_time:[0-9.]*' | cut -d: -f2 > "$OUT/scenes.txt" || true

ffmpeg -v error -y -i "$VIDEO" \
  -vf "fps=1/3,scale=240:-1,drawtext=text='%{pts\:hms}':x=5:y=5:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=6x5" \
  -frames:v 1 "$OUT/sheet.jpg"

if command -v whisper >/dev/null; then
  ffmpeg -v error -y -i "$VIDEO" -ac 1 -ar 16000 "$OUT/audio.wav"
  whisper "$OUT/audio.wav" --model small --output_format json --output_dir "$OUT" \
    --word_timestamps True --fp16 False > "$OUT/whisper.log" 2>&1
  mv "$OUT/audio.json" "$OUT/transcript.json"
  python3 - "$OUT" <<'PY'
import json, re, sys
out = sys.argv[1]
d = json.load(open(f"{out}/transcript.json"))
with open(f"{out}/transcript.txt", "w") as f:
    for s in d["segments"]:
        f.write(f"{s['start']:6.1f}-{s['end']:6.1f} {s['text'].strip()}\n")
text = " ".join(s["text"].strip() for s in d["segments"])
open(f"{out}/script.txt", "w").write("\n".join(re.split(r"(?<=[.?!])\s+", text)) + "\n")
words = len(text.split())
dur = d["segments"][-1]["end"] - d["segments"][0]["start"]
print(f"words {words}, {round(words / dur * 60)} wpm over {dur:.1f} s")
PY
else
  echo "whisper not found: no transcript (pip install openai-whisper)"
fi

echo "duration $(grep -o 'duration=[0-9.]*' "$OUT/meta.txt" | cut -d= -f2) s, hard cuts $(wc -l < "$OUT/scenes.txt" | tr -d ' ')"
echo "wrote $OUT: meta.txt scenes.txt sheet.jpg $( [ -f "$OUT/script.txt" ] && echo transcript.txt transcript.json script.txt)"
