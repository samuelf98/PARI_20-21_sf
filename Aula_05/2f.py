#!/usr/bin/env python
# coding=utf-8

import cv2

def main():



    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png', 1)

    #Limites para mostrar o caixote
    BGR_min=(0,60,0)
    BGR_max=(50,255,50)
    mask1 = cv2.inRange(image_rgb, BGR_min, BGR_max)


    #Pintar A imagem toda
    imagemadicionada=cv2.add(image_rgb,(50,50,200,0))

    #Display
    window_name = "Imagem Original Pintada"
    cv2.imshow(window_name, imagemadicionada)
    cv2.waitKey(0)

    #Adicionar a máscara (pintar vermelho no caixote À imagem original)
    Imagemadicionada2=image_rgb.copy()      #Tenho de criar uma cópia pelo original por causa das referencias

    cv2.add(image_rgb,(0,0,230,0),dst=Imagemadicionada2,mask=mask1)

    #Preciso de dizer onde vou pintar, neste caso o destino é dst. E vou pintar o que? mask=mask1
    window_name1="Caixote Pintado"
    cv2.imshow(window_name1, Imagemadicionada2)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()