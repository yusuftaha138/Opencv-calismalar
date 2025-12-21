import cv2
import numpy as np


def bos_fonksiyon(x):
    pass

def main():
  
    kamera = cv2.VideoCapture(0)

    cv2.namedWindow("Ayarlar")
    cv2.resizeWindow("Ayarlar", 640, 240)
    
    cv2.createTrackbar("Alt-H", "Ayarlar", 100, 179, bos_fonksiyon)
    cv2.createTrackbar("Alt-S", "Ayarlar", 150, 255, bos_fonksiyon)
    cv2.createTrackbar("Alt-V", "Ayarlar", 0, 255, bos_fonksiyon)
    
    cv2.createTrackbar("Ust-H", "Ayarlar", 140, 179, bos_fonksiyon)
    cv2.createTrackbar("Ust-S", "Ayarlar", 255, 255, bos_fonksiyon)
    cv2.createTrackbar("Ust-V", "Ayarlar", 255, 255, bos_fonksiyon)

    print("Renk takibi başlatıldı. Çıkış için 'Q' tuşuna basın.")

    while True:
        ret, cerceve = kamera.read()
        if not ret:
            break

        hsv_format = cv2.cvtColor(cerceve, cv2.COLOR_BGR2HSV)

        alt_h = cv2.getTrackbarPos("Alt-H", "Ayarlar")
        alt_s = cv2.getTrackbarPos("Alt-S", "Ayarlar")
        alt_v = cv2.getTrackbarPos("Alt-V", "Ayarlar")
        ust_h = cv2.getTrackbarPos("Ust-H", "Ayarlar")
        ust_s = cv2.getTrackbarPos("Ust-S", "Ayarlar")
        ust_v = cv2.getTrackbarPos("Ust-V", "Ayarlar")

        alt_sinir = np.array([alt_h, alt_s, alt_v])
        ust_sinir = np.array([ust_h, ust_s, ust_v])
        maske = cv2.inRange(hsv_format, alt_sinir, ust_sinir)

        maske = cv2.erode(maske, None, iterations=2)
        maske = cv2.dilate(maske, None, iterations=2)

        konturlar, _ = cv2.findContours(maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(konturlar) > 0:
            
            en_buyuk_kontur = max(konturlar, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(en_buyuk_kontur)
            
           
            cv2.rectangle(cerceve, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(cerceve, "Nesne", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Maske (Siyah-Beyaz)", maske)
        cv2.imshow("Renk Takibi", cerceve)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()