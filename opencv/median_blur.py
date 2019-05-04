#!/usr/bin/python3
import numpy as np
import cv2

pic = cv2.imread("my_image.jpg")

kernal = 3
median = cv2.medianBlur(pic, kernal)
cv2.imshow("Original Image", pic)

cv2.imshow("Median Blurred Image", median)



cv2.waitKey(0)
cv2.destroyAllWindows()