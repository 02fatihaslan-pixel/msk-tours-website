# index.html içindeki img/... referanslarını base64 olarak gömer -> msktours-onizleme.html
import base64, re, os, mimetypes
src = open('index.html', encoding='utf-8').read()
def embed(m):
    path = m.group(1)
    if not os.path.exists(path): return m.group(0)
    mime = mimetypes.guess_type(path)[0] or 'application/octet-stream'
    data = base64.b64encode(open(path,'rb').read()).decode()
    return f'data:{mime};base64,{data}'
out = re.sub(r'(img/[A-Za-z0-9_.-]+)', embed, src)
open('msktours-onizleme.html','w',encoding='utf-8').write(out)
print(len(src)//1024, 'KB ->', len(out)//1024, 'KB')
