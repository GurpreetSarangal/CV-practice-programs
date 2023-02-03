import cv2 as cv

capture = cv.VideoCapture(1)
haar_cascade = cv.CascadeClassifier('C:\\Users\\DAVASR\\Documents\\AFRAAS_practice\\testing_files\\haar_face.xml')


while(True):
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

    for(x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
    
    cv.imshow("video", frame)

    if cv.waitKey(1) == ord('e'):
        break

capture.release()
cv.destroyAllWindows()