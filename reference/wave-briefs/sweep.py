#!/usr/bin/env python3
"""Render-vs-extraction sweep for one PDF.

For every page: count the words a 300 dpi render (tesseract --psm 4) knows that
the native text layer does not. When the gain is >= 5 words, append the OCR text
to the source's text.md under an `=== OCR SUPPLEMENT, PDF PAGE n ===` header.
Scans are scored at all four rotations and the best kept.

usage: sweep.py <pdf> <text.md> [--force-ocr]
"""
import re, subprocess, sys, tempfile, os
from concurrent.futures import ThreadPoolExecutor

pdf, textmd = sys.argv[1], sys.argv[2]
force = '--force-ocr' in sys.argv

info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
n = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))

# Rotation is scored by dictionary hits. The earlier scorer (common words plus 0.1 x
# token count) let a garbage rotation of a label-only landscape page win on token
# count alone; on 2026-09-11 most Dyaco service-manual picture pages came out upside
# down that way. A wrong rotation produces almost no dictionary words.
WORDS = set(w.strip().lower() for w in open('/usr/share/dict/words')
            if len(w.strip()) >= 3 and w.strip().isalpha())

def words(t):
    return set(w for w in re.findall(r'[a-z0-9]+', t.lower()) if len(w) > 1)

def score(t):
    return sum(1 for w in re.findall(r'[A-Za-z]{3,}', t) if w.lower() in WORDS)

def ocr_png(png, rot):
    src = png
    if rot:
        rotated = png.replace('.png', f'-r{rot}.png')
        from PIL import Image
        Image.open(png).rotate(rot, expand=True).save(rotated)
        src = rotated
    out = subprocess.run(['tesseract', src, 'stdout', '--psm', '4'], capture_output=True, text=True).stdout
    return out

def page(p):
    nat = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', pdf, '-'], capture_output=True, text=True).stdout
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['pdftoppm', '-r', '300', '-png', '-f', str(p), '-l', str(p), pdf, f'{d}/pg'], check=True)
        pngs = [f for f in os.listdir(d) if f.endswith('.png')]
        if not pngs:
            return p, 0, ''
        png = f'{d}/{pngs[0]}'
        best = ocr_png(png, 0)
        # a scanned page can read plausibly upside down: score all four rotations
        # score all four rotations on any page the text layer barely covers
        if len(words(nat)) < 25:
            cands = [best] + [ocr_png(png, r) for r in (90, 180, 270)]
            best = max(cands, key=score)
    gained = len(words(best) - words(nat))
    return p, gained, best

results = []
with ThreadPoolExecutor(max_workers=4) as ex:
    for p, gained, ocr in ex.map(page, range(1, n + 1)):
        results.append((p, gained, ocr))

added = []
with open(textmd, 'a') as fh:
    for p, gained, ocr in results:
        if gained >= 5 or (force and ocr.strip()):
            fh.write(f'\n\n=== OCR SUPPLEMENT, PDF PAGE {p} ===\n')
            fh.write(f'<!-- render-vs-extraction: {gained} words the text layer does not have; tesseract --psm 4 at 300 dpi -->\n')
            fh.write(ocr.rstrip() + '\n')
            added.append((p, gained))
print(f'{os.path.basename(pdf)}: {n} pages, supplemented {len(added)}: ' + ' '.join(f'p{p}(+{g})' for p, g in added))
