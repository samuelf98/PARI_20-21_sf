#!/usr/bin/env python
# coding=utf-8

import cv2
from matplotlib import pyplot as plt

def main():

    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png', 1)
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)

    #Limites para mostrar o caixote - Devia-se usar a window e ver os valores:
    HSV_min=(60,230,80)
    HSV_max=(70,250,105)
    mask1 = cv2.inRange(hsv, HSV_min, HSV_max)


    #Configurar janela para poder ver valores de pixeis
    plt.figure(1)
    plt.imshow(hsv)
    plt.show()

    window_name="Imagem"
    cv2.imshow(window_name, mask1)
    cv2.waitKey(0)





if __name__ == '__main__':
    main()