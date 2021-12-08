from django.db import models
from project.Facial_Recog.facerecognizer import FaceRecognizer
# Create your models here.
class gettingDatabase:
    def __init__(self):
        self.face = FaceRecognizer()
         