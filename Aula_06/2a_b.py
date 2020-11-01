#!/usr/bin/env python
# coding=utf-8
import cv2

def main():
    # initial setup
    cap = cv2.VideoCapture(0)       # Cap é o objeto ; 0 é a camara default neste caso é a do pc

    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    while True:

        signal, image = cap.read()  # get an image from the camera
        if not signal:          #se não receber sinal desliga - sinal é true ou false
            break
        cv2.imshow(window_name, image)  # Showing the video feed
        key=cv2.waitKey(0)        #Assim tira uma foto cada vez que  carregar numa tecla
        if key ==ord("q"):          #Para parar carrego no q
            break
    cv2.destroyAllWindows()     #Se quiser video coloco waitkey(1)

if __name__ == '__main__':
    main()