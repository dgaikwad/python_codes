#!/usr/bin/python3

import numpy as np
import cv2

pic = cv2.imread("my_image.jpg")
cv2.imshow("Original Image", pic)
thredshold1 = 50
thredshold2 = 100

canny = cv2.Canny(pic, thredshold1, thredshold2)

cv2.imshow("Canny edge Detection Image", canny)
cv2.waitKey(5000)
cv2.destroyAllWindows()


