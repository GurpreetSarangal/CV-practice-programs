import numpy as np
import cv2 as cv 
import os

haar_cascade = cv.CascadeClassifier('testing_files\haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read(r'testing_files\face_trained.yml')

DIR = r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons'
peoples = []

for i in os.listdir(DIR):
    peoples.append(i)

img = cv.imread(r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\test\irani.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('person', gray)
# cv.waitKey(0)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for(x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"label : {label}, with a confidence of {confidence}")
    cv.putText(img, str(peoples[label]), (x, y+h+30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('detected image', img)
cv.waitKey(0)