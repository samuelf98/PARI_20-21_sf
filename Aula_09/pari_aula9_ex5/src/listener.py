#!/usr/bin/env python
# coding=utf-8


import rospy
from colorama import Fore
from pari_aula8_ex4.msg import Mensagem_Dog


def callback(data):
    #cor = rospy.get_param('highlight_text_color')
    cor="BLUE"
    rospy.loginfo('Data Received: ' + getattr(Fore, cor) + str(data) + Fore.RESET + " Topic: " + Nome_topico)


def listener():


    global Nome_topico
    Nome_topico = 'Conversa'

    rospy.init_node('subscriber', anonymous=False)

    rospy.Subscriber(Nome_topico, Mensagem_Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



if __name__ == '__main__':
    listener()
