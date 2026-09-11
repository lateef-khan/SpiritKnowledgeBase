#!/usr/bin/env python3
"""Delete duplicate cards and re-point every reference to the survivor.
usage: dedupe.py <loser-id>=<winner-id> ...   (both must be untracked-or-tracked cards on disk)"""
import sys, os, re, glob, yaml
os.chdir('/mnt/HDD/Projects/SpiritKnowledgeBase')
idx={}
for f in glob.glob('cards/**/*.md', recursive=True):
    m=re.search(r'^id: (.*)$', open(f).read(), re.M)
    if m: idx[m.group(1).strip()]=f
pairs=[a.split('=') for a in sys.argv[1:]]
import subprocess
touched=set(l[3:] for l in subprocess.run(['git','status','--porcelain','-uall','cards/'],capture_output=True,text=True).stdout.splitlines())
for lose,win in pairs: assert lose in idx and win in idx, (lose,win)
for f in list(idx.values()):
    t=open(f).read(); orig=t; d=os.path.dirname(f)
    for lose,win in pairs:
        if f==idx[lose]: continue
        # relative links
        def sub(m):
            tgt=os.path.normpath(os.path.join(d,m.group(1)))
            return f']({os.path.relpath(idx[win], d)})' if tgt==idx[lose] else m.group(0)
        t=re.sub(r'\]\(([^)]+\.md)\)', sub, t)
        # list entries in see_also / not_to_be_confused_with (self-link guard)
        if f==idx[win]: t=re.sub(r'^- '+re.escape(lose)+r'\n', '', t, flags=re.M)
        else: t=re.sub(r'^- '+re.escape(lose)+r'$', '- '+win, t, flags=re.M)
        # bare id mentions in body text
        t=t.replace('`'+lose+'`','`'+win+'`')
    # dedupe see_also / ntbcw lists
    def dedupe_block(m):
        seen=[]; 
        for l in m.group(2).splitlines():
            if l not in seen: seen.append(l)
        return m.group(1)+'\n'.join(seen)+'\n'
    t=re.sub(r'^((?:see_also|not_to_be_confused_with):\n)((?:- .*\n)+)', dedupe_block, t, flags=re.M)
    # only a real re-pointing may touch a card outside the wave; list dedupe alone must not
    if t!=orig and (any(lose in orig for lose,_ in pairs) or f in touched): open(f,'w').write(t)
for lose,win in pairs:
    os.remove(idx[lose]); print('deleted', idx[lose], '->', win)
