#!/usr/bin/python3


import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype="uint8")
color = (250,0, 250)

radius = 100
cv2.circle(pic, (100, 100), radius, color)

cv2.imshow("Dark", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()







