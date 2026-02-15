import cv2 
import numpy as np

path1 = "C:\\python-gorseller\\aircraft.jpg"

path2 = "C:\\python-gorseller\\aircraft(1).jpg"

img1 = cv2.imread(path1)
img1 = cv2.resize(img1, (640, 550))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2, (640, 550))

img3 = cv2.medianBlur(img1,7)

# if img1.shape == img2.shape:
#     print("Same size.")
# else:
#     print("Different size.")

diff = cv2.subtract(img1, img3)
b,g,r = cv2.split(diff)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("The images are the same.")
else:
    print("The images are different.")



cv2.imshow("Difference", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()