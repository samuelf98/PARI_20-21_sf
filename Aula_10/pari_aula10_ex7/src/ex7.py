#!/usr/bin/env python
# coding=utf-8

import cv2
from cv_bridge import CvBridge
import rospy

from sensor_msgs.msg import Image


def main():
    # -----------------Câmara e Conversao para rviz------------------------------------------

    cap = cv2.VideoCapture(0)  # Cap é o objeto ; 0 é a camara default neste caso é a do pc
    bridge = CvBridge()

    window_name = 'Camara'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    Nome_topico = 'Conversa'
    frequency = 10
    pub = rospy.Publisher(Nome_topico, Image)
    rospy.init_node('publisher', anonymous=False)
    rate = rospy.Rate(frequency)

    while not rospy.is_shutdown():

        signal, image = cap.read()  # get an image from the camera

        if not signal:  # se não receber sinal desliga - sinal é true ou false
            break
        cv2.imshow(window_name, image)  # Showing the video feed
        image2=bridge.cv2_to_imgmsg(image, "bgr8")         #Converter bgr image to rviz
        key = cv2.waitKey(1)  # Assim tira uma foto cada vez que  carregar numa tecla

        if key == ord("q"):  # Para parar carrego no q
            break

        # --------------Configurar Mensagem--------------------

        rospy.loginfo("Estou a escrever:")
        pub.publish(image2)  # Aqui tenho de enviar a minha mensagem do Num que foi criada à parte.
        rate.sleep()
        print ("0")
    cv2.destroyAllWindows()  # Se quiser video coloco waitkey(1)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
