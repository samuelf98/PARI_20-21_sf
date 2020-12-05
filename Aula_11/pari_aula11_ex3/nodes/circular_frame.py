#!/usr/bin/env python
# coding=utf-8
import math
from math import cos,sin

import cv2
import rospy

# Because of transformations

import tf2_ros
import geometry_msgs.msg
import tf_conversions

if __name__ == '__main__':

    rospy.init_node('Circular_Test')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
    rospy.sleep(0.5)
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = rospy.get_param("~Nome_Principal")

    #Distance,velocity and names of Universe
    velocidade = rospy.get_param("~velocity")*0.001
    raio = rospy.get_param("~ra")
    angulo=0
    t.child_frame_id = rospy.get_param("~Nome_Satelite")
    n_rot=0
    while not rospy.is_shutdown():

        # Coordenadas Polares
        t.transform.translation.x = raio * cos(angulo)  # Polares
        t.transform.translation.y = raio * sin(angulo)
        t.transform.translation.z = 0.0

        #Rotação sobre si mesmo
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, n_rot)           #
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        # Delay para abrandar
        rospy.sleep(0.01)

        t.header.stamp = rospy.Time.now()
        #Send informationw
        br.sendTransform(t)

        angulo+=velocidade

        if angulo>=2*math.pi:
            angulo=0

        n_rot += velocidade*10

        if angulo >= 2 * math.pi:
            angulo = 0
    # Repetir processo
    rospy.spin()
