import cv2 as cv

capture = cv.VideoCapture(1)
while(True):
    isTrue, frame = capture.read()
    cv.imshow('droid', frame)
    if cv.waitKey(2) == ord('e'):
        break

capture.release()
cv.destroyAllWindows()