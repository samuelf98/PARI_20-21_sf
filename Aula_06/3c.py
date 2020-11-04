#!/usr/bin/env python
# coding=utf-8

import cv2
import dlib

def edge_detecion(imagem_cinza,imagem_cores):
    imagem3=cv2.Canny(imagem_cinza,30,60)
    #REtr.Tree dá-me todos os contornos, e o chain dá-me todos os pontos
    contours,h=cv2.findContours(imagem3,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imagem_cores,contours,-1,(0,0,255),1)#pintar a vermelho
    return(imagem_cores)

def main():
    #------------Detetar Cara-------------------------------------------#

    #Usar o script para detetar caras
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # To capture video from webcam.
    cap = cv2.VideoCapture(0)


    while True:
        # Read the frame
        _, imagem = cap.read()

        imagem2 = imagem.copy()

        # Con#vert to grayscale
        gray = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        detetor=dlib.get_frontal_face_detector()
        # Draw the rectangle de azul around each face; Limitar a area da cara
        for (x, y, w, h) in faces:
            face_area=w*h
            if face_area>20000:
                #Retangulo azul
                cv2.rectangle(imagem2, (x, y), (x + w, y + h), (255, 0, 0), 2)

                overlay=imagem2.copy()
                #Retangulo pintado a verde
                cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 180, 0), -1)  # A filled rectangle
                alpha = 0.3  # Transparency factor.

                # Following line overlays transparent rectangle over the image
                imagem2 = cv2.addWeighted(overlay, alpha, imagem2, 1 - alpha, 0)

        #---------Deteção de Arestas--------#
        mask=edge_detecion(gray,imagem)

        # if face_area>20000:
        #     # Todos os pontos que o haarscade mme dá. Mas para a boca preciso apenas dos 48
        #     x_lista=[]
        #     y_lista=[]
        #
        #     for n in range(0,landmarks):
        #         x=landmarks.part(n).x
        #         y=landmarks.part(n).y
        #         cv2.circle(imagem2,(x,y),10,(255,0,0),-1)
        #
        #     cv2.imshow("Pontos", imagem2)
        #
        #     for n inrange(48,68):
        #         x = landmarks.part(n).x
        #         y = landmarks.part(n).y
        #         x_lista.append(x)
        #         y_lista.append(y)

        # Display
        cv2.imshow("Original", imagem)
        cv2.imshow('Detetar Caras', imagem2)
        cv2.imshow('Detetar Arestas', mask)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Release the VideoCapture object
    cap.release()

    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
