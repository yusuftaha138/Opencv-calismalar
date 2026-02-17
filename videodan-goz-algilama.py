import cv2   

vid = cv2.VideoCapture("C:\\OpenCv\\test_videos\\eye.mp4")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

while True:
    ret, frame = vid.read()
    if not ret:
        break
    frame = cv2.resize(frame,(480,360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_frame = frame[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    cv2.imshow('video',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

