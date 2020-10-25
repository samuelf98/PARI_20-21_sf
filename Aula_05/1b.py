#!/usr/bin/env python

import cv2
import argparse


def main():

    ap = argparse.ArgumentParser(description='Please insert path to file')
    ap.add_argument('-path', '--Path_to_Image', type=str, default=777,
    help='Please type path to file')
    args = vars(ap.parse_args())

    image_filename = args['Path_to_Image']

    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an imaget

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding - NEste caso ele fecha a janela quando se preissona uma tecla

    #PAra imprimir a imagem correr no terminal:Path_to_Image

if __name__ == '__main__':
    main()