import cv2 as cv
import os


# capture = cv.VideoCapture(1)
# while(True):
#     isTrue, frame = capture.read()
#     cv.imshow('droid', frame)
#     if cv.waitKey(2) == ord('e'):
#         break

# capture.release()
# cv.destroyAllWindows()

# img = cv.imread(r"C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons\Phunsuk Wangdu\1.jfif")
# cv.imshow("test",img)
# cv.waitKey(0)
DIR = r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons'
imagePaths = [os.path.join(DIR, f) for f in os.listdir(DIR)]

print(imagePaths)