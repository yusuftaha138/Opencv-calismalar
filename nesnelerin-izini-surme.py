import cv2
import numpy as np

cap = cv2.VideoCapture(r"C:\python-gorseller\dog.mp4")  

if not cap.isOpened():
    print("Video açılamadı")
    exit()

while True:

    ret, frame = cap.read()

    if not ret or frame is None:
        print("Frame alınamadı / Video bitti")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([179, sensitivity, 255])  # HSV max H=179

    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
