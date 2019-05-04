#!/usr/bin/python3


import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype="uint8")
#img = cv2.imread("my_image.jpeg")
color = (250,0, 250)
thickness = 3
cv2.rectangle(pic, (0,0), (500, 150), color, thickness , lineType=8, shift=0)

cv2.imshow("Dark", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()





