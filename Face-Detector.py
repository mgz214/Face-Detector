import cv2
from cvzone.FaceDetectionModule import FaceDetector
import time

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

dec = FaceDetector(minDetectionCon=0.75)

while True:
    success, img = cap.read()

    if success:
        img, boxs = dec.findFaces(img, draw=True)

        
        cv2.imshow("Image", img)
        
        if cv2.waitKey(25) & 0xFF == ord(' '):

            break

cv2.destroyAllWindows()