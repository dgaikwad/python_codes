#!/usr/bin/python3


import numpy as np
import cv2
pic = np.zeros((1000,1000,3), dtype="uint8")
font = cv2.FONT_HERSHEY_DUPLEX
color = (20, 200, 200)
thickness = 1
cv2.putText(pic, "India", (100,100), font, 3, color, thickness )

cv2.imshow("Dark", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()







