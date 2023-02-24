import cv2 as cv
import shutil
import numpy as np
import os
from .Recognizer import Recognizer


class Camera:
    def __init__(self, cam):
        self.AllModes = [(0, cv.CAP_DSHOW), (1, None)]
        self.SelectedMode = self.AllModes[cam]
        self.pathToCascade = r"resources\models\haar_face.xml"
        self.pathToRecognizer = r"resources\models\face_trained.yml"
        self.pathToDatabase = r"resources\database\persons"
        
        

    def connect(self):
        if self.SelectedMode[1] == None:
            capture = cv.VideoCapture(self.SelectedMode[0])
        else:
            capture = cv.VideoCapture(self.SelectedMode[0], self.SelectedMode[1])
        
        self.capture = capture

    def getFrame(self):
        if self.capture == None:
            self.connect()
        
        isRead, Frame = self.capture.read()
        if isRead:
            return Frame
        else:
            return None
        
    
        if (haar_cascade==None):
            haar_cascade = cv.CascadeClassifier(self.pathToCascade)
        gray = self.toGrayScale(Frame)
        frame_roi = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        first_face_indices = frame_roi[0]
        try:
            x, y, w, h = first_face_indices
        except:
            return None
        return Frame[x:x+w, y:y+h]

    def toGrayScale(self, Frame):
        return cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
    
    def saveImg(self, Frame, name,path=r"resources\database\persons"):
        cv.imwrite(f"{name}.jpg", Frame)

    def addNewFace(self, name, path=r"resources\database\persons"):
        try:
            id = len(os.listdir(path)) + 1
        except:
            message = "given path is not found"
            raise Exception(message)

        pathForNewFace = os.path.join(path, str(id) + "_" + name)
        
        # ! check if user is already registered or not
        

        os.mkdir(pathForNewFace)
        haar_cascade = cv.CascadeClassifier(self.pathToCascade)
        # os.chdir(self.pathToDatabase)
        self.connect()
        tempId = 1
        threshold = 0
        try:
            while True:
                if threshold>=30:
                    message = "Person is not in frame"
                    raise Exception(message)
                
                frame = self.getFrame()
                if frame == None:
                    message = "Maybe camera was disconnected"
                    raise Exception(message)

                cv.imshow("Recording You...", frame)        
                face = Recognizer.cropToFace(frame, haar_cascade)

                if(face == None):
                    threshold += 1
                    continue
                
                
                self.saveImg(face, name+"_"+tempId)
                tempId += 1
                if tempId >= 100 or cv.waitKey(20) == ord('e') :
                    break
        except Exception as e:
            shutil.rmtree(pathForNewFace)
            print(e)
        finally:
            cv.destroyAllWindows()
        
    def test_Cam(self):
        self.connect()
        while(True):
            frame = self.getFrame()
            cv.imshow("test", frame)
            rec = Recognizer()
            # rec.cropToFace(frame)
            cropped = rec.cropToFace(frame)
            if cropped != []:
                cv.imshow("face", cropped)
            if cv.waitKey(20) == ord('e'):
                break

    def updateFace(self):
        pass
    def removeFace(self):
        pass
    
    def __del__(self):
        print("Camera object is destroyed")
        cv.destroyAllWindows()
