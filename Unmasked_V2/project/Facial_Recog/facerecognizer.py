
import numpy as np
import cv2 as cv
import os
import project.Facial_Recog.Detector as Detector
from project.Facial_Recog.firebase import FireBase
import sys
from project.Facial_Recog.SendingEmail import sendEmail
import keyboard

class FaceRecognizer:
    def __init__(self):
        self.fire = None
        self.path = None
        self.haar_cascade = None
        self.USERS = r'C:/Users/Jazz/Desktop/UnmaskedVersion2/Unmasked_V2/project/Facial_Recog/users'
        
        self.people = []
    
    def getDatabase(self):
        return self.fire
    def setDatabase(self,fire):
        self.fire = fire
    def initFirebaseDB(self):
        if self.fire == None:
            self.fire = FireBase()
            self.path = self.fire.getPath()
            self.haar_cascade = cv.CascadeClassifier(self.path + '/haar_face.xml')
    def setPeople(self, list):
        self.people = list

    def checkParameters(self):
        if self.people is None:
            return False
        else:
            return True

    def startDetect(self):
        if self.checkParameters():
            self.fire.getAllPictures()
            users = self.fire.getAllNames()
            self.setPeople(users)
            self.compareUsers()
            self.create_train(self.USERS)
            
            
                
            Detector.capture()
            imgPath = "C:/Users/Jazz/Desktop/UnmaskedVersion2/Unmasked_V2/my-image.png"
            img = cv.imread(imgPath)
            name = self.detect(img)
            if name == None:
                print("Unknown entity")
            else:
                userid = self.fire.getUserID(name)
                self.fire.iterateOffenses(userid)
                self.fire.addOffendingPic(userid, imgPath)
                email = self.fire.getEmail(userid)
                sendEmail(email)
                
                cv.destroyAllWindows
        
        else:
            print("The people list is empty. Please run setPeople")

    def detect(self, img):
        face_recognizer = cv.face.LBPHFaceRecognizer_create()
        face_recognizer.read('face_trained.yml')

        np.load('features.npy', allow_pickle=True)
        np.load('labels.npy', allow_pickle=True)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Person', gray)
        label = None
        faces_rect = self.haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)
        for (x, y, w, h) in faces_rect:
            faces_roi = gray[y:y+h, x:x+w]

            label, confidence = face_recognizer.predict(faces_roi)
            print(f'Label = {self.people[label]} with a confidence of {confidence}')

            cv.putText(img, str(self.people[label]), (20, 20),
                    cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        cv.imshow('Detected_Face', img)
        if label == None:
            return None
        cv.waitKey(5)
        cv.destroyAllWindows
        return self.people[label]
        
        #Title: OpenCV Course - Full Tutorial with Python
         #Author: freeCodeCamp.org
        # #Date: 2020
        #Code Version: Python3
        #Abailability: https://www.youtube.com/watch?v=oXlwWbU8l2o, https://github.com/jasmcaus/opencv-course

    def create_train(self, DIR):
        haar_cascade = cv.CascadeClassifier(self.path + 'haar_face.xml')
        features = []
        labels =[]
        #loop over every person in list
        for person in self.people:
            #grab path for each person file
            path = os.path.join(DIR, person)
            label = self.people.index(person)
            print(person)
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

    def compareUsers(self):
        users = self.fire.getAllNames()
        usersdir = self.fire.getPath() + 'users/'
        dirnames = next(os.walk(usersdir), (None, [], None))[1]
        for i in dirnames:
            if i not in users:
                deleteddir = usersdir + i
                filenames = next(os.walk(deleteddir), (None, None, []))[2]
                for i in filenames:
                    os.remove(deleteddir + '/' + i)
                os.rmdir(deleteddir)
        print("Updated /users/ directory!")
                        
                
