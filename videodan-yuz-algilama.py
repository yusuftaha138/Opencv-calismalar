import cv2

vid = cv2.VideoCapture("C:\\OpenCv\\test_videos\\faces.mp4")

face_cascade = cv2.CascadeClassifier(  cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while 1:
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()