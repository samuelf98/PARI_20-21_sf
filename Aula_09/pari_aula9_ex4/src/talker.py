#!/usr/bin/env python
# coding=utf-8

# Neste exercicio criou-se um ficheiro yaml onde se colocaram os paramateros. Este ficheiro foi colocado dentro da
# pasta msg, logo quando vou correr o comando rosparam load params.yaml, tenho de estar na sua pasta

#Posso ainda colocar todos os parametros existentes no rosparam list num ficheiro fazendo rosparam dump novo_ficheiro.yaml

import rospy
from colorama import Fore
from pari_aula9_ex1.msg import Mensagem_Dog


dog_msg = Mensagem_Dog()
dog_msg.name = 'Bobbi'
dog_msg.age = 7
dog_msg.color = 'Black'
dog_msg.brothers.append('Lassie')  # Adicionar a uma lista

def talker():

    Nome_topico='Conversa'
    frequency=10

    pub = rospy.Publisher(Nome_topico, Mensagem_Dog , queue_size=10)
    rospy.init_node('publisher', anonymous=False)
    rate = rospy.Rate(frequency)


    while not rospy.is_shutdown():
        # Get value of parameter (first i had to make de set of the parame.)
        cor = rospy.get_param('highlight_text_color')      #Como estou a usar um parametro privado( que gravei com o nome publisher) meto o til e assim reconhece esse nome
        hello_str = "Publicar: " + getattr(Fore, cor) + str(dog_msg) + Fore.RESET + " on topic: " +  rospy.remap_name(Nome_topico)      #Altera a string de debug o nome do topico
        rospy.loginfo(hello_str)
        pub.publish(dog_msg)            #Aqui tenho de enviar a minha mensagem do Num que foi criada à parte.
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
