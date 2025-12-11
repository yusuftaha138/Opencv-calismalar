import cv2
import numpy as np

img = cv2.imread("klon.jpg")
dimensions = img.shape
print(dimensions)  # (yükseklik, genişlik, kanal sayısı)
color = img[420, 500,0] # BGR formatında mavi kanal değeri
print("BGR :",color)

blue = img[420, 500]
print(blue)  # BGR formatında tüm renk kanalları

green = img[420,500,1]


img[420, 500,0] = 250
print("new blue:", img[420, 500,0])

blue1 = img.item(150,200,0)
print("blue1:", blue1)

""""
Videoda girdiği:
img.itemset((150,200,0),175)
print("new blue1:",img[150,200,0])
"""
img[420,500,0] = 175
print("new blue1:",img[150,200,0])



cv2.imshow("Klon Asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()