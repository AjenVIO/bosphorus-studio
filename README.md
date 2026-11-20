# Bosphorus Studio

Production repo for **The Bosphorus Files** (YouTube). Code-drawn history documentaries, rendered
in GitHub Actions. See AGENTS.md for the rules and `.agents/skills/bosphorus-episode/SKILL.md` for
the workflow. Licence: see LICENSE (proprietary; engine/ is MIT).

## Kurulum (bir kez)
1. GitHub'da boş, **public** bir repo aç: `bosphorus-studio` (README eklemeden).
2. Bu klasörde (PowerShell):
   ```
   git init -b main
   git add -A
   git commit -m "Bosphorus Studio initial"
   git remote add origin https://github.com/<kullanici>/bosphorus-studio.git
   git push -u origin main
   ```
3. Gemini API anahtarı (ücretsiz, kart istemez): https://aistudio.google.com/apikey →
   repo **Settings → Secrets and variables → Actions → New repository secret** →
   adı `GEMINI_API_KEY`.
4. Actions sekmesi → **render** → Run workflow → episode: `E001-ships-over-land`.

## Bölüm üretmek
Antigravity'de: "yeni bölüm: <konu>" — ajan `.agents/workflows/bolum.md` adımlarını izler.
