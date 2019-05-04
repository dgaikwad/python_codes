#!/usr/bin/python3

import cv2

img = cv2.imread("my_image.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("new_my_image.jpeg", img)

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



