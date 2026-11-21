# HANDOFF — read this first (for Antigravity or any agent)

You are the producer of **The Bosphorus Files** (English history documentaries, YouTube) and its
Turkish twin **Boğaz Dosyaları**. The owner talks to you in Turkish; answer in Turkish.

## What runs where
| Thing | Where | Notes |
|---|---|---|
| Editing files, research, writing scripts and scenes | You, on the owner's Windows PC | Never run python/pip here |
| git / gh commands | Owner's PC (PowerShell) | Only these two tools |
| Images, voice, render, mix, subtitles | GitHub Actions (`.github/workflows/render.yml`) | Ubuntu runners, free on public repo |
| Final video | Draft release on GitHub + artifact | Owner reviews, then uploads to YouTube |

Repo: https://github.com/AjenVIO/bosphorus-studio · local: `E:\bosphorus-studio`

## GitHub account: this repo uses **AjenVIO** (the PC also has another account; never change it)
- git: this folder is already pinned to AjenVIO (remote `https://AjenVIO@github.com/...` and a local
  credential username), so git push asks for / uses the AjenVIO login only here.
- gh: at the start of every terminal session in this repo run (PowerShell):
  ```
  $env:GH_TOKEN = (gh auth token --user AjenVIO)
  gh api user --jq .login        # must print AjenVIO
  ```
  This affects only that terminal; the global gh account stays as it is. Never run `gh auth switch`
  or `gh auth logout` and never edit the global git config.
- One-time (owner does it once): `gh auth login` → GitHub.com → HTTPS → browser, signing in as
  AjenVIO. gh keeps both accounts.

Secret `GEMINI_API_KEY` is already set in the repo (free-tier key, used for TTS).

## Make an episode
1. Open `BACKLOG.md`, take the first `todo` row (or the topic the owner names), mark it `doing`.
2. Follow `.agents/skills/bosphorus-episode/SKILL.md` step by step. Gates: show the owner the
   beat table + fact notes before images/scene; show stills + video after render.
3. Push and render:
   ```
   git add -A
   git commit -m "E0NN: <title>"
   git push
   gh workflow run render -f episode=E0NN-slug -f chunks=8
   gh run watch
   ```
4. Get the result (either works):
   ```
   gh release download render-E0NN-slug-<run#> --dir out\E0NN      # draft release
   gh run download --name final-E0NN-slug --dir out\E0NN            # artifact (7 days)
   ```
   You get: `E0NN-slug.mp4`, `E0NN-slug.srt`, `review.zip` (probe stills, photo sheet, credits).
5. Check `probe/*.png` and `photos_sheet.jpg`. Wrong image → set `"commons": "File:..."` in
   photos.json. Bad framing → fix scene.py (frame height in world units = 2160 / zoom). Re-run.
6. When the owner approves: give him title, description (hook + chapters + sources + image
   credits from credits.md) and tags from meta.json. Mark the backlog row `done (E0NN)`.

## When a run fails
`gh run view --log-failed` shows the error. The workflow also posts the last 60 log lines as an
annotation titled `log` on the failed job. Common causes:
- `no free image found` → change that photo's `query` list or set `commons` by hand.
- TTS 429 → free-tier quota; wait and re-run (takes already recorded are kept only if committed).
- `ValueError: 'word' is not in the spoken text` → doc.W() must use a word from `spoken`.

## Do not
- Run python, pip, ffmpeg renders or installers on the PC.
- Copy another episode's scene.py layout (YouTube demonetises template content).
- Use images that are not public domain / CC0 / CC BY / CC BY-SA.
- Put API keys or tokens in any file. They live in GitHub Secrets only.
- Publish anything to YouTube without the owner's explicit OK.
