import cv2

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()