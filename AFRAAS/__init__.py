from .Camera import *
from .Project import *
from .Recognizer import *


# def initiate():
#     project = Project()
#     project.

# def test(c=1):
#     cam = Camera(c)
#     cam.test_Cam()

def startUp():
    pass

def standBy(camera=Camera(1), 
            recognizer=Recognizer()):
    window = Project()
    while True:
        frame = camera.getFrame()
        window.dashboard(frame)

        face = recognizer.cropToFace(frame)
        if face != []:
            label, confidence = recognizer.whoIs(face)
            if confidence:
                

    
    

def boot():
    cam = Camera(1)
    rec = Recognizer()
    startUp()
    standBy(cam, rec)
    pass