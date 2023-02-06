import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('testing_files\haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read(r'testing_files\face_trained.yml')

DIR = r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons'
peoples = []

for i in os.listdir(DIR):
    peoples.append(i)

capture = cv.VideoCapture(1)

while(True):
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

    for(x, y, w, h) in faces_rect:

        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        if confidence > 40 :
            

            print(f"label : {peoples[label]}, with a confidence of {confidence}")

            cv.putText(frame, str(peoples[label]), (x, y+h+30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), thickness=2)

        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        
    
    cv.imshow("video", frame)

    if cv.waitKey(30) == ord('e'):
        break
