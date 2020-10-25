#!/usr/bin/env python
# coding=utf-8

import cv2

from matplotlib.pyplot import imshow


def main():
    # image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png'
    # img = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an imaget

    img = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png', 1)
    # Aqui converte a iamgem para escala de cinzentos usando o 0. Se fosse 1 era a cores

    cv2.imshow('IMAGEM', img)
    cv2.waitKey(0)



if __name__ == '__main__':
    main()