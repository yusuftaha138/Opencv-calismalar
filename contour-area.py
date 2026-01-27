import cv2

img = cv2.imread("C:\\python-gorseller\\corner2.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,tresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(
    tresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

# contours,=cv2.findContours(tresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      #hatalı yazdığım 

cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("tresh",tresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

