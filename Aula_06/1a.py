#!/usr/bin/env python
# coding=utf-8


import cv2
import numpy as np



def main():
    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar.png', 1)
    window_name="Imagem Desenho"
    (Linhas,Colunas,z)=np.shape(image_rgb)

    # Center coordinates
    center_coordinates = ( Colunas/2,Linhas/2)

    # Radius of circle
    radius = 20

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.circle() method
    # Draw a circle with blue line borders of thickness of 2 px
    image = cv2.circle(image_rgb, center_coordinates, radius, color, thickness)

    # Displaying the image
    cv2.imshow(window_name, image)
    #Funcionalidade do mouse: vai chamar a função click_event

    cv2.waitKey(0)
if __name__ == "__main__":
    main()
