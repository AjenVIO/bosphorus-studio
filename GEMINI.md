# The Bosphorus Files — production studio

This repo makes narrated history documentaries for the YouTube channel **The Bosphorus Files**
(English) and its Turkish twin **Boğaz Dosyaları**. Every frame is drawn by code (engine/, Skia in
Python); images come from Wikimedia Commons with free licences; the voice is Gemini TTS.

**Start here:** read `HANDOFF.md` (how the system runs) and `BACKLOG.md` (what to make next).

## Hard rules for any agent working here
1. **Never run Python, pip or the render on the owner's PC.** All Python runs in GitHub Actions
   (`.github/workflows/render.yml`). On the PC you only edit files and use `git` and `gh`.
2. **Zero spending.** No paid APIs, no billing, no trials that ask for a card.
3. **Facts are sourced.** Every claim in `script.json` has a line in `fact_notes` with its source.
   If a fact is disputed, the narration says so ("said to be", "about 70").
4. **Only free-licensed images** (public domain, CC0, CC BY, CC BY-SA). Never upload a photo of a
   living private person. AI images only as labelled illustration, never as evidence.
5. **Every episode is different**: its own layout, items and camera. Never copy a scene.py and
   only swap the photos — YouTube demonetises template content.
6. Secrets (`GEMINI_API_KEY`, YouTube tokens) live only in GitHub Secrets. Never write them to a file.
7. Talk to the owner in Turkish; keep code, comments and docs in English.

## How to make an episode
Follow `.agents/skills/bosphorus-episode/SKILL.md`. Short version: research → script.json → the
owner approves the beat table → photos.json → scene.py → push → `gh workflow run render` →
review the artifact → upload.
