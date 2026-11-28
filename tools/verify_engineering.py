import re
from pathlib import Path
from html.parser import HTMLParser

class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]
        self.links=[]
        self.lang=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if 'lang' in a:self.lang.append(a['lang'])

source=Path('index.html').read_text()
p=Check();p.feed(source)
assert p.ids.count('engineering')==1
assert '#engineering' in p.links
for slug in ['meu-ritmo','api-studio','imovance','doc-intelligence','flow-engine','pulse-monitor','freight-connect','traincore','meu-ritmo-app','linkpilot']:
    assert any('/JustJao1/'+slug+'/blob/' in a and a.endswith('/docs/engineering-quality.md') for a in p.links),slug
assert 'pt-BR' in p.lang and 'en' in p.lang
assert Path('evidencias/engineering-quality-2026-11-28.md').exists()
for existing in ['work','cases','about','education','contact','themeControl','projectCount']:
    assert existing in p.ids,existing
print('Portfolio structure, bilingual links and evidence record verified')
