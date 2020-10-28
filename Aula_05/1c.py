#!/usr/bin/env python
# coding=utf-8

import cv2


def main():
    flip_flop = False  # Variável responsável por mudar as imagens
    while True:
        if flip_flop:
            image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar.png'
            flip_flop=False
        else:
            image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png'
            flip_flop=True

        image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an imaget
        cv2.imshow('window', image)  # Display the image
        k= cv2.waitKey(3000)  # wait for a key press before proceeding - NEste caso ele fecha a janela quando se preissona uma tecla

        #Parar programa
        if k==107:
            break

if __name__ == '__main__':
    main()
