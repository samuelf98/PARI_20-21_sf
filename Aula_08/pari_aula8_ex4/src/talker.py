#!/usr/bin/env python
# coding=utf-8


import rospy
from colorama import Fore
import argparse
#from dog_lib import Dog

from pari_aula8_ex4.msg import Mensagem_Dog
from pari_aula8_ex5.srv import SetDogName, SetDogNameResponse

dog_msg = Mensagem_Dog()
dog_msg.name = 'Bobbi'
dog_msg.age = 7
dog_msg.color = 'Black'
dog_msg.brothers.append('Lassie')  # Adicionar a uma lista


def callbackfunction(request):
    dog_msg.name=request.new_name       #request é o parÂmetro que o SetDogName.srv vai mandar para alterar com o desejado pelo user
    dog_msg.color=request.color
    #print(request)
    return SetDogNameResponse(True)

def talker():
    ap = argparse.ArgumentParser(description='Definition of a test mode:')
    ap.add_argument('-tn', '--Topic_name', type=str, default="xxx",
                    help='Nome do topico')
    ap.add_argument('-m', '--Message', type=str, default="Hello World!",
                    help=' Full path to json file.')
    ap.add_argument('-f', '--Frequency', type=int, default=10,
                    help=' Choose a frequency.')

    args = vars(ap.parse_args())

    Nome_topico=args['Topic_name']
    message=args['Message']
    frequency=args['Frequency']

    #Create Service: Nome, Ficheiro(srv), função que me vai buscar o primeiro oparÂmetro do Serviço (neste caso:SetDoName o new_name)
    x=rospy.Service("Nome_Servico", SetDogName, callbackfunction)



    #setup do publicador: as mensagens já n ão são do tipo string, mas do Num (mensagem)
    pub = rospy.Publisher(Nome_topico, Mensagem_Dog , queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(frequency)

    # dog =Dog(name='Bobi', age=7, color='Black')
    # dog.addBrother('Lassie')


    while not rospy.is_shutdown():
        hello_str = "Publicar: " + Fore.RED + str(dog_msg)+ Fore.RESET + " on topic: " + Nome_topico
        rospy.loginfo(hello_str)
        pub.publish(dog_msg)            #Aqui tenho de enviar a minha mensagem do Num que foi criada à parte.
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
