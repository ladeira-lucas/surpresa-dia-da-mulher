import argparse
from pathlib import Path

import qrcode


def gerar_qrcode(url: str, saida: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    caminho = Path(saida)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    img.save(caminho)
    print(f"QR Code salvo em: {caminho.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera um QR Code para abrir a pagina surpresa."
    )
    parser.add_argument("url", help="URL que sera aberta ao escanear o QR Code")
    parser.add_argument(
        "-o",
        "--output",
        default="qrcode_surpresa.png",
        help="Arquivo de saida (padrao: qrcode_surpresa.png)",
    )
    args = parser.parse_args()

    gerar_qrcode(args.url, args.output)


if __name__ == "__main__":
    main()
