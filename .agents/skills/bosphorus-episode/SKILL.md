---
name: bosphorus-episode
description: Make one episode of The Bosphorus Files (English history documentary, Ottoman/Byzantine/war history) from a topic to a rendered MP4 in GitHub Actions, without running Python on the owner's PC. Use when the owner says "bölüm yap", "yeni bölüm", "episode", or gives a history topic.
---

# Bosphorus Files episode

The film engine is `engine/` (cinematic-film, MIT). Read `engine/SKILL.md` and `engine/references/film.md`
and `engine/references/story.md` once per session: they are the rules for scenes and scripts.
`episodes/E001-ships-over-land/` is the reference episode: copy its *structure*, never its layout.

## Gates (stop and ask the owner, in Turkish)
- **Gate 1:** after the script: show the beat table (one line per narration line: text, hero, typed)
  and the fact notes with sources. Wait for "onay".
- **Gate 2:** after the render: show the probe stills, the photo contact sheet and the MP4 path.

## Steps
1. **Folder.** `episodes/E0NN-short-slug/` (next free number).
2. **Research.** Search the web; 2+ independent sources per number, date and name. Write
   `fact_notes` in script.json, one note per claim, with the source.
3. **script.json.** Takes (sections of 2–4 lines) of lines: `id`, `text`, `spoken` (numbers and dates
   in words), `hero` (what the camera shows), `typed` (big on-screen text or ""). Cold open first,
   one bridge line ("Three weeks earlier..."), then time only moves forward. Length: 60 s ≈ 150 words,
   10 min ≈ 1,450 words, 20 min ≈ 2,900 words. Optional `gap_after` (seconds) on a line.
4. **Gate 1.**
5. **photos.json.** One entry per image: `id`, `what`, `kind` (photo|doc), and either `commons`
   ("File:...", exact) or `query` (a Commons search; the workflow picks the first free-licensed hit
   ≥1000 px and writes it back). Prefer paintings, miniatures, maps and engravings old enough to be
   public domain. `grade`: natural for paintings, bw for photographs.
6. **voice.json.** Copy `episodes/E001-ships-over-land/voice.json` as is: channel voice is **Orus** with the documentary
   style prompt and the EQ/compression `post` chain (owner approved, Nov 2026). Do not change the voice
   unless the owner asks; to audition voices run `gh workflow run voice-samples -f voices="Orus,Gacrux"`.
   Voice runs in Actions with the `GEMINI_API_KEY` secret (free tier). Recorded takes are cached between
   runs, so a failed run does not spend the quota again.
7. **scene.py.** One wall, clusters left to right, one hero per line, hits on spoken words via
   `doc.W(line, "word")` (search the SPOKEN text). Fit every print fully in frame: frame height in
   world units = 2160 / zoom. Keep big type ≥ 500 units. Add a wide camera key between far clusters
   so travel never shows an empty board. End on a pull-back of the whole wall.
8. **meta.json.** `title`, `description` (hook paragraph, chapters, sources, credits), `tags`.
9. **Push and render** (on the PC: only git and gh):
   ```
   git add -A && git commit -m "E0NN: <title>" && git push
   gh workflow run render -f episode=E0NN-short-slug -f chunks=8
   gh run watch
   gh run download --name final-E0NN-short-slug --dir out/E0NN
   ```
10. **Gate 2.** Look at `probe/*.png` and `photos_sheet.jpg`. Wrong image → set its `commons`
    by hand. Bad framing → fix scene.py. Re-run.

## Turkish version (Boğaz Dosyaları)
Copy the episode to `E0NN-slug-tr/`, translate `text` and `spoken` (natural Turkish, not literal),
translate `typed` and labels in scene.py, set voice.json style to Turkish narration. Same images.
