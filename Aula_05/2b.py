#!/usr/bin/env python
# coding=utf-8

#Ajuda do prof

import cv2
import numpy as np

def main():

    #Load Image RGB
    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png')

    #Convert RGB to gray
    image_gray=cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)

    #Thresholding - cv2.threshold: Tudo acima de 127 passa a ter o valor de 255
    _, thresh1 = cv2.threshold(image_gray, 127, 150, cv2.THRESH_BINARY)

    print(type(image_gray))
    print(image_gray.shape)
    print(image_gray.dtype)

    #Thresholding usando o nump
    image_np_thresholded=image_gray>128         #Aqui tenho uma matriz boleana
    image_np_thresholded=image_np_thresholded.astype(np.uint8)*255       #astype permite converter todos os pontos da matriz da imagem usadno tb o np converte para 0 e 1
        #np.uint8 permite que os pixeis da matriz  sejam convertidos de boleanos para uint8
        #Assim, o meu pixel (apesar de só ter valores 0 e 1) pode ser convertido em valores entre 0 e 255

    #Display
    window_name= "Imagem Threshold"
    cv2.imshow(window_name,thresh1)
    cv2.waitKey(0)
    #Display com o nump - foi necessário converte-lo
    window_name2= "Imagem Nump"
    cv2.imshow(window_name2,image_np_thresholded)
    cv2.waitKey(0)




if __name__ == '__main__':
    main()
