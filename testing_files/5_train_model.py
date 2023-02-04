import cv2 as cv
import os
import numpy as np 

people = []
for i in os.listdir(r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons'):
    people.append(i)

# print(people)

haar_cascade = cv.CascadeClassifier(r'C:\Users\DAVASR\Documents\AFRAAS_practice\testing_files\haar_face.xml')

DIR = r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons'

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        # print("path : ",path," \n label: ",label)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            # cv.imshow('test', img_array)

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            # cv.imshow('test2', gray)
            # cv.waitKey(0)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # face region of interest

                features.append(faces_roi)
                labels.append(label)
        

create_train()
# print(f"length of peoples list : {len(people)}")
# print(f"length of features list : {len(features)}")
# print(f"length of labels list : {len(labels)}")

# convert python lists to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

# and save them
np.save('features.npy', features)
np.save('labels.npy', labels)

# face recognizer initiation
face_recoginizer = cv.face.LBPHFaceRecognizer_create()

# train the model and save for using it in other files
face_recoginizer.train(features, labels)
face_recoginizer.save('face_trained.yml')

