#!/usr/bin/env python
# coding=utf-8

import cv2

# Global variables

window_name = 'window'


def onTrackbar(threshold):
    _, I_thre=cv2.threshold(I_gray,threshold,255,cv2.THRESH_BINARY)
    cv2.imshow(window_name,I_thre)

def main():

    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png',1)

    global I_gray
    I_gray=cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)


    cv2.namedWindow(window_name)

    trackbar_name='Threshold'

    #Criar trackbar : nome,nome janela,ponto inicial da trackbar,max,função
    cv2.createTrackbar(trackbar_name,window_name,0,255,onTrackbar)

    #Aqui serve para a barra começar nos 128
    onTrackbar(128)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()