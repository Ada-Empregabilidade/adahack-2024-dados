import qrcode
from qrcode.image.styledpil import StyledPilImage


def gera_qrcode(url, path_imagem, path_qrcode):
    """Função que recebe uma url e uma imagem e gera um QRcode personalizado."""
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )  # para poder adicionar uma imagem
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path=path_imagem,
    )

    imagem.save(path_qrcode)

    return None


def main():
    url = str(input('Insira a url: '))
    path_imagem = str(input('Insira a imagem: '))
    path_qrcode = str(input('Insira onde salvar: '))

    gera_qrcode(url, path_imagem, path_qrcode)


if __name__ == '__main__':
    main()
