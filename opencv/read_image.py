#!/usr/bin/python3

import cv2
img = cv2.imread("my_image.jpeg", 0)
cv2.imshow("Its my first image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

