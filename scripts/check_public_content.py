"""Catch accidental reintroduction of source lab credentials (not a general secret scanner)."""
from pathlib import Path
import html
import re

docs = Path('docs')
patterns = [r'dcloud\s*(?:\d+|z{4})\s*!', r'cb\d+\.dc-\d+\.com',
            r'last\s+(?:four|4)[ -]+digits', r'dcloudconnect[^\s]*[?]']
errors = []
referenced = set()
for path in docs.rglob('*.md'):
    source = path.read_text(encoding='utf-8')
    plain = html.unescape(re.sub(r'<[^>]+>', '', source))
    if any(re.search(pattern, plain, re.I) for pattern in patterns):
        errors.append(f'Potential lab credential in {path}')
    referenced.update(re.findall(r'assets/images/([^\s)]+)', source))
assets = {p.name for p in (docs / 'assets/images').iterdir() if p.is_file()}
if assets != referenced:
    errors.append('Image directory contains missing or unreferenced files; review before publishing.')
if list(docs.rglob('*.docx')) or list(docs.rglob('*.zip')):
    errors.append('Original documents/archives must not be included in public docs.')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: public text checks; {len(assets)} referenced image assets. Review new images manually.')
