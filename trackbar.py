import cv2
import numpy as np

def nothing(x):
    pass

canvas = np.zeros((512,512,3),np.uint8) 
img = canvas.copy()
cv2.namedWindow("Trackbar Pencere")

cv2.createTrackbar("B","Trackbar Pencere",0,255,nothing)
cv2.createTrackbar("G","Trackbar Pencere",0,255,nothing)
cv2.createTrackbar("R","Trackbar Pencere",0,255,nothing)
switch = "0 : OFF, 1 : ON"
cv2.createTrackbar(switch, "image",0, 1, nothing)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

    r = cv2.getTrackbarPos("R", "Trackbar Pencere")
    g = cv2.getTrackbarPos("G", "Trackbar Pencere")
    b = cv2.getTrackbarPos("B", "Trackbar Pencere")

    s = cv2.getTrackbarPos(switch, "image")
    if s == 0:
        img[:] = [0,0,0]
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()