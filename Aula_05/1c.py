#!/usr/bin/env python
# coding=utf-8

import cv2

def main():
    x=0     # Variável responsável por mudar as imagens
    while True:
        if x==0:
            image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar.png'
            x=1
        else:
            image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png'
            x=0

        image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an imaget
        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(3000) # wait for a key press before proceeding - NEste caso ele fecha a janela quando se preissona uma tecla




if __name__ == '__main__':
    main()