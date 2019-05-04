#!/usr/bin/python3


import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype="uint8")
cv2.line(pic, (0,0), (50, 10), (123, 200, 98), 3)

cv2.imshow("Dark", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()





