#Facial recognizing code
import cv2 as cv
import numpy as np


import os
class FaceRecognizer:
    def __init__(self, path):
        self.path = path
        self.haar_cascade = cv.CascadeClassifier(self.path + '/haar_face.xml')
        self.people = []
    
    def setPeople(self, list):
        self.people = list

    def checkParameters(self):
        if self.people is None:
            return False
        else:
            return True

    def startDetect(self, img):
        if self.checkParameters():
            self.detect(img)
        else:
            print("The people list is empty. Please run setPeople")

    def detect(self, img):
        face_recognizer = cv.face.LBPHFaceRecognizer_create()
        face_recognizer.read('face_trained.yml')

        np.load('features.npy', allow_pickle=True)
        np.load('labels.npy', allow_pickle=True)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Person', gray)

        faces_rect = self.haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)
        for (x, y, w, h) in faces_rect:
            faces_roi = gray[y:y+h, x:x+w]

            label, confidence = face_recognizer.predict(faces_roi)
            print(f'Label = {self.people[label]} with a confidence of {confidence}')

            cv.putText(img, str(self.people[label]), (20, 20),
                    cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        cv.imshow('Detected_Face', img)
        cv.waitKey(0)

    def create_train(self, DIR):
        haar_cascade = cv.CascadeClassifier('C:/Users/PCAero/Desktop/FacialRecognition/haar_face.xml')
        features = []
        labels =[]
        #loop over every person in list
        for person in self.people:
            #grab path for each person file
            path = os.path.join(DIR, person)
            label = self.people.index(person)
            
            #Loop over every image in file
            for img in os.listdir(path):
                img_path = os.path.join(path, img)
                img_array = cv.imread(img_path)
                gray = cv.cvtColor(img_array, cv.COLOR_RGB2GRAY)
                
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=16)
                
                #rectangle around face
                for (x,y,w,h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    features.append (faces_roi)
                    #index of list (mapping between string and numerical label, which lightens load on hardware)
                    labels.append(label)
        features = np.array(features, dtype='object')
        labels = np.array(labels)
        face_recognizer = cv.face.LBPHFaceRecognizer_create()
        face_recognizer.train(features,labels)
        face_recognizer.save('face_trained.yml')
        print("Training Complete!")
        np.save('features.npy', features)
        np.save('labels.npy', labels)

