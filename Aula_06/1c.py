#!/usr/bin/env python
# coding=utf-8

import cv2
from functools import partial
import numpy as np


def click_event(event, x, y, flags, params,imagem,window_name,color):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
    if event==cv2.EVENT_MOUSEMOVE and drawing:
        center_coordinates = (x, y)
        radius = 3
        thickness = -1
        imagem = cv2.circle(imagem, center_coordinates, radius, color, thickness)
        cv2.imshow(window_name, imagem)
    if event== cv2.EVENT_LBUTTONUP:
        drawing=False


def main():
    image_rgb = np.ones((400, 600,3))
    k=None
    window_name = "Imagem Desenho"
    color=(0,0,0)

    while k!=ord('q'):
        # Displaying the image
        cv2.imshow(window_name, image_rgb)
         #Usando o partial, criar uma função auxiliar para colocar a variavel imagem
        p_imagem = partial(click_event,imagem=image_rgb,window_name=window_name,color=color)
        cv2.setMouseCallback(window_name, p_imagem)

        k=cv2.waitKey(0)
        if k==ord('r'):
            color=(0,0,255)
        if k==ord('g'):
            color=(0,255,0)
        if k==ord('b'):
            color=(255,0,0)

if __name__ == "__main__":
    main()
