#!/usr/bin/env python
# coding=utf-8


import rospy
from colorama import Fore
from pari_aula9_ex1.msg import Mensagem_Dog


dog_msg = Mensagem_Dog()
dog_msg.name = 'Bobbi'
dog_msg.age = 7
dog_msg.color = 'Black'
dog_msg.brothers.append('Lassie')  # Adicionar a uma lista

    #PAra testar o codigo e alterar o nome do topico ou o no do publicador, no terminal: rosrun pari_aula9_ex1 talker.py Conversa:=Novo_Topico  __name:=New_Publisher_Name

def talker():

    Nome_topico='Conversa'
    frequency=10

    #setup do publicador: as mensagens já n ão são do tipo string, mas do Num (mensagem)
    pub = rospy.Publisher(Nome_topico, Mensagem_Dog , queue_size=10)
    rospy.init_node('publisher', anonymous=True)                    #Posso colocar o anonymous a false, mas depois pode haver colisões de canais. O publisher pode mudar para Samuel
    rate = rospy.Rate(frequency)

    while not rospy.is_shutdown():
        hello_str = "Publicar: " + Fore.RED + str(dog_msg)+ Fore.RESET + " on topic: " + rospy.remap_name(Nome_topico)      #Altera a string de debug o nome do topico
        rospy.loginfo(hello_str)
        pub.publish(dog_msg)            #Aqui tenho de enviar a minha mensagem do Num que foi criada à parte.
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
