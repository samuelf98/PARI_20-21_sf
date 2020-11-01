#!/usr/bin/env python
# coding=utf-8

import cv2



def main():
    #Usar o script para detetar caras
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)


    while True:
        # Read the frame
        _, imagem = cap.read()

        imagem2 = imagem.copy()

        # Convert to grayscale
        gray = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle de azul around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(imagem2, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display
        cv2.imshow("Original", imagem)
        cv2.imshow('Detetar Caras', imagem2)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Release the VideoCapture object
    cap.release()

    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
