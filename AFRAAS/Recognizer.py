import cv2 as cv
from Camera import Camera


class Recognizer:
    def __init__(self, path=r"resources\models\haar_face.xml"):
        self.pathToCascade = path
        try:
            self.cascade = cv.CascadeClassifier(self.pathToCascade)
        except:
            message = "haar cascade file is not found on the path provided"
            raise Exception(message)
        
    def whoIs(self):
        pass
    def cropToFace(self, Frame):
        gray = Camera.toGrayScale(Frame)
        pass
    def prepareDataSet(self):
        pass
    def trainRecognizer(self):
        pass