import cv2 as cv
import os



class Recognizer:
    def __init__(self, cascade=r"resources\models\haar_face.xml", model=r"resources\models\face_trained.yml"):
        self.pathToCascade = cascade
        self.pathToModel = model
        try:
            self.cascade = cv.CascadeClassifier(self.pathToCascade)
            self.model = cv.face.LBPHFaceRecognizer_create()
            self.model.read(model)

        except:
            message = "haar cascade or model is not found on the path provided"
            raise Exception(message)
        
        self.DIR = r'resources\database\persons'
        self.peoples = []

        for i in os.listdir(self.DIR):
            self.peoples.append(i)
        
    def whoIs(self, Face_roi):
        label, confidence = self.model.predict(Face_roi)
        if confidence >= 50:
            return self.peoples[label], confidence
        else:
            return "", False
        
    def cropToFace(self, Frame):
        gray = cv.cvtColor(Frame, cv.COLOR_RGB2GRAY)
        # cv.imshow("testing", gray)
        frame_roi = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        try:
            first_face_indices = frame_roi[0]
            x, y, w, h = first_face_indices
        except:
            return []
        return Frame[y:y+h, x:x+w]
        
    def prepareDataSet(self):
        pass
    def trainRecognizer(self):
        pass
    
       