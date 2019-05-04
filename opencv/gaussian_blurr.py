#!/usr/bin/python3
import cv2
import numpy as np

pic = cv2.imread("my_image.jpg")
cv2.imshow("Original Image ", pic)
matrix = (7, 7)

blur = cv2.GaussianBlur(pic, matrix, 0)


cv2.imshow("Blurred Image ", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

