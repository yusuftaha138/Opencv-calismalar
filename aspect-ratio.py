import cv2 

def resizewithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = img.shape[:2]

    if width is None and height is None:
        return img

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(img, dim, interpolation=inter)
    return resized

img = cv2.imread("klon.jpg",0)
img1 = resizewithAspectRatio(img, width= None, height=300, inter=cv2.INTER_AREA)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()