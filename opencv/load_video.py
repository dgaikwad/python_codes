#!/usr/bin/python3

import cv2
import numpy as np
cap = cv2.VideoCapture("my_video.avi")

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("vid", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
