from Camera import Camera
from Recognizer import Recognizer


class Project:
    def __init__(self, camera):
        self.conn = Camera.connect(camera)
        self.cascade = Recognizer()
        pass

    def start(self):
        print("start")
        pass

    def intro(self):
        pass

    def registerNewFace(self):
        pass

    def dashboard(self):
        pass

    def initiateScanning(self):
        pass
