#!/usr/bin/env python
# coding=utf-8

from math import cos,sin, pi

import rospy
# Because of transformations


import tf2_ros
import geometry_msgs.msg



#The moon dosn't rotate around the earth (how to do it)

if __name__ == '__main__':

    rospy.init_node('Circular_Test')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "sol"
    t.child_frame_id = "child_name"

    # Coordenadas Polares
    raio = 3
    angulo=0
    while not rospy.is_shutdown():
        t.transform.translation.x = raio * cos(angulo)  # Polares
        t.transform.translation.y = raio * sin(angulo)
        t.transform.translation.z = 0.0
        #q = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        t.transform.rotation.x = 0
        t.transform.rotation.y = 0
        t.transform.rotation.z = 0
        t.transform.rotation.w = 1
        rospy.loginfo(str(t.transform.translation.x) + ", " + str(t.transform.translation.y))

        # Nova transformação com novo carimbo de tempo
        t.header.stamp = rospy.Time.now()
        #Send informationw
        br.sendTransform(t)

        angulo+=0.001
        if angulo>2*pi:
            angulo=0

    rospy.spin()
