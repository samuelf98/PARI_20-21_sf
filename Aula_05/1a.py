#!/usr/bin/env python

import cv2

def main():

    image_filename = '/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an imaget

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding - NEste caso ele fecha a janela quando se preissona uma tecla


if __name__ == '__main__':
    main()