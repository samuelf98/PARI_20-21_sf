#!/usr/bin/env python
# coding=utf-8



import argparse
import cv2 as cv

# Global variables
window_name = 'window - Ex3a'
image_gray = None
alpha_slider_max=100

def onTrackbar(threshold):
    alpha = threshold / alpha_slider_max
    beta = (1.0 - alpha)
    dst = cv.addWeighted(image_gray, alpha,image_gray,beta,0.0)
    cv.imshow(window_name, dst)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())
    image = cv.imread(args['image'], cv.IMREAD_COLOR)  # Load an image
    global image_gray # use global var
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)

    cv.namedWindow(window_name)

    trackbar_name = 'Alpha x %d' % alpha_slider_max
    cv.createTrackbar(trackbar_name, window_name, 0, alpha_slider_max, onTrackbar)

if __name__ == '__main__':
    main()

