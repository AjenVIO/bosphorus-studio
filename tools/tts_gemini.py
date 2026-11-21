#!/usr/bin/env python3
"""Record narration takes with the Gemini API (free-tier key, no billing) into audio/takes/<take>.wav.

One request per take (a whole section), so the delivery stays consistent; split_takes.py cuts it
into lines afterwards. Takes that already exist are kept (record them in AI Studio by hand if you like).

  GEMINI_API_KEY=... python3 tools/tts_gemini.py --project episodes/E001-ships-over-land

voice.json in the project (optional): {"voice": "Orus", "style": "...", "model": "...", "post": "<ffmpeg -af chain>"}
"""
import argparse, base64, json, os, pathlib, subprocess, sys, time, urllib.request, urllib.error

MODELS = ["gemini-3.1-flash-tts-preview", "gemini-2.5-flash-preview-tts"]
STYLE = ("Read this as the narrator of a serious history documentary: a deep, calm, measured voice, "
         "slightly grave, never theatrical. Leave a clear one-second pause at every paragraph break.")

class EmptyAudio(Exception):
    pass


def call(model, key, text, voice):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    body = {"contents": [{"parts": [{"text": text}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
    try:
        part = d["candidates"][0]["content"]["parts"][0]["inlineData"]
    except (KeyError, IndexError):
        reason = (d.get("candidates") or [{}])[0].get("finishReason", "?")
        raise EmptyAudio(f"no audio in response (finishReason={reason})")
    return base64.b64decode(part["data"]), part.get("mimeType", "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    proj = pathlib.Path(a.project)
    script = json.loads((proj / "script.json").read_text())
    cfg = json.loads((proj / "voice.json").read_text()) if (proj / "voice.json").exists() else {}
    voice, style = cfg.get("voice", "Orus"), cfg.get("style", STYLE)
    models = [cfg["model"]] if cfg.get("model") else MODELS
    tdir = proj / "audio" / "takes"; tdir.mkdir(parents=True, exist_ok=True)
    for take in script["takes"]:
        out = tdir / f"{take['take']}.wav"
        if out.exists() and not a.force:
            print(f"{out.name}: exists, kept"); continue
        if not key:
            sys.exit("GEMINI_API_KEY is not set and takes are missing: add the secret or commit the takes")
        text = style + "\n\n" + "\n\n".join(l["spoken"].strip() for l in take["lines"])
        pcm = None
        for m in models:
            for attempt in range(4):
                try:
                    pcm, mime = call(m, key, text, voice); break
                except EmptyAudio as e:
                    print(f"{m}: {e}, retrying")
                    time.sleep(8 * (attempt + 1)); continue
                except urllib.error.HTTPError as e:
                    msg = e.read().decode()[:300]
                    print(f"{m}: HTTP {e.code} {msg}")
                    if e.code in (429, 500, 503) and attempt < 3:
                        time.sleep(20 * (attempt + 1)); continue
                    break
            if pcm: break
        if not pcm:
            sys.exit(f"TTS failed for {take['take']}")
        raw = tdir / f"{take['take']}.pcm"; raw.write_bytes(pcm)
        post = ["-af", cfg["post"]] if cfg.get("post") else []
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", str(raw),
                        *post, "-ar", "48000", str(out)], check=True)
        raw.unlink()
        print(f"{out.name}: recorded with {m} / {voice}")
        time.sleep(3)

if __name__ == "__main__":
    main()
