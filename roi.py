#roi --> region of interest = ilgi alanı

#Görüntü üzerinde belirli bir bölgeyi seçmek ve o bölge üzerinde işlemler yapmak için kullanılır.

import cv2
import numpy as np
img = cv2.imread("klon.jpg")
roi = img[30:200, 200:400]
cv2.imshow("ROI",roi)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()