import cv2 as cv

img = cv.imread('C:\\Users\\DAVASR\\Documents\\AFRAAS_practice\\testing_files\\th.webp')
cv.imshow('face',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('C:\\Users\\DAVASR\\Documents\\AFRAAS_practice\\testing_files\\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print("number of faces found", len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('faces found', img)
cv.waitKey(0)