#!/usr/bin/env python
# coding=utf-8

####### Não consegui pôr a trabalhar

import cv2
import numpy as np
from PIL import Image

def main():

    #Imagem em escala de cinzentos
    img = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png', 0)

    img_gray = Image.open('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png').convert('L')
    x=np.asanyarray(img_gray)
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #cv2.imshow('window', img_gray)  # Display the image
    #print(type(im_gray))  # Diz o tipo de variável neste caso numpy.ndarray
    #print(im_gray.shape)  # Nºde linhas por nº de colunas por nº de canais de cor
    #print(im_gray.dtype)  # Tipo de imagem: uint8


    cv2.imshow('window', img)
    cv2.waitKey(0)
    #image_thresholded = np.asanyarray(img_gray) > 128





if __name__ == '__main__':
    main()
