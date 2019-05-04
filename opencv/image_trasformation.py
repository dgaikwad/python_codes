#!/usr/bin/python3
import cv2
import numpy as np

pic = cv2.imread("my_image.jpg")

cols = pic.shape[1]
rows = pic.shape[0]

#creating 2-d array of float elements.

#left transformation of image
#M = np.float32([[1, 0 , -150], [0, 1, -70]])


#right transformation of image
M = np.float32([[1, 0 , 150], [0, 1, 70]])

shifted = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow("shifted", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()





color = (20, 200, 200)
thickness = 1
