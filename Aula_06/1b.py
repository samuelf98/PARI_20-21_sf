#!/usr/bin/env python
# coding=utf-8


import cv2
import numpy as np

def main():
    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar.png', 1)
    window_name="Imagem Desenho"
    (Linhas,Colunas,z)=np.shape(image_rgb)

    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (Colunas/2, Linhas/2)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (0, 0, 255)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.putText() method
    #Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
    image = cv2.putText(image_rgb, 'PARI', org, font,
                        fontScale, color, thickness, cv2.LINE_AA)

    # Displaying the image
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
if __name__ == "__main__":
    main()
