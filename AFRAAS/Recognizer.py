import cv2 as cv
import numpy as np
import os



class Recognizer:
    def __init__(self, 
                cascade=r"AFRAAS\resources\models\haar_face.xml", 
                model=r"AFRAAS\resources\models\face_trained.yml"):
        self.pathToCascade = cascade
        self.pathToModel = model
        self.pathToLabels = r"AFRAAS\resources\models\labels.npy"
        self.pathToFeatures = r"AFRAAS\resources\models\features.npy"
        try:
            self.cascade = cv.CascadeClassifier(self.pathToCascade)
            self.model = cv.face.LBPHFaceRecognizer_create()
            self.model.read(model)

            l = np.load(self.pathToLabels)
            self.labels = l.tolist()

            f = np.load(self.pathToFeatures, allow_pickle=True)
            self.features = f.tolist()

        except:
            message = "haar cascade or model is not found on the path provided"
            raise Exception(message)
        
        self.DIR = r'AFRAAS\resources\database\persons'
        self.people = []

        for i in os.listdir(self.DIR):
            self.people.append(i)
        
    def whoIs(self, Face_roi):
        Face_roi = cv.cvtColor(Face_roi, cv.COLOR_BGR2GRAY)
        label, confidence = self.model.predict(Face_roi)
        if confidence >= 50:
            return self.people[label], confidence
        else:
            return "", False
        
    def cropToFace(self, Frame):
        gray = cv.cvtColor(Frame, cv.COLOR_RGB2GRAY)
        # cv.imshow("testing", gray)
        frame_roi = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        try:
            first_face_indices = frame_roi[0]
            self.x, self.y, self.w, self.h = first_face_indices
        except:
            return []
        return Frame[self.y:self.y+self.h, self.x:self.x+self.w]
        
    def prepareDataSet(self, face_roi, name):
        face_roi = cv.cvtColor(face_roi, cv.COLOR_BGR2GRAY)
        if name not in self.people:
            self.people.append(name)
            self.people.sort()

        label = self.people.index(name)

        # self.labels = np.load(self.pathToLabels)
        # self.features = np.load(self.pathToFeatures)

        self.features.append(face_roi)
        self.labels.append(label)


    
    def saveChangedDataset(self):
        self.features = np.array(self.features, dtype='object')
        self.labels = np.array(self.labels)
        np.save(self.pathToFeatures, self.features)
        np.save(self.pathToLabels, self.labels)


    def trainRecognizer(self):
        pass
    
       