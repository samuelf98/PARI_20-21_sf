#!/usr/bin/env python
# coding=utf-8

import cv2
import matplotlib.pyplot as plt

def main():
    image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png'
    img = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an imaget

    RED,GREEN,BLUE=cv2.split(img)
    ret, BLUE = cv2.threshold(BLUE, 50, 50, cv2.THRESH_BINARY)
    ret, GREEN = cv2.threshold(GREEN, 100, 100, cv2.THRESH_BINARY)
    ret, RED = cv2.threshold(RED, 150, 150, cv2.THRESH_BINARY)
    MERGE = cv2.merge((RED,GREEN,BLUE))
    ZERO = img

    titles = ['Original Image', 'BLUE', 'GREEN', 'RED', 'MERGE','ZERO']
    images = [img, BLUE, GREEN, RED, MERGE, ZERO]

    for i in xrange(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])                  #Aqui tira os eixos das imagens
    plt.show()

    cv2.imshow('window', MERGE)  # Display the image
    cv2.waitKey(0)  # wait for a key press before proceeding - NEste caso ele fecha a janela quando se preissona uma tecla

if __name__ == '__main__':
    main()