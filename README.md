# MSK Tours – Website

Tek sayfalık kurumsal tanıtım sitesi. Statik HTML, build adımı yok.

- `index.html` – site (DE birincil, TR ikinci dil; tüm metinler dosyanın sonundaki `I18N` nesnesinde)
- `img/` – web için küçültülmüş görseller ve logo
- `build-embed.py` – tüm görselleri base64 gömerek tek dosyalık `msktours-onizleme.html` üretir (WhatsApp ile paylaşım için): `python build-embed.py`

## İletişim bilgilerini güncelleme
`index.html` içinde `const CONTACT = {...}` bloğu – tek yer.

## Yayın
Depo Netlify/Vercel'e bağlı; `main` dalına push → otomatik yayın. Build command boş, publish directory `/`.

## Yapılacaklar (yayından önce)
- [ ] Impressum sayfası
- [ ] Datenschutzerklärung sayfası
- [ ] E-posta adresi (`CONTACT.email`)
- [ ] Hizmet listesinin firma tarafından onayı
