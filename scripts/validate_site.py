"""Validate the rendered Pages artifact before it is published (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import sys
import re

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
errors = []
source = Path('_data/publications.yml').read_text(encoding='utf-8')
records = re.split(r'(?m)^- id: ', source)[1:]
paper_ids = [record.splitlines()[0].strip() for record in records]
unlinked_manuscripts = [record.splitlines()[0].strip() for record in records
                        if re.search(r'(?m)^  category: manuscript\s*$', record)
                        and not re.search(r'(?m)^  arxiv: https://arxiv\.org/abs/', record)]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.lang = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if a.get('id'):
            if a['id'] in self.ids: errors.append('Duplicate ID: ' + a['id'])
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key): self.links.append(a[key])

for relative, language in [('index.html', 'en'), ('zh/index.html', 'zh-CN')]:
    path = root / relative
    if not path.is_file():
        errors.append('Missing page: ' + relative)
        continue
    html = path.read_text(encoding='utf-8')
    page = Page(); page.feed(html)
    if page.lang != language: errors.append('Incorrect language: ' + relative)
    for section in ('about', 'research', 'education', 'publications', 'awards', 'contact'):
        if section not in page.ids: errors.append('Missing section: ' + section)
    if html.count('class="publication"') != len(paper_ids): errors.append('Publication count differs from source data: ' + relative)
    for paper_id in paper_ids:
        if 'paper-' + paper_id not in page.ids: errors.append('Missing work: ' + paper_id)
    for link in page.links:
        parsed = urlparse(link)
        if parsed.scheme or parsed.netloc: continue
        if not parsed.path:
            if parsed.fragment and unquote(parsed.fragment) not in page.ids:
                errors.append('Broken anchor: ' + link)
            continue
        target = root / unquote(parsed.path.lstrip('/')) if parsed.path.startswith('/') else path.parent / unquote(parsed.path)
        if target.is_dir(): target = target / 'index.html'
        if not target.is_file(): errors.append('Missing local target: ' + link)
    if re.search(r'(?<!\d)1[3-9](?:[ -]*\d){9}(?!\d)', html):
        errors.append('Unexpected personal phone number in rendered page')
    for marker in ('ICLR 2027', 'AAAI 2027', 'resume.pdf', 'Your Name', '{{', '{%'):
        if marker in html: errors.append('Unexpected source/private/template text: ' + marker)
    for paper in unlinked_manuscripts:
        start=html.find('id="paper-'+paper+'"')
        fragment=html[start:html.find('</article>',start)]
        if '<a ' in fragment: errors.append('Unverified manuscript link: ' + paper)

required = ['assets/files/Sicen_Guo_CV.pdf', 'images/gsc_bio.jpg', 'assets/css/main.css', 'assets/css/custom.css', '404.html', 'sitemap.xml']
for item in required:
    if not (root / item).is_file(): errors.append('Missing artifact: ' + item)
pdfs = list(root.rglob('*.pdf'))
if len(pdfs) != 1: errors.append('Only the public CV PDF may be published')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Passed: bilingual pages, {len(paper_ids)} works each, anchors, local assets, manuscript links and public artifact checks.')
