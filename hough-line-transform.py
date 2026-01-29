# import cv2 
# import numpy as np

# img = cv2.imread("C:\\python-gorseller\\h_line.png")

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# edges = cv2.Canny(gray,50,150) #canny ile kenarları tespti ediyoruz

# lines = cv2.HoughLinesP(
#     img,
#     rho=1,
#     theta=np.pi/180,
#     threshold=100,
#     minLineLength=50,
#     maxLineGap=10)

# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imshow("img",img)
# cv2.imshow("edges",edges)
# cv2.imshow("gray",gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

    #Hata verdi güncel chatgptden aldığım kod aşağıda

import cv2 
import numpy as np

img = cv2.imread("C:\\python-gorseller\\h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

lines = cv2.HoughLinesP(
    edges,
    rho=1,
    theta=np.pi/180,
    threshold=100,
    minLineLength=50,
    maxLineGap=200
)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("img", img)
cv2.imshow("edges", edges)
cv2.imshow("gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

