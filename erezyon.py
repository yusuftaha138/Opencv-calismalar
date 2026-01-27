      #dilation işlemi
# import cv2
# import numpy as np

# img = cv2.imread("C:\\python-gorseller\\klon.jpg",0)

# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel,iterations=3)

# cv2.imshow("img",img)
# cv2.imshow("dilation",dilation)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



        #opening işlemi
# import cv2
# import numpy as np

# img = cv2.imread("C:\\python-gorseller\\klon.jpg",0)

# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel,iterations=3)

# cv2.imshow("img",img)
# cv2.imshow("opening",opening)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


        #closing işlemi
# import cv2
# import numpy as np

# img = cv2.imread("C:\\python-gorseller\\klon.jpg",0)

# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel,iterations=3)

# cv2.imshow("img",img)
# cv2.imshow("closing",closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#         #gradient işlemi

# import cv2
# import numpy as np

# img = cv2.imread("C:\\python-gorseller\\klon.jpg",0)

# kernel = np.ones((5,5),np.uint8)
# gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernel,iterations=3)

# cv2.imshow("img",img)
# cv2.imshow("gradient",gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

        #tophat işlemi
import cv2
import numpy as np

img = cv2.imread("C:\\python-gorseller\\klon.jpg",0)

kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT, kernel,iterations=3)

cv2.imshow("img",img)
cv2.imshow("tophat",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()