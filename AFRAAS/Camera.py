import cv2 as cv
import numpy as np
import os


class Camera:
    def __init__(self):
        self.modes = [(0, cv.CAP_DSHOW), (1, None)]
        self.pathToCascade = r"resources\models\haar_face.xml"
        self.pathToRecognizer = r"resources\models\face_trained.yml"

    def connect(self, mode):
        pass

    def getFrame(self):
        pass

    def cropToFace(self):
        pass

    def toGrayScale(self):
        pass
    def saveFrame(self):
        pass
    def addNewFace(self):
        pass
    def updateFace(self):
        pass
    def removeFace(self):
        pass
    