#!/usr/bin/env python3
"""After the agents: every NEW card whose applies_to names exactly one machine gets
that machine's model_number from reference/model-numbers.csv (inserted after `code:`),
and any new multi-machine card that carries one loses it. Regex edits only - never
round-trip through render_card. Product cards (lookup: model-numbers) are skipped."""
import csv, re, subprocess, sys, os
os.chdir('/mnt/HDD/Projects/SpiritKnowledgeBase')
skus = {r['machine']: r['model_number'].split() for r in csv.DictReader(open('reference/model-numbers.csv'))}
status = subprocess.run(['git','status','--porcelain','-uall','cards/'], capture_output=True, text=True).stdout.splitlines()
new = [l[3:] for l in status if l.startswith('??') and l.endswith('.md')]
added = removed = 0
for f in new:
    t = open(f).read()
    if 'lookup: model-numbers' in t: continue
    m = re.search(r'\n  applies_to:\n((?:  - .*\n)+)', t)
    if not m: continue
    ap = [l.strip()[2:] for l in m.group(1).splitlines()]
    has = re.search(r'\n  model_number:\n(?:  - .*\n)+', t)
    if len(ap) == 1 and ap[0] != '*' and ap[0] in skus:
        if has: continue
        block = '  model_number:\n' + ''.join(f"  - '{s}'\n" for s in skus[ap[0]])
        t2 = re.sub(r"(\n  code: [^\n]*\n)", r"\1" + block, t, count=1)
        if t2 != t: open(f,'w').write(t2); added += 1
    elif len(ap) != 1 and has:
        t2 = t.replace(has.group(0), '\n'); open(f,'w').write(t2); removed += 1
print(f'model_number added to {added} one-machine cards, removed from {removed} multi-machine cards')
