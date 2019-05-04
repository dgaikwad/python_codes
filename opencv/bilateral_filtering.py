#!/usr/bin/python3
import numpy as np
import cv2

pic = cv2.imread("my_image.jpg")
cv2.imshow("Original Image", pic)

dimpixel = 7
color = 100
space = 100

filter = cv2.bilateralFilter(pic, dimpixel, color, space)

cv2.imshow("Bilateral filter Image", filter)

cv2.waitKey(0)
cv2.destroyAllWindows()


