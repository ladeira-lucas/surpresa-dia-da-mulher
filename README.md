# Surpresa com QR Code (gratis com GitHub Pages)

Projeto para criar uma pagina romantica e abrir via QR Code.

## Publicar gratis no GitHub Pages

1. No GitHub, abra o repositorio `surpresa-dia-da-mulher`.
2. Va em **Settings > Pages**.
3. Em **Build and deployment**, escolha:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
4. Clique em **Save**.
5. Aguarde 1-3 minutos e pegue sua URL publica (exemplo):
   - `https://ladeira-lucas.github.io/surpresa-dia-da-mulher/`

## Expiracao automatica (5 dias)

No arquivo `index.html`, ajuste estes valores se quiser:

```js
const SITE_LAUNCH_DATE = "2026-03-08";
const SITE_TTL_DAYS = 5;
```

Apos o periodo, a pagina mostra automaticamente a mensagem de encerramento.

## Gerar o QR Code final

Quando tiver a URL publica, rode:

```bash
python generate_qr.py "https://ladeira-lucas.github.io/surpresa-dia-da-mulher/" -o qr_namorada.png
```

## Desenvolvimento local (opcional)

- Versao Flask: `python app.py`
- Versao GitHub Pages: abrir `index.html` no navegador
