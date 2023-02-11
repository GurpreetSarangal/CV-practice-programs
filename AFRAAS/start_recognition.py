import os
import datetime

import cv2 as cv
import numpy

def start_camera(mode=1, additional=None):
    try:
        if additional == None:
            capture = cv.VideoCapture(mode)
        else:
            capture = cv.VideoCapture(mode, additional)
    except:
        raise Exception("E-1: Camera was not accessed")
    
    return capture

def recognize(frame):
    return False, 0

def process():
    try:
        capture = start_camera(1)
    except Exception as e:
        print(e)
        exit()
    
    time_now = datetime.datetime.now()
    range = datetime.timedelta(seconds=45)
    time_out = time_now + range


    print("starting: ", datetime.datetime.now())
    while(datetime.datetime.now() != time_out):
        isTrue, frame = capture.read()
        is_recognized, label = recognize(frame)
        if is_recognized:
            print(f"The attendance is marked for label: {label}")
            break
    
    print("ending: ", datetime.datetime.now())
    print("time out")

process()