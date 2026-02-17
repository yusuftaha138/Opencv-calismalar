
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

if face_cascade.empty() or eye_cascade.empty():
    print("Cascade dosyaları yüklenemedi!")
    exit()

vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = vid.read()
    if not ret:
        print("Frame alınamadı")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (480, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=3
        )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_frame, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
