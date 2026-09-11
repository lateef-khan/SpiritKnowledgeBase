#!/usr/bin/env python3
"""Post-wave reconciliation checks that `kb lint` does not make.

Run from the repo root: rtk proxy python3 $S/reconcile.py
"""
import re, subprocess, glob, collections, os, sys
import yaml

sys.path.insert(0, '/mnt/HDD/Projects/SpiritKnowledgeBase')
os.chdir('/mnt/HDD/Projects/SpiritKnowledgeBase')

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

kb = yaml.safe_load(open('kb.yaml'))
models = {b: set(v) for b, v in kb['models'].items()}
all_models = set().union(*models.values())
sections = set(kb['facets']['section']['values'])

status = sh('git status --porcelain -uall cards/').splitlines()
new_files = [l[3:] for l in status if l.startswith('??')]
mod_files = [l[3:] for l in status if l.startswith(' M') or l.startswith('M ') or l.startswith('MM')]
del_files = [l[3:] for l in status if l.startswith(' D') or l.startswith('D ')]
print(f'new cards: {len(new_files)}   modified cards: {len(mod_files)}   deleted: {len(del_files)}')
if del_files:
    print('!! DELETED FILES:'); [print('   ', f) for f in del_files]

def load(path):
    t = open(path).read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', t, re.S)
    if not m: return None, t
    try:
        return yaml.safe_load(m.group(1)), m.group(2)
    except Exception as e:
        return None, t

cards = {}
for f in glob.glob('cards/**/*.md', recursive=True):
    fm, body = load(f)
    if fm: cards[f] = (fm, body)
ids = {fm['id']: f for f, (fm, _) in cards.items()}
print(f'cards on disk: {len(cards)}')

touched = set(new_files) | set(mod_files)
problems = collections.Counter()

def warn(kind, msg):
    problems[kind] += 1
    print(f'[{kind}] {msg}')

for f in sorted(touched):
    if f not in cards:
        warn('unparseable', f); continue
    fm, body = cards[f]
    fa = fm.get('facets', {})
    brands = fa.get('brand') or []
    if isinstance(brands, str): brands = [brands]
    # two-brand cards
    if len(brands) != 1:
        warn('brand-count', f'{f}: brand={brands}')
    # Sole cards touched by this wave
    if f in mod_files and 'sole' in brands:
        warn('sole-touched', f)
    # id / section agreement
    sec = fa.get('section')
    cid = fm['id']
    for s in sections:
        if f'-{s}-' in cid and s != sec and not (s == 'specs' and sec == 'specs'):
            warn('id-section', f'{cid}: id names {s}, facet says {sec}')
    # folder / section agreement
    parts = f.split('/')
    if len(parts) >= 3 and parts[2] != sec and parts[1] != 'shared':
        warn('folder-section', f'{f}: folder {parts[2]} vs facet {sec}')
    if parts[1] == 'shared' and parts[2] != sec:
        warn('folder-section', f'{f}: shared folder {parts[2]} vs facet {sec}')
    # shared filename must be the full id
    if parts[1] == 'shared' and os.path.basename(f) != cid + '.md':
        warn('shared-filename', f'{f}: basename is not the id {cid}')
    # one-machine card in the right folder
    ap = fa.get('applies_to') or []
    if isinstance(ap, str): ap = [ap]
    model = fa.get('model')
    if isinstance(model, list): model = model[0] if len(model) == 1 else '*'
    if len(ap) == 1 and ap != ['*'] and model != ap[0]:
        warn('model-applies', f'{cid}: model={model} applies_to={ap}')
    if len(ap) > 1 and model != '*':
        warn('model-applies', f'{cid}: model={model} but applies_to lists {len(ap)}')
    if ap == ['*']:
        warn('applies-star', f'{cid}: applies_to is * (must be a policy-level fact)')
    for m in ap:
        if m != '*' and m not in all_models:
            warn('dangling-model', f'{cid}: {m}')
    if ap != ['*'] and brands and any(m not in models.get(brands[0], set()) for m in ap if m != '*'):
        warn('brand-model', f'{cid}: brand {brands} vs applies_to {ap}')
    if len(ap) == 1 and parts[1] != ap[0] and parts[1] != 'shared':
        warn('folder-model', f'{f}: one-machine card for {ap[0]} not under cards/{ap[0]}/')
    # stray model_number / lookup on non-product cards
    # one-machine cards carry model_number; a card naming several machines must not
    if 'model_number' in fa and fa.get('lookup') != 'model-numbers' and len(ap) != 1:
        warn('stray-model-number', cid)
    # links resolve
    for l in re.findall(r'\]\(([^)]+\.md)\)', body):
        if not os.path.exists(os.path.join(os.path.dirname(f), l)):
            warn('broken-link', f'{f} -> {l}')
    for l in list(fm.get('see_also') or []) + list(fm.get('not_to_be_confused_with') or []):
        if l not in ids:
            warn('dangling-see-also', f'{cid} -> {l}')
    # extracted_at
    if str(fm.get('source', {}).get('extracted_at')) != '2026-09-11' and f in new_files:
        warn('extracted-at', f'{cid}: {fm.get("source", {}).get("extracted_at")}')
    # question names a model or the brand
    q = fm.get('question', '')
    if not (any(m in q for m in ap) or 'spirit' in q.lower() or 'xterra' in q.lower()):
        warn('question-model', f'{cid}: {q[:70]}')
    # title with a model id token
    if re.search(r'\b[a-z]{1,2}\d{1,3}\b', fm.get('title', '')):
        warn('title-model-token', f'{cid}: {fm.get("title")[:70]}')

# duplicate titles across the whole repo, restricted to ones this wave touched
def norm(t):
    t = t.lower().replace('ise', 'ize').replace('isation', 'ization')
    return ' '.join(sorted(re.findall(r'[a-z0-9]+', t)))
by_title = collections.defaultdict(list)
for f, (fm, _) in cards.items():
    by_title[norm(fm.get('title', ''))].append(f)
for t, fs in by_title.items():
    if len(fs) > 1 and any(f in touched for f in fs):
        warn('dup-title', f'{fs[0].split("/")[-1][:50]}: ' + ', '.join(fs))

# duplicate ids
by_id = collections.Counter(fm['id'] for fm, _ in cards.values())
for i, n in by_id.items():
    if n > 1: warn('dup-id', i)

# inventory of new cards per section and per model
inv = collections.Counter()
for f in new_files:
    if f in cards:
        fa = cards[f][0].get('facets', {})
        inv[(fa.get('section'), 'shared' if f.split('/')[1] == 'shared' else f.split('/')[1])] += 1
print('\nnew cards by section:')
sec_tot = collections.Counter()
for (s, m), n in inv.items(): sec_tot[s] += n
for s, n in sorted(sec_tot.items(), key=lambda x: -x[1]): print(f'  {s:12} {n}')
print('\nmodified existing cards by section:')
ms = collections.Counter(cards[f][0]['facets'].get('section') for f in mod_files if f in cards)
for s, n in sorted(ms.items(), key=lambda x: -x[1]): print(f'  {s:12} {n}')
print('\nproblem summary:', dict(problems) or 'none')
