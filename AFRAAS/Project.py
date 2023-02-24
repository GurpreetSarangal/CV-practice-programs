from .Camera import Camera
from .Recognizer import Recognizer
import cv2 as cv


class Project:
    def __init__(self):
        
        pass

    def start(self):
        print("start")
        pass

    def intro(self):
        pass

    def registerNewFace(self):
        pass

    def dashboard(self, Frame):
        cv.imshow("video", Frame)
        

    def initiateScanning(self):
        pass
