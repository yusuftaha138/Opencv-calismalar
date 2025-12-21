import cv2
import numpy as np
import os

def main():
    
    kayit_klasoru = "yakalanan_goruntuler"
 
    kamera = cv2.VideoCapture(0)
    print("Kamera başlatıldı.")
    print("Fotoğraf çekmek için 'S' tuşuna basın.")
    print("Çıkış yapmak için 'Q' tuşuna basın.")

   
    mevcut_dosyalar = os.listdir(kayit_klasoru)
    sayac = 1
    
    while True:
       
        ret, cerceve = kamera.read()

        if not ret:
            print("Görüntü alınamadı.")
            break

        cv2.imshow("Kamera (Cekim icin 'S', Cikis icin 'Q')", cerceve)

        tus = cv2.waitKey(5) & 0xFF

       # Burda yapay zekadan yardım aldım.
        if tus == ord('s'):
            dosya_adi = f"{kayit_klasoru}/foto_{sayac}.jpg"
            cv2.imwrite(dosya_adi, cerceve)
            print(f"Kaydedildi: {dosya_adi}")
            sayac += 1 

        elif tus == ord('q'):
            print("Çıkış")
            break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()