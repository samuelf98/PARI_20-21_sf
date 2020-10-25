#!/usr/bin/env python
# coding=utf-8

import cv2
import matplotlib.pyplot as plt

def main():
    # image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png'
    # img = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an imaget

    img = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png', 0)
    # Aqui converte a iamgem para escala de cinzentos usando o 0. Se fosse 1 era a cores

    # Só depois de ter a escala de cinzentos é que posso binarizar
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


    #cv2.imshow('window', thresh1)  # Display the image
    #cv2.waitKey(0)  # wait for a key press before proceeding - NEste caso ele fecha a janela quando se preissona uma tecla

    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in xrange(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])                  #Aqui tira os eixos das imagens
    plt.show()

if __name__ == '__main__':
    main()