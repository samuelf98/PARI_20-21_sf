#!/usr/bin/env python


import rospy
from std_msgs.msg import String
import argparse

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
    pub = rospy.Publisher(Nome_topico, String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(frequency)

    while not rospy.is_shutdown():
        #hello_str = message + " %s" % rospy.get_time()
        hello_str = message + " Topic: " + Nome_topico
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
