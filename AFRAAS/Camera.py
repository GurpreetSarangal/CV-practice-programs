import cv2 as cv
import numpy as np
import os


class Camera:
    def __init__(self):
        self.modes = [(0, cv.CAP_DSHOW), (1, None)]
        self.pathToCascade = r"resources\models\haar_face.xml"
        self.pathToRecognizer = r"resources\models\face_trained.yml"
        self.pathToDatabase = r"resources\database\persons"

    def connect(self, mode):
        if mode[1] == None:
            capture = cv.VideoCapture(mode[0])
        else:
            capture = cv.VideoCapture(mode[0], mode[1])
        
        return capture

    def getFrame(self, capture):
        isRead, Frame = capture.read()
        if isRead:
            return Frame
        else:
            return None
        
    def cropToFace(self, Frame):
        haar_cascade = cv.CascadeClassifier(self.pathToCascade)
        gray = self.toGrayScale(Frame)
        frame_roi = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        first_face_indices = frame_roi[0]
        x, y, w, h = first_face_indices
        return Frame[x:x+w, y:y+h]

    def toGrayScale(self, Frame):
        return cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
    
    def saveFrame(self, Frame, path=r"resources\database\persons"):
        
    def addNewFace(self):
        pass
    def updateFace(self):
        pass
    def removeFace(self):
        pass
    