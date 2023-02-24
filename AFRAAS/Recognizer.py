import cv2 as cv



class Recognizer:
    def __init__(self, cascade=r"resources\models\haar_face.xml", model=r"resources\models\face_trained.yml"):
        self.pathToCascade = cascade
        self.pathToModel = model
        try:
            self.cascade = cv.CascadeClassifier(self.pathToCascade)
            self.model = cv.face.LBPHFaceRecognizer_create()
            self.model.read(model)
            
        except:
            message = "haar cascade file is not found on the path provided"
            raise Exception(message)
        
    def whoIs(self, Frame):
        label, confidence = self
        pass
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
    
       