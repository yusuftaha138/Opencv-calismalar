import cv2
import numpy
import numpy as np
cap = cv2.VideoCapture 

cap = cv2.VideoCapture("C:\\python-gorseller\\hsv.mp4")
circles = []

def mouse(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouse)

while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)
        
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key==27:
        break
    elif key == ord("h"):
        circles =[]

cap.release()
cv2.destroyAllWindows()