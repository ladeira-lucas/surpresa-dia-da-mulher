# Surpresa com QR Code

Projeto para criar uma pagina romantica, publicar e gerar um QR Code para abrir no celular.

## 1) Instalar dependencias

```bash
pip install -r requirements.txt
```

## 2) Rodar localmente

```bash
python app.py
```

Site local: `http://127.0.0.1:5000`

## 3) Publicar no Render (gratis)

1. Suba este projeto no GitHub.
2. No Render, clique em **New + > Blueprint** e selecione o repositorio.
3. O Render vai ler o arquivo `render.yaml` automaticamente.
4. Em **Environment**, configure `SITE_LAUNCH_DATE` no formato `YYYY-MM-DD`.

Exemplo para publicar em 8 de marco de 2026:

```text
SITE_LAUNCH_DATE=2026-03-08
```

Com `SITE_TTL_DAYS=5`, o site fica ativo por 5 dias e depois cai sozinho.

## 4) Como funciona a queda automatica

- Variavel `SITE_LAUNCH_DATE`: data de inicio do link.
- Variavel `SITE_TTL_DAYS`: dias no ar (padrao 5).
- Depois do prazo, a pagina principal retorna mensagem de encerramento.

## 5) Gerar o QR Code (apos deploy)

Quando tiver a URL publica do Render, rode:

```bash
python generate_qr.py "https://sua-url-publica.onrender.com" -o qr_namorada.png
```

## Observacoes

- A URL do QR deve ser publica (internet), nao `localhost`.
- O HTML ja inclui `noindex,nofollow` para reduzir indexacao em buscadores.
