#!/usr/bin/env python
# coding=utf-8

import cv2
from functools import partial


def onTrackbar1(threshold,dict,window_name,image):
    Bmin=threshold
    dict["Bmin"]=Bmin
    Bmax=dict["Bmax"]
    Gmin=dict["Gmin"]
    Gmax=dict["Gmax"]
    Rmin=dict["Rmin"]
    Rmax=dict["Rmax"]

    BGR_min=(Bmin,Gmin,Rmin)
    BGR_max=(Bmax,Gmax,Rmax)
    mask1 = cv2.inRange(image, BGR_min, BGR_max)

    cv2.imshow(window_name,mask1)



def onTrackbar2(threshold, dict, window_name, image):
    Bmax = threshold
    dict["Bmax"] = Bmax
    Bmin = dict["Bmin"]
    Gmin = dict["Gmin"]
    Gmax = dict["Gmax"]
    Rmin = dict["Rmin"]
    Rmax = dict["Rmax"]

    BGR_min=(Bmin,Gmin,Rmin)
    BGR_max=(Bmax,Gmax,Rmax)
    mask1 = cv2.inRange(image, BGR_min, BGR_max)

    cv2.imshow(window_name, mask1)

def onTrackbar3(threshold, dict, window_name, image):
    Gmin = threshold
    dict["Gmin"] = Gmin
    Bmin = dict["Bmin"]
    Bmax = dict["Bmax"]
    Gmax = dict["Gmax"]
    Rmin = dict["Rmin"]
    Rmax = dict["Rmax"]

    BGR_min=(Bmin,Gmin,Rmin)
    BGR_max=(Bmax,Gmax,Rmax)
    mask1 = cv2.inRange(image, BGR_min, BGR_max)

    cv2.imshow(window_name, mask1)

def onTrackbar4(threshold, dict, window_name, image):
    Gmax = threshold
    dict["Gmax"] = Gmax
    Bmin = dict["Bmin"]
    Bmax = dict["Bmax"]
    Gmin = dict["Gmin"]
    Rmin = dict["Rmin"]
    Rmax = dict["Rmax"]

    BGR_min=(Bmin,Gmin,Rmin)
    BGR_max=(Bmax,Gmax,Rmax)
    mask1 = cv2.inRange(image, BGR_min, BGR_max)

    cv2.imshow(window_name, mask1)


def onTrackbar5(threshold, dict, window_name, image):
    Rmin = threshold
    dict["Rmin"] = Rmin
    Bmin = dict["Bmin"]
    Bmax = dict["Bmax"]
    Gmax = dict["Gmax"]
    Gmin = dict["Gmin"]
    Rmax = dict["Rmax"]

    BGR_min=(Bmin,Gmin,Rmin)
    BGR_max=(Bmax,Gmax,Rmax)
    mask1 = cv2.inRange(image, BGR_min, BGR_max)

    cv2.imshow(window_name, mask1)


def onTrackbar6(threshold, dict, window_name, image):
    Rmax = threshold
    dict["Rmax"] = Rmax
    Bmin = dict["Bmin"]
    Bmax = dict["Bmax"]
    Gmax = dict["Gmax"]
    Rmin = dict["Rmin"]
    Gmin = dict["Gmin"]

    BGR_min=(Bmin,Gmin,Rmin)
    BGR_max=(Bmax,Gmax,Rmax)
    mask1 = cv2.inRange(image, BGR_min, BGR_max)

    cv2.imshow(window_name, mask1)

    return Stringprint(dict)

def Stringprint(dict):
    return (dict)

def main():
    image_rgb = cv2.imread('/home/samuel/PARI_20-21_sf/Aula_05/Imagens/atlas2000_e_atlasmv.png', 1)
    window_name = 'window'
    cv2.namedWindow(window_name)
    dic={"Bmin":0, "Bmax":0,"Gmin":0,"Gmax":0,"Rmin":0,"Rmax":0}
    myonTrackbar1 = partial(onTrackbar1,dict=dic,window_name=window_name,image=image_rgb)
    myonTrackbar2 = partial(onTrackbar2,dict=dic,window_name=window_name,image=image_rgb)
    myonTrackbar3 = partial(onTrackbar3,dict=dic,window_name=window_name,image=image_rgb)
    myonTrackbar4 = partial(onTrackbar4,dict=dic,window_name=window_name,image=image_rgb)
    myonTrackbar5 = partial(onTrackbar5,dict=dic,window_name=window_name,image=image_rgb)
    myonTrackbar6 = partial(onTrackbar6,dict=dic,window_name=window_name,image=image_rgb)


    # Criar trackbar
    cv2.createTrackbar('min B/H', window_name, 0, 255, myonTrackbar1)
    cv2.createTrackbar('max B/H', window_name, 0, 255, myonTrackbar2)
    cv2.createTrackbar('min G/S', window_name, 0, 255, myonTrackbar3)
    cv2.createTrackbar('max G/S', window_name, 0, 255, myonTrackbar4)
    cv2.createTrackbar('min R/V', window_name, 0, 255, myonTrackbar5)
    cv2.createTrackbar('max R/V', window_name, 0, 255, myonTrackbar6)

    cv2.imshow(window_name, image_rgb)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
