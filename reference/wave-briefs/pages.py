#!/usr/bin/env python3
"""Print pages of a source's text.md, split on form feeds, with PDF page numbers
and text.md line numbers. Bypasses the rtk hook's truncation of cat/head/sed.
A page's `=== OCR SUPPLEMENT, PDF PAGE n ===` block (appended at the end of
text.md by the render sweep) is printed under that page.

usage: pages.py <source-id> [from [to]]      (PDF page numbers, 1-based)
       pages.py <source-id> grep <regex>     (list pages whose text matches)
       pages.py <source-id> supplements      (list which pages carry OCR)
"""
import re, sys
sid = sys.argv[1]
text = open(f'sources/{sid}/text.md').read()
main, _, tail = text.partition('\n=== OCR SUPPLEMENT, PDF PAGE ')
supp = {}
if tail:
    for m in re.finditer(r'(?:^|\n=== OCR SUPPLEMENT, PDF PAGE )(\d+) ===\n(.*?)(?=\n=== OCR SUPPLEMENT, PDF PAGE |\Z)', tail, re.S):
        supp[int(m.group(1))] = m.group(2).rstrip()
pages = main.split('\x0c')
starts, n = [], 1
for p in pages:
    starts.append(n)
    n += p.count('\n')
mode = sys.argv[2] if len(sys.argv) > 2 else None
if mode == 'supplements':
    print('pages with OCR supplements:', sorted(supp) or 'none')
    sys.exit()
if mode == 'grep':
    rx = re.compile(sys.argv[3], re.I)
    for i, p in enumerate(pages, 1):
        body = p + '\n' + supp.get(i, '')
        hits = [l.strip() for l in body.splitlines() if rx.search(l)]
        if hits:
            print(f'--- page {i} ({len(hits)} hits): ' + ' | '.join(h[:80] for h in hits[:4]))
    sys.exit()
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else a
for i in range(a, min(b, len(pages)) + 1):
    print(f'\n======== PDF PAGE {i}  (text.md lines {starts[i-1]}-{starts[i-1] + pages[i-1].count(chr(10))}) ========')
    print(pages[i-1].rstrip())
    if i in supp:
        print(f'\n-------- OCR SUPPLEMENT for page {i} (what the render shows; not native text) --------')
        print(supp[i])
