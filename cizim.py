import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255
# print(canvas) # Beyaz bir tuval oluşturur

cv2.line(canvas, (50,50), (512,512), (255,0,0),5) # Mavi çizgi


cv2.line(canvas, (100,150), (200,250), (0,0,255),thickness=7) # Kırmızı çizgi

cv2.rectangle(canvas, (20,20), (50,50), (0,255,0),thickness = 3)   

cv2.rectangle(canvas, (50,50), (150,150), (0,255,0), thickness=25)

cv2.circle(canvas, (300,300), 50, (255,0,255), thickness=-1)

# Kendi düşündüğüm yöntemle üçgen çizimi:
# cv2.line(canvas, (400,100), (500,50), (0,0,0), thickness=3)
# cv2.line(canvas, (500,50), (400,200), (0,0,0), thickness=3)
# cv2.line(canvas, (400,200), (400,100), (0,0,0), thickness=3)

# Üçgen çizimi GÖSTERİLEN yöntem

p1 = (100,200)
p2 = (50,50)
p3 = (300,100)

cv2.line(canvas, p1, p2, (0,0,0), 3)
cv2.line(canvas, p2, p3, (0,0,0), 3)
cv2.line(canvas, p3, p1, (0,0,0), 3)

points = np.array([[130,200],[330,250],[100,100]], np.int32)

cv2.polylines(canvas, [points], isClosed=True, color=(255,0,0), thickness=2)

cv2.ellipse(canvas, (400,400), (75,25), 50,0,360, (0,255,255), thickness=-1)





cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

