import cv2
import numpy as np

img = cv2.imread("C:\\python-gorseller\\klon.jpg",0)

row,col = img.shape
# print(row)
# print(col)

M = np.float32([[1,0,250],[0,1,250]])


dst = cv2.warpAffine(img,M,(col,row))


cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()