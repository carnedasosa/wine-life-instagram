#!/usr/bin/env bash
# Esporta slide HTML in PNG 1080x1350. Serve Chrome, Chromium o Edge.
# Ogni cartella finisce nella png/ accanto a lei: post/04-nebbiolo -> post/png/04-nebbiolo-slide-1.png
# Uso (dalla radice di wine-life):
#   bash templates/export.sh                      tutti i template
#   bash templates/export.sh templates/consiglia-post
#   bash templates/export.sh post/04-nebbiolo post/06-600-acini
#   bash templates/export.sh post/*/              tutti i post
# Funziona su macOS, Linux e Windows (Git Bash, quello che usa Claude Code).
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
find_chrome() {
  command -v google-chrome || command -v chromium || command -v chromium-browser && return
  for c in "/c/Program Files/Google/Chrome/Application/chrome.exe" \
           "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
           "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    [ -x "$c" ] && echo "$c" && return
  done
  return 0
}
CHROME="${CHROME:-$(find_chrome)}"
[ -n "$CHROME" ] || { echo "Chrome non trovato: imposta CHROME=/percorso/chrome"; exit 1; }
# Su Windows Chrome vuole file:///C:/..., altrove file:///home/...
if BASE=$(pwd -W 2>/dev/null); then BASE="file:///$BASE"; else BASE="file://$PWD"; fi
[ $# -gt 0 ] || set -- templates/*/
for d in "$@"; do
  d="${d%/}"; name="$(basename "$d")"
  [ "$name" = png ] && continue
  ls "$d"/*.html >/dev/null 2>&1 || continue
  mkdir -p "$(dirname "$d")/png"
  for f in "$d"/*.html; do
    out="$(dirname "$d")/png/$name-$(basename "$f" .html).png"
    "$CHROME" --headless=new --disable-gpu --hide-scrollbars $CHROME_FLAGS --force-device-scale-factor=1 \
      --window-size=1080,1350 --virtual-time-budget=6000 --screenshot="$ROOT/$out" "$BASE/$f" >/dev/null 2>&1
    echo "ok  $out"
  done
done
