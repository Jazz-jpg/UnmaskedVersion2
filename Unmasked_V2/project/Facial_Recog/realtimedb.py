import urllib
import pyrebase
from firebase import FireBase
import os
from PIL import Image
from facerecognizer import FaceRecognizer
import cv2 as cv
import TakePicture as TakePicture
import Detector as Detector
import time

fire = FireBase()
fr = FaceRecognizer()
ryanid = "G000001"
path = "C:/Users/Jazz/Desktop/UnmaskedVersion2/Unmasked_V2/project/Facial_Recog/"
path = fire.getPath()
fr = FaceRecognizer(path)
# data = {
#    "f_name": "Andy",
#    "l_name" : "Lu",
# }
#imgPath = path + "my-image.png"
USERS = r'C:/Users/Jazz/Desktop/UnmaskedVersion2/Unmasked_V2/project/Facial_Recog/users'

# creates and uploads picture captured from detector.py
#fire.createUser('G1111111', data)
#fire.addUserPic('G1111111', imgPath)

# downloads all pictures for training
# fire.getAllPictures()

# gets all names of people in database and sets face recognizer list of recognizable people
# !!! setPeople is required for facial detection!!!
people = fire.getAllNames() 
fr.setPeople(people)

# trains model based off pictures in folder names of people in /users
# fr.create_train(USERS)
#pics = TakePicture.getImageNames(1)
# for i in pics:
#imgPath = path + 'PersonImages/' + i
#fire.addUserPic('G1111111', imgPath)
# time.sleep(3)


# time.sleep(10)
# print("Downloading")
# fire.getAllPictures()
# fr.create_train(USERS)

Detector.capture()
imgPath = fire.getPath() + "my-image.png"
img = cv.imread(imgPath)
fr.startDetect(img)

# for i in images:
#    img = cv.imread(path+i)
#    fr.startDetect(img)
