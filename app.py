import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from flask import Flask, render_template

app = Flask(__name__)
TZ = ZoneInfo("America/Manaus")

SURPRESA = {
    "titulo": "Feliz Dia da Mulher, meu amor",
    "subtitulo": "Hoje e sempre, celebro sua forca, sua luz e o amor que voce espalha.",
    "frase_destaque": (
        "Voce e a mulher mais incrivel que eu conheco. "
        "Obrigado por ser meu porto seguro, meu riso favorito e meu maior orgulho."
    ),
    "motivos": [
        "Seu sorriso ilumina qualquer lugar.",
        "Sua coragem me inspira todos os dias.",
        "Seu carinho faz eu me sentir em casa.",
        "Com voce, cada momento vira memoria inesquecivel.",
    ],
    "fotos": [
        {
            "arquivo": "images/1.jpeg",
            "titulo": "Aldeia e Polaroide",
            "texto": "Nesse dia na aldeia, a polaroide guardou mais que uma foto: guardou o comeco de uma memoria que sempre me faz sorrir.",
        },
        {
            "arquivo": "images/2.jpeg",
            "titulo": "Primeiro encontro especial",
            "texto": "Nosso primeiro jantar mais chique, com massa na mesa e aquele friozinho bom de quem ja sentia que estava vivendo algo raro.",
        },
        {
            "arquivo": "images/3.jpg",
            "titulo": "No barco, rumo a aventura",
            "texto": "No meio do rio, eu olhava a paisagem e pensava que a melhor vista era voce do meu lado, rindo comigo.",
        },
        {
            "arquivo": "images/4.jpeg",
            "titulo": "Aniversario da sua amiga",
            "texto": "No aniversario da sua amiga, a gente estava tao em sintonia que parecia cena de filme: leve, bonita e nossa.",
        },
        {
            "arquivo": "images/5.jpeg",
            "titulo": "Seu aniversario",
            "texto": "No seu aniversario, eu so conseguia agradecer por existir uma mulher tao forte, doce e incrivel como voce.",
        },
        {
            "arquivo": "images/6.jpeg",
            "titulo": "Shopping e risadas",
            "texto": "No shopping, brincando com oculos da loja e provando que os melhores momentos sao os espontaneos que a gente inventa juntos.",
        },
        {
            "arquivo": "images/7.jpeg",
            "titulo": "Porao do Alemao",
            "texto": "A caminho do Porao do Alemao, com clima de rock e coracao tranquilo, porque qualquer role com voce ja vira lembranca favorita.",
        },
        {
            "arquivo": "images/8.jpeg",
            "titulo": "Nosso momento aleatorio",
            "texto": "Essa foto sem roteiro e a nossa cara: simples, verdadeira e cheia daquele carinho que aparece ate no silencio.",
        },
        {
            "arquivo": "images/9.jpeg",
            "titulo": "Partiu pagode",
            "texto": "Indo pro pagode, com sorriso no rosto e a certeza de que a melhor parte da noite sempre e dividir tudo com voce.",
        },
        {
            "arquivo": "images/10.jpeg",
            "titulo": "Nosso Natal",
            "texto": "No Natal, entre luzes e abracos, eu senti de novo que meu presente preferido e construir uma vida ao seu lado.",
        },
        {
            "arquivo": "images/11.jpeg",
            "titulo": "Dia dos Namorados",
            "texto": "Na nossa comemoracao de Dia dos Namorados, o amor estava no olhar, no toque e no jeito que a gente se escolhe todos os dias.",
        },
    ],
    "mensagem_final": (
        "Feliz Dia da Mulher, minha princesa. "
        "Que eu sempre saiba te amar, te cuidar e te fazer sorrir."
    ),
}


def _get_date_from_env(var_name: str):
    raw = os.getenv(var_name, "").strip()
    if not raw:
        return None
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return None


def get_site_status():
    launch_date = _get_date_from_env("SITE_LAUNCH_DATE")
    ttl_days_raw = os.getenv("SITE_TTL_DAYS", "5").strip()

    try:
        ttl_days = max(1, int(ttl_days_raw))
    except ValueError:
        ttl_days = 5

    # Sem data de inicio configurada, o site permanece ativo.
    if launch_date is None:
        return {"active": True, "expires_on": None}

    expires_on = launch_date + timedelta(days=ttl_days - 1)
    today = datetime.now(TZ).date()
    return {
        "active": today <= expires_on,
        "expires_on": expires_on.strftime("%d/%m/%Y"),
    }


@app.route("/")
def home():
    status = get_site_status()
    if not status["active"]:
        return render_template("expired.html", expires_on=status["expires_on"]), 410
    return render_template("index.html", surpresa=SURPRESA)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
