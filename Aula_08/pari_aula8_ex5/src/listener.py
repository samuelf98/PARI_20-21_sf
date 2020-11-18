#!/usr/bin/env python


import rospy
import argparse
#from std_msgs.msg import String
from pari_aula8_ex4.msg import Dog

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'Data Received %s', data.data)
    rospy.loginfo('Data Received: %s' + str(data) + " Topic: " + Nome_topico)
def listener():

    ap = argparse.ArgumentParser(description='Definition of a test mode:')
    ap.add_argument('-tn', '--Topic_name', type=str, default="xxx",
                    help='Nome do topico')

    args = vars(ap.parse_args())
    global Nome_topico
    Nome_topico=args['Topic_name']

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber(Nome_topico, Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
