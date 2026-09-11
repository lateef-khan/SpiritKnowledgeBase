#!/usr/bin/env python3
"""Re-score the rotation of OCR supplements. The sweep picked the rotation by common-word
count plus 0.1 x token count, which lets a garbage rotation of a label-only page win on
token count. This pass scores every existing supplement by dictionary hits; a block with a
low ratio is re-OCR'd at 0/90/180/270 and replaced by the rotation with the most dictionary
words when that beats the stored block. Prints one line per replaced page."""
import re, sys, os, subprocess, tempfile, yaml
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
os.environ['OMP_THREAD_LIMIT'] = '1'
os.chdir('/mnt/HDD/Projects/SpiritKnowledgeBase')
WORDS = set(w.strip().lower() for w in open('/usr/share/dict/words') if len(w.strip()) >= 3 and w.strip().isalpha())
HDR = re.compile(r'\n=== OCR SUPPLEMENT, PDF PAGE (\d+) ===\n')
def score(t):
    toks = re.findall(r'[A-Za-z]{3,}', t)
    return sum(1 for w in toks if w.lower() in WORDS), len(toks)
man = {e['id']: e for e in yaml.safe_load(open('sources/manifest.yaml'))}
sids = sys.argv[1:]
def ocr(png, rot):
    src = png
    if rot:
        src = png.replace('.png', f'-r{rot}.png'); Image.open(png).rotate(rot, expand=True).save(src)
    return subprocess.run(['tesseract', src, 'stdout', '--psm', '4'], capture_output=True, text=True).stdout
def redo(pdf, p):
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['pdftoppm', '-r', '300', '-png', '-f', str(p), '-l', str(p), pdf, f'{d}/pg'], check=True)
        png = [f'{d}/{f}' for f in os.listdir(d) if f.endswith('.png')][0]
        cands = [(ocr(png, r), r) for r in (0, 90, 180, 270)]
    return max(cands, key=lambda c: score(c[0])[0])
for sid in sids:
    path = f'sources/{sid}/text.md'; t = open(path).read()
    pdf = man[sid]['origin_uri'].replace('file://', '')
    parts = HDR.split(t)                      # [head, page, block, page, block, ...]
    todo = []
    for i in range(1, len(parts), 2):
        p, block = int(parts[i]), parts[i + 1]
        body = re.sub(r'^<!--.*?-->\n', '', block, count=1, flags=re.S)
        hits, n = score(body)
        if n >= 8 and hits / n < 0.5:
            todo.append((i, p, hits))
    def work(item):
        i, p, hits = item
        best, rot = redo(pdf, p)
        return i, p, hits, best, rot
    replaced = 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, p, hits, best, rot in ex.map(work, todo):
            bh, bn = score(best)
            if bh > hits + 2:
                comment = re.match(r'^<!--.*?-->\n', parts[i + 1], flags=re.S)
                c = comment.group(0) if comment else ''
                c = c.replace(' -->', f'; re-OCR at {rot} degrees after the first pass scored a wrong rotation -->')
                parts[i + 1] = c + best.rstrip() + '\n'
                replaced += 1
                print(f'{sid} p{p}: {hits} -> {bh} dictionary words, rotation {rot}')
    if replaced:
        out = parts[0]
        for i in range(1, len(parts), 2):
            out += f'\n=== OCR SUPPLEMENT, PDF PAGE {parts[i]} ===\n' + parts[i + 1]
        open(path, 'w').write(out)
    print(f'{sid}: {len(todo)} low-ratio blocks checked, {replaced} replaced')
