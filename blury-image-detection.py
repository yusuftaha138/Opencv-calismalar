import cv2

img = cv2.imread("C:\\python-gorseller\\starwars.jpg")

blurry_img = cv2.medianBlur(img, 9)

laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var() 
print(laplacian)

# laplacian görüntünün keskinliğini ölçmek için kullanılan bir yöntemdir. Eğer laplacian değeri düşükse, görüntünün bulanık olduğunu gösterebilir. Genellikle, laplacian değeri 1000'in altında ise, görüntünün bulanık olduğu kabul edilir. Ancak, bu eşik değeri görüntüye ve uygulamaya bağlı olarak değişebilir.


if laplacian < 500:
    print("The image is blurry.")





"""
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""