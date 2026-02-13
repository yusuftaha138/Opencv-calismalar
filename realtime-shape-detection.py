# import cv2
# import numpy as np

# def nothing(x):
#     pass

# cv2.createTrackbar("Lower Hue", "Settings", 0, 179, nothing)
# cv2.createTrackbar("Lower Saturation", "Settings", 0, 255, nothing)
# cv2.createTrackbar("Lower Value", "Settings", 0, 255, nothing)
# cv2.createTrackbar("Upper Hue", "Settings", 0, 179, nothing)
# cv2.createTrackbar("Upper Saturation", "Settings", 0, 255, nothing)
# cv2.createTrackbar("Upper Value", "Settings", 0, 255, nothing)

# font = cv2.FONT_HERSHEY_SIMPLEX

# cap = cv2.VideoCapture(0)
# cv2.namedWindow("Settings")

# while True:
#     ret,frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     Ih=cv2.getTrackbarPos("Lower Hue", "Settings")
#     Is=cv2.getTrackbarPos("Lower Saturation", "Settings")
#     Iv=cv2.getTrackbarPos("Lower Value", "Settings")
#     Uh=cv2.getTrackbarPos("Upper Hue", "Settings")
#     Us=cv2.getTrackbarPos("Upper Saturation", "Settings")
#     Uv=cv2.getTrackbarPos("Upper Value", "Settings")

#     lower = np.array([Ih, Is, Iv])
#     upper = np.array([Uh, Us, Uv])

#     mask = cv2.inRange(frame, lower, upper)

#     cv2.imshow("Frame", frame)
#     cv2.imshow("Mask", mask)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

      #Hata VERDİ yapay zekadan aldığım kod aşağıda


import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Settings")  # ÖNCE pencere

# SONRA trackbarlar
cv2.createTrackbar("Lower Hue", "Settings", 0, 179, nothing)
cv2.createTrackbar("Lower Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Settings", 179, 179, nothing)
cv2.createTrackbar("Upper Saturation", "Settings", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Settings", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)  # Aynalama işlemi

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    Ih = cv2.getTrackbarPos("Lower Hue", "Settings")
    Is = cv2.getTrackbarPos("Lower Saturation", "Settings")
    Iv = cv2.getTrackbarPos("Lower Value", "Settings")
    Uh = cv2.getTrackbarPos("Upper Hue", "Settings")
    Us = cv2.getTrackbarPos("Upper Saturation", "Settings")
    Uv = cv2.getTrackbarPos("Upper Value", "Settings")

    lower = np.array([Ih, Is, Iv])
    upper = np.array([Uh, Us, Uv])

    mask = cv2.inRange(hsv, lower, upper)  # HSV ÜZERİNDE

    kernel = np.ones((5, 5), np.uint8)
    mask= cv2.erode(mask, kernel, iterations=1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    contours= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in contours:
        area = cv2.contourArea(cnt)
        epsilon = 0.02*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        x =approx.ravel()[0]
        y =approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
            elif len(approx) > 4:
                cv2.putText(frame, "Circle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
