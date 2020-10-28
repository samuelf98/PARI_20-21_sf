#!/usr/bin/env python
# coding=utf-8



import cv2

def main():
    # Load Image
    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlascar2.png')

    # Dividir imagem - Vou colocar em cada uma das variaveis um dos canais de cor
    b, g, r = cv2.split(image_rgb)
    _, bt = cv2.threshold(b, 50, 255,cv2.THRESH_BINARY)  # 255 é o valor que ele colocar se o valor do pixel for maior que 50
    _, gt = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
    _, rt = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY)

    # Existem variaveis silenciosas que é uma variavel, mas  que n é utilizada. Neste caso é o retval que pode ser
    # substituido por _

    # Merge
    newimage = cv2.merge((bt, gt, rt))

    # Display
    mywindo = "IMAGEM"
    cv2.imshow(mywindo, newimage)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
