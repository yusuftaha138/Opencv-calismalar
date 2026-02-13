# import cv2
# import numpy as np

# cap = cv2.VideoCapture("C:\\python-gorseller\\car.mp4")
# first_frame = cap.read()
# first_frame = cv2.resize(first_frame, (640, 480))
# first_gray = cv2.cvtColor(first_frame[1], cv2.COLOR_BGR2GRAY)
# first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# while True:
#     frame= cap.read()
#     frame = cv2.resize(frame, (640, 480))
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (5, 5), 0)

#     diff = cv2.absdiff(first_gray, gray)

#     cv2.imshow("frame", frame)
#     cv2.imshow("diff", diff)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\python-gorseller\\car.mp4")

ret, first_frame = cap.read()
if not ret:
    print("Video okunamadı!")
    exit()

first_frame = cv2.resize(first_frame, (640, 480))
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    diff = cv2.absdiff(first_gray, gray)

    cv2.imshow("Frame", frame)
    cv2.imshow("Diff", diff)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

