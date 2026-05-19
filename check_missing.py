import os, re

PAPERS_DIR = os.path.join('.', 'content', 'papers')
with open('missing_authors.txt', encoding='utf-8') as f:
    listed = [l.strip() for l in f if l.strip().endswith('.md')]

still_missing = []
now_has_authors = []
for fname in listed:
    fpath = os.path.join(PAPERS_DIR, fname)
    if not os.path.exists(fpath):
        still_missing.append(('MISSING FILE', fname))
        continue
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        text = f.read()
    m = re.search(r'^authors:\s*(.+)$', text, re.MULTILINE)
    if m:
        now_has_authors.append((fname, m.group(1).strip().strip('"')))
    else:
        still_missing.append(('no authors', fname))

print('=== NOW HAS AUTHORS ===')
for fname, auth in now_has_authors:
    fs = fname[:65].encode('ascii', errors='replace').decode()
    a = auth[:50].encode('ascii', errors='replace').decode()
    print(f'  {fs} -> {a}')
print(f'\nTotal: {len(now_has_authors)}')

print()
print('=== STILL MISSING ===')
for reason, fname in still_missing:
    fs = fname[:70].encode('ascii', errors='replace').decode()
    print(f'  [{reason}] {fs}')
print(f'\nTotal: {len(still_missing)}')
