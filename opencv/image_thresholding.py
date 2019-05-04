#!/usr/bin/python3

import cv2
import numpy as np

#Reading image in gray color, 0 means gray color

pic = cv2.imread("my_image.jpg", 0)
#if pixel value is greater  then threshold its turn to white(1) else black(0)
threshold = 100


(T_value, binary_threshold) = cv2.threshold(pic, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image using Threshold", binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
