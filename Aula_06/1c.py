#!/usr/bin/env python
# coding=utf-8

import cv2
from functools import partial
import numpy as np


def click_event(event, x, y, flags, params,imagem,window_name):
        if event == cv2.EVENT_LBUTTONDOWN:
            center_coordinates = (x, y)
            radius = 3
            color = (255, 0, 0)
            thickness = -1
            imagem = cv2.circle(imagem, center_coordinates, radius, color, thickness)
            # print(x,y)
            cv2.imshow(window_name, imagem)



def main():

     image_rgb = np.ones((400, 600,3))

     window_name = "Imagem Desenho"

     # Displaying the image
     cv2.imshow(window_name, image_rgb)


    #Usando o partial, criar uma função auxiliar para colocar a variavel imagem

     p_imagem = partial(click_event,imagem=image_rgb,window_name=window_name)

    #Aqui vou ativar a função partial
     cv2.setMouseCallback(window_name, p_imagem)

     cv2.waitKey(0)

if __name__ == "__main__":
    main()
