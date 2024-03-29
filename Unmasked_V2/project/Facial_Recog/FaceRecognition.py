import numpy as np
import cv2 as cv

#Title: OpenCV Course - Full Tutorial with Python
#Author: freeCodeCamp.org
# #Date: 2020
#Code Version: Python3
#Abailability: https://www.youtube.com/watch?v=oXlwWbU8l2o, https://github.com/jasmcaus/opencv-course

# Obtain info from FaceTesting
haar_cascade = cv.CascadeClassifier('')

people = ["Ben Afflek", "Beyonce", "Scarlett Johansson","Ryan Reynolds"]
# np.load('features.npy')
# np.load('labels.npy')

#Obtain yml file for facial training
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
#get image needing to be verified
img = cv.imread(r"")

#turn image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#detect face in image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

#rectangle around face
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0), thickness =2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness =2)
cv.imshow('Detected_Face', img)
cv.waitKey(0)
