# import numpy as np
# import cv2

# source = cv2.imread("C:\\OpenCv\\test_images\\source.jpg")
# target = cv2.imread("C:\\OpenCv\\test_images\\target.jpg")
# transfer = cv2.imread("C:\\OpenCv\\test_images\\transfer.jpg")

# def color_transfer(source, target):
#     source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
#     target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

#     (lMeanSrc, aMeanSrc, bMeanSrc) = cv2.mean(source)[:3]
#     (lMeanTar, aMeanTar, bMeanTar) = cv2.mean(target)[:3]

#     (lStdSrc, aStdSrc, bStdSrc) = (source[..., 0].std(), source[..., 1].std(), source[..., 2].std())
#     (lStdTar, aStdTar, bStdTar) = (target[..., 0].std(), target[..., 1].std(), target[..., 2].std())

#     l = ((target[..., 0] - lMeanTar) * (lStdSrc / lStdTar)) + lMeanSrc
#     a = ((target[..., 1] - aMeanTar) * (aStdSrc / aStdTar)) + aMeanSrc
#     b = ((target[..., 2] - bMeanTar) * (bStdSrc / bStdTar)) + bMeanSrc

#     transfer = cv2.merge([l, a, b])
#     transfer = np.clip(transfer, 0, 255).astype("uint8")
#     transfer = cv2.cvtColor(transfer, cv2.COLOR_LAB2BGR)

#     return transfer

# def image_stats(image):
#     (l, a, b) = cv2.split(image)
#     lMean, lStd = (l.mean(), l.std())
#     aMean, aStd = (a.mean(), a.std())
#     bMean, bStd = (b.mean(), b.std())
#     return (lMean, lStd, aMean, aStd, bMean, bStd)

import numpy as np
import cv2

# Kaynak ve hedef görseller
source = cv2.imread(r"C:\OpenCv\test_images\source.jpg")
target = cv2.imread(r"C:\OpenCv\test_images\target.jpg")

# Dosyalar okunabildi mi kontrol
if source is None:
    print("Source dosyası okunamadı!")
if target is None:
    print("Target dosyası okunamadı!")

# Renk transfer fonksiyonu
def color_transfer(source, target):
    source_lab = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
    target_lab = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

    (lMeanSrc, aMeanSrc, bMeanSrc) = cv2.mean(source_lab)[:3]
    (lMeanTar, aMeanTar, bMeanTar) = cv2.mean(target_lab)[:3]

    (lStdSrc, aStdSrc, bStdSrc) = (source_lab[...,0].std(), source_lab[...,1].std(), source_lab[...,2].std())
    (lStdTar, aStdTar, bStdTar) = (target_lab[...,0].std(), target_lab[...,1].std(), target_lab[...,2].std())

    l = ((target_lab[...,0] - lMeanTar) * (lStdSrc / lStdTar)) + lMeanSrc
    a = ((target_lab[...,1] - aMeanTar) * (aStdSrc / aStdTar)) + aMeanSrc
    b = ((target_lab[...,2] - bMeanTar) * (bStdSrc / bStdTar)) + bMeanSrc

    transfer_lab = cv2.merge([l, a, b])
    transfer_lab = np.clip(transfer_lab, 0, 255).astype("uint8")
    transfer_bgr = cv2.cvtColor(transfer_lab, cv2.COLOR_LAB2BGR)

    return transfer_bgr

# Fonksiyonu çağır ve transfer uygula
result = color_transfer(source, target)

# Sonucu göster
cv2.imshow("Source", source)
cv2.imshow("Target", target)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sonucu kaydetmek istersen
cv2.imwrite(r"C:\OpenCv\test_images\result.jpg", result)


# Bu dosyayı çalıştıramadım chatgptden kod aldım onlar da çalışmadı.