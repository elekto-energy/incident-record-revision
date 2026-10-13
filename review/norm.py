import re,html,sys,pypdf,json
S='/mnt/user-data/uploads/INCIDENT_RECORD_REVISION/sources/'
def ws(t): return re.sub(r'\s+',' ',t.replace(' ',' ')).strip()
def pdf_pages():
    r=pypdf.PdfReader(S+'OAI-PDF/body.pdf'); return [ws(p.extract_text() or '') for p in r.pages]
def html_text(p):
    s=open(S+p,encoding='utf-8').read()
    s=re.sub(r'<script.*?</script>|<style.*?</style>',' ',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s); return ws(html.unescape(s))
