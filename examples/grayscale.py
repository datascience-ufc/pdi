# coding: utf-8

# https://pillow.readthedocs.io/en/5.2.x/handbook/tutorial.html
# Carregar bibliotecas
from PIL import Image # Módulo de Imagem do Pillow

# Módulo de matemática do python
# sqrt: raíz quadrada
# floor: chão -> menor número inteiro de um float
from math import sqrt, floor

import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def modulo(p):
    """Cálcula o módulo do vetor RGB p (tuplas) e retorna sua intensidade."""
    r, g, b = p
    return sqrt(r ** 2 + g ** 2 + b ** 2)

def grayscale(im):
    """Transforma a imagem im em escala de cinza

    Parameters
    ----------
    im: PIL.Image
        Imagem a ser segmentada.

    Return
    ------
    Um objeto imagem do pillow
    """
    # Acessar a resolução da imagem
    # w -> width -> largura
    # h -> height -> altura
    w, h = im.size
    # Objeto de acesso dos pixels: PixelAccess object
    imcp = im.copy()
    pix = imcp.load()
    for i in range(w):
        for j in range(h):
            p = pix[i, j]
            gray = floor(modulo(p))
            pix[i, j] = (gray, gray, gray)
    return imcp

def segmentation(im, limiar=200):
    """Segmenta a imagem baseado num limiar

    Tudo que estiver abaixo do limiar ficará preto.

    Parameters
    ----------
    im: PIL.Image
        Imagem a ser segmentada.
    limiar: int
        Inteiro para considerar o limiar.

    Return
    ------
    Um objeto imagem do pillow
    """
    w, h = im.size
    # Objeto de acesso dos pixels: PixelAccess object
    imcp = im.copy()
    pix = imcp.load()
    for i in range(w):
        for j in range(h):
            p = pix[i, j]
            gray = floor(modulo(p))
            if gray < limiar:
                pix[i, j] = BLACK
    return imcp


def main():
    fname = "data/flor-de-lotus.jpg"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    # Abrir a imagem
    im = Image.open(fname)
    print("Imagem: ", im.format, im.size, im.mode)

    # Transforma em escalas de cinza
    grayimage = grayscale(im)

    # Segmentação de imagem baseado num limiar mínimo
    # limir € [0, 255]
    limiar = 250
    segimage = segmentation(im, limiar)

    im.show(title="Imagem original")
    grayimage.show(title="Imagem em escalas de cinza")
    segimage.show(title="Imagem segmentada com limiar={}".format(limiar))


if __name__ == '__main__':
    main()
