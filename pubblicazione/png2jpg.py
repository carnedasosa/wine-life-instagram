#!/usr/bin/env python3
"""Converte le PNG dei post in JPEG per l'API di Instagram (che non accetta PNG).

Uso (dalla radice di wine-life):
  python pubblicazione/png2jpg.py post/png/11-*.png     solo alcune
  python pubblicazione/png2jpg.py                       tutte quelle di post/png/
Serve Pillow: pip install pillow
"""
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
files = [Path(a) for a in sys.argv[1:]] or sorted((HERE.parent / "post" / "png").glob("*.png"))
out = HERE / "jpg"
out.mkdir(exist_ok=True)
for f in files:
    dest = out / (f.stem + ".jpg")
    Image.open(f).convert("RGB").save(dest, "JPEG", quality=92, optimize=True, progressive=True)
    print(f"ok  {dest.relative_to(HERE.parent)}")
