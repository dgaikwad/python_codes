#!/usr/bin/python3

import cv2
import numpy as np

pic = cv2.imread("my_image.jpg")
rows = pic.shape[1]
cols = pic.shape[0]
print(rows, cols)
center = (cols/2, rows/2)
#if angle is positive then it will rotate image anticlock wise else closckwise
angle = 90
M = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow("Image rotation", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()