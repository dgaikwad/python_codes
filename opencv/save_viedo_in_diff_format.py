#!/usr/bin/python3
import cv2
import numpy as np
cap = cv2.VideoCapture("my_video.avi")
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 30
framesize = (720, 480)
out = cv2.VideoWriter("sample_output.avi", fourcc, fps, framesize)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
