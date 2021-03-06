#!/usr/bin/env python
# coding=utf-8

import cv2
from matplotlib import pyplot as plt

def main():

    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png', 1)

    # Dividir Canais
    b, g, r = cv2.split(image_rgb)

    _, bt = cv2.threshold(b, 50, 255,cv2.THRESH_BINARY)
    _, gt = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
    _, rt = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY)

    #Limites para mostrar o caixote - Devia-se usar a window e ver os valores:
    BGR_min=(0,60,0)
    BGR_max=(50,255,50)
    mask1 = cv2.inRange(image_rgb, BGR_min, BGR_max)


    #Configurar janela para poder ver valores de pixeis
    plt.figure(1)
    plt.imshow(image_rgb)
    plt.show()

    window_name="Imagem"
    cv2.imshow(window_name, mask1)
    cv2.waitKey(0)





if __name__ == '__main__':
    main()