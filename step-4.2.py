import cv2
import numpy as np
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray= cv2.GaussianBlur(gray, (3,3), 0)
edged = cv2.Canny(gray, 20, 100)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

if len (cnts)>0:
    c = max (cnts,key=cv2.contourArea)
    msak = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(msak, [c], -1, 255, -1)

    (x,y,w,h) = cv2.boundingRect(c)
    imgROI= img[y:y+h, x:x+w]
    maskROI = msak[y:y+h, x:x+w]
    imgROI = cv2.bitwise_and(imgROI, imgROI, mask=maskROI)

for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate(imgROI, angle)
		cv2.imshow("Rotated (Problematic)", rotated)
		cv2.waitKey(0)
for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate_bound(imgROI, angle)
		cv2.imshow("Rotated (Correct)", rotated)
		cv2.waitKey(0)