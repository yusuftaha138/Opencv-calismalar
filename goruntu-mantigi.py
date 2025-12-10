import cv2
import numpy as np

# 10x10 siyah bir görüntü (3 kanal, uint8)
img = np.zeros((10, 10, 3), dtype=np.uint8)

img[0,0] = 255
img[0,1] = 200
img [0,2] = 100
img [0,3] = 15

"""
img[0,0] = (255,255,255)  # Pikseli beyaza ayarla
img[0,1] = (255,255,200)
img [0,2] = (255,255,100)
img [0,3] = (255,255,15)
"""
# Doğru çağrı: interpolation parametresi fonksiyon çağrısının içinde olmalı
img = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_AREA)

cv2.imshow("Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()