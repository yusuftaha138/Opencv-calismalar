import cv2
import numpy as np

img1 = cv2.imread("C:\\python-gorseller\\coins.jpg")

img2 = cv2.imread("C:\\python-gorseller\\balls.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

blur1 = cv2.medianBlur(gray1, 5)
blur2 = cv2.medianBlur(gray2, 5)

circles = cv2.HoughCircles(blur1, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/4, 
param1=200, param2=10, minRadius=20, maxRadius=89)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)
        

# cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()