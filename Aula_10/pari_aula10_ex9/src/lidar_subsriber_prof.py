#!/usr/bin/env python
# coding=utf-8
from math import cos, sin
#import random
from matplotlib import cm

import rospy

from sensor_msgs.msg import LaserScan  # PointCloud2 é o tipo de mensagens

from visualization_msgs.msg import Marker,MarkerArray

# global variables
pub = None
color_r = 1.0
color_b = 0.0
color_g = 0.0


def callback(msg):
    raio=0
    i=0
    c=1
    marker_array = MarkerArray()
    n_color=0
    color_map = cm.tab20(range(0,len(msg.ranges)))                 #Vou criar o colormap com o tamanho do msg.ranges para depois o percorrer
    for r in msg.ranges:  # Vou ver a variação do raio

        raio_inicial = raio
        raio = r

        if abs(raio - raio_inicial) > 1:  # Condição
            global color_r, color_b, color_g
            color_r = color_map[n_color,0]
            color_b = color_map[n_color,1]
            color_g = color_map[n_color,2]
            n_color+=1


        theta = msg.angle_min + i * msg.angle_increment

        x = r * cos(theta)  # r é o raio
        y = r * sin(theta)

        # Marcadores a mudar de cor
        Sphere = Marker()
        Sphere.header.stamp = rospy.Time.now()
        Sphere.header.frame_id = "base_laser_link"
        Sphere.type = Marker.SPHERE
        Sphere.action = Marker.ADD
        Sphere.id=c
        Sphere.ns = "SPHERE"
        Sphere.scale.x = 0.5
        Sphere.scale.y = 0.5
        Sphere.scale.z = 0.5
        Sphere.color.r = color_r
        Sphere.color.g = color_g
        Sphere.color.b = color_b
        Sphere.color.a = 0.3
        Sphere.pose.orientation.w = 1.0
        Sphere.pose.position.x = x
        Sphere.pose.position.y = y
        Sphere.pose.position.z = 0

        marker_array.markers.append(Sphere)
        i += 1
        c+=1

    global pub
    pub.publish(marker_array)




def listener():
    # Initiate node
    rospy.init_node('listener', anonymous=False)

    # Initiate subscriber: o tipo de mensagens é laserscan --------Publishier
    rospy.Subscriber("base_scan", LaserScan, callback)

    global pub
    pub = rospy.Publisher('~publicador', MarkerArray, queue_size=2000)
    rospy.Rate(1)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
