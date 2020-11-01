#!/usr/bin/env python
# coding=utf-8
# Igual a 3 mas sem variaveis globais

import cv2
from functools import partial


# A minha função necessita de 3 argumentos de entrada
def onTrackbar(threshold, I_gray, window_name):  # Threshold tem de aparecer primeiro
    _, I_bin = cv2.threshold(I_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, I_bin)


def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        #Este evento dá as coordenadas x,y automaticamente do rato
        print(x, y)



def main():
    window_name = 'window'
    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png', 1)

    I_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow(window_name)
    trackbar_name = 'Threshold'

    # partial fucntiom
    myonTrackbar = partial(onTrackbar, I_gray=I_gray, window_name=window_name)

    cv2.createTrackbar(trackbar_name, window_name, 0, 255, myonTrackbar)

    #Funcionalidade do mouse: vai chamar a função click_event
    cv2.setMouseCallback(window_name, click_event)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
