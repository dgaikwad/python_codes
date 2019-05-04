#!/usr/bin/python3
import numpy as np
import cv2
pic = np.zeros((1000,1000,3), dtype="uint8")
color = (20, 200, 200)
thickness = 1
radius =100
cv2.rectangle(pic, (100,100), (500, 500), color, thickness)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, "India", (100,100), font, 3, color, thickness )
cv2.circle(pic, (150,150), radius, thickness)
cv2.line(pic, (110,200), (300,700), color)

cv2.imshow("ALL COMBINATION...", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()







