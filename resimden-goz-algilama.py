import cv2   

img = cv2.imread("C:\\OpenCv\\test_images\\face.png")

face_cascade = cv2.CascadeClassifier(  cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	gray2 = gray[y:y+h, x:x+w]
	img2 = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(gray2)

	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
	
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()