#!/usr/bin/env bash
# CI setup without apt-get update (which can hang on slow mirrors): static ffmpeg from GitHub,
# system GL/font libs only if missing, each step time-limited.
set -eo pipefail
if ! command -v ffmpeg >/dev/null; then
  curl -sSL --retry 3 -m 240 -o /tmp/ff.tar.xz https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz
  tar -xJf /tmp/ff.tar.xz -C /tmp && sudo cp /tmp/ffmpeg-master-latest-linux64-gpl/bin/ff* /usr/local/bin/
fi
ffmpeg -version | head -1
missing=""
for lib in libGL.so.1 libEGL.so.1 libfontconfig.so.1; do ldconfig -p | grep -q "$lib" || missing="$missing $lib"; done
if [ -n "$missing" ]; then
  echo "missing:$missing"
  timeout 240 sudo apt-get -o Acquire::Retries=3 -o Acquire::http::Timeout=20 install -y -qq --no-install-recommends libgl1 libegl1 libfontconfig1 fonts-dejavu-core >/dev/null \
  || { timeout 180 sudo apt-get -o Acquire::http::Timeout=20 update -qq && timeout 240 sudo apt-get install -y -qq --no-install-recommends libgl1 libegl1 libfontconfig1 fonts-dejavu-core >/dev/null; }
fi
pip install -q -r requirements.txt
