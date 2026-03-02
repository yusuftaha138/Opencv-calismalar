from gettext import install
from networkx import center
import pip
import cv2
import numpy as np
import imutils
from sympy import python
import argparse

img = cv2.imread("C:\\OpenCv\\test_images\\tutorial_load_image.jpg")

print("width={}, height={}, depth={}".format(img.shape[1], img.shape[0], img.shape[2]))

# cv2.imshow("resim", img)
# cv2.waitKey(0)


# OpenCV görüntüleri RGB yerine BGR sırasıyla saklar
( B, G, R ) = img[100, 50]
print ( "R={}, G={}, B={}" . format ( R, G, B ))

# roi = img[60:160,320:420]
# cv2.imshow("roi", roi)
# cv2.waitKey(0)

# resized = cv2.resize(img, (200, 200))
# cv2.imshow("resized", resized)
# cv2.waitKey(0)

# r = 300.0 / img.shape[1]
# dim = (300, int(img.shape[0] * r))
# resized = cv2.resize(img, dim)
# cv2.imshow("Aspect Ratio Resize", resized)
# cv2.waitKey(0)

# resized = imutils.resize(img, width=300)
# cv2.imshow("imutils resize", resized)
# cv2.waitKey(0)

# w= img.shape[1]
# h= img.shape[0]
# center = ( w // 2 , h // 2 )
# M = cv2.getRotationMatrix2D ( center , -45 , 1.0 )
# rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
# cv2.imshow("OpenCV Rotation", rotated)
# cv2.waitKey(0)

# blurred = cv2.GaussianBlur(img, (11, 11), 0)
# cv2.imshow("Blurred", blurred)
# cv2.waitKey(0)

output = img.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# Resmin ortasına 20 piksel çapında (içi dolu) mavi bir daire çizin
# x=300,y=150
output = img.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Daire", output)
cv2.waitKey(0)

#kırmızı bir çizgi çiz, çizgi 60,20 noktasından başlayıp 400,200 noktasında bitsin ve kalınlığı 5 piksel olsun
output = img.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# Resmin üzerine yeşil metin çiz

output =img.copy()
cv2.putText( output, "OpenCV + Jurassic Park", (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7 ,(0,255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)


# python opencv_tutorial_01.py 
# width=600, height=322, depth=3
# R=41, G=49, B=37

