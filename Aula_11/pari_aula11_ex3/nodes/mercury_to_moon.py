#!/usr/bin/env python


import rospy
import math
import tf
#import geometry_msgs.msg


if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            (trans,rota) = listener.lookupTransform('sol', 'Mercurio', rospy.Time(0))
            (trans1, rota1) = listener.lookupTransform('sol', 'Lua', rospy.Time(0))
            x=trans[0]
            y = trans[1]
            x1=trans1[0]
            y1=trans1[1]
            distance= math.sqrt(math.pow((x-x1),2)+math.pow((y-y1),2))
            rospy.loginfo("The distance from Mars to Moon: " + str(distance))

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()