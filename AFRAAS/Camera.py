import cv2 as cv
import shutil
import numpy as np
import os
from .Recognizer import Recognizer


class Camera:
    def __init__(self, cam):
        self.AllModes = [(0, cv.CAP_DSHOW), (1, None)]
        self.SelectedMode = self.AllModes[cam]
        self.pathToCascade = r"AFRAAS\resources\models\haar_face.xml"
        self.pathToRecognizer = r"AFRAAS\resources\models\face_trained.yml"
        self.pathToDatabase = r"AFRAAS\resources\database\persons"
        if cam==1:
            self.capture = cv.VideoCapture(self.SelectedMode[0])
        else:
            self.capture = cv.VideoCapture(self.SelectedMode[0], self.SelectedMode[1])
        
        
        
        
        

    def connect(self):
        if self.SelectedMode[1] == None:
            capture = cv.VideoCapture(self.SelectedMode[0])
        else:
            capture = cv.VideoCapture(self.SelectedMode[0], self.SelectedMode[1])
        
        return capture

    def getFrame(self):
        isRead, Frame = self.capture.read()
        return Frame
        
        
    
        

    def toGrayScale(self, Frame):
        return cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
    
    def saveImg(self, Frame, name):

        cv.imwrite(f"{name}.jpg", Frame)

    def addNewFace(self, name):
        try:
            id = len(os.listdir(self.pathToDatabase)) + 1
        except:
            message = "given path is not found"
            raise Exception(message)

        pathForNewFace = os.path.join(self.pathToDatabase, str(id) + "_" + name)
        
        # ! check if user is already registered or not
        

        os.mkdir(pathForNewFace)
        haar_cascade = cv.CascadeClassifier(self.pathToCascade)
        # os.chdir(self.pathToDatabase)
        # self.connect()
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
        # self.connect()
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
    
    def mark(self, Frame, label, x, y, w, h):
        cv.putText(Frame, str(label), (x, y+h+30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), thickness=2)
        cv.rectangle(Frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
    def __del__(self):      
        self.capture.release()
        cv.destroyAllWindows()
