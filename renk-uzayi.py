import cv2

img=cv2.imread("klon.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("klon BGR", img)
# cv2.imshow("klon RGB", img_rgb)
# cv2.imshow("klon HSV", img_hsv)
cv2.imshow("klon GRAY", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
