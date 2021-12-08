from typing import OrderedDict
from cv2 import VideoCapture, fastNlMeansDenoisingColoredMulti
from django.shortcuts import render, redirect#will render/show web files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect  
from django.conf import settings
import pyrebase 
import firebase_admin
from pyrebase.pyrebase import Firebase
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import project.Facial_Recog.Detector as Detector 
from project.Facial_Recog.facerecognizer import FaceRecognizer
from firebase_admin import db

from collections import OrderedDict
from operator import getitem
#Configuration for firebase database
fr = FaceRecognizer()
fr.initFirebaseDB()

#Test page 
def index (request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, welcome to the index page.This is a test.")
#About page 
def about (request):
    return render(request,'About.html')
#Add page 
def add(request):
    return render(request, 'add.html')
#Adds a student and then redirects to manage student page
def addStud(request):
    #getting information
    database = fr.getDatabase()
    fName = request.GET['First Name']
    lName = request.GET['Last Name']
    GrizzID = request.GET['GrizzlyID']
    email = request.GET['Email']
    #studPic = request.FILES['Image']
    fr
    
    #Inserting data in firebase db
    database = {"email":email,"f_name":fName,"l_name":lName,"offences": 0}
    db.reference("/users/").child(GrizzID).update(database)
    
    #redirecting to manage student page
    return redirect(manageStudents)
#Deletes student from database
def deletestudent(request):
    database = fr.getDatabase()
    GrizzID = request.GET['Grizz-ID']
    db.reference('/users/').child(GrizzID).delete()
    #print("Would of deleted")
    return redirect(manageStudents)

#Update student from database
#WIP
def studentupdate(request):
    database = fr.getDatabase()
    fName = request.GET['FirstName']
    lName = request.GET['LastName']
    GrizzID = request.GET['GrizzlyID']
    email = request.GET['Email']

    temp = {"email":email,"f_name":fName,"l_name":lName}
    #db.reference('/users/').child(GrizzID).update(temp)
    return render(request, 'ManageStudents.html')
def update(request):
    return render(request, 'update.html')
#Admin homepage
def adminHome(request):
    return render(request, 'AdminHome.html')
#Alert page
#WIP
def alert(request):
    allKey = {}
    data = fr.getDatabase()
    data = db.reference('/users/')
    users = data.get()
    for user in users:
        temp = db.reference('/users/'+ user)
        temp = temp.get()
        #print(temp)
        allKey[user] = temp
        
    #Title: Python | Sort nested dictionary by key
    #Author: GeeksforGeeks
    #Date: 2020
    #Code Version: Python3
    #Abailability: https://www.geeksforgeeks.org/python-sort-nested-dictionary-by-key/
    
    sortedKeys = OrderedDict(sorted(allKey.items(), key = lambda x: getitem(x[1], 'offenses'),reverse=True))
    #print(sortedKeys)
    return render(request, 'alert.html',{'allUsers':sortedKeys})
#Contact page
def contact(request):
    return render(request, 'Contact.html')
#General Questions page
def genQuestions(request):
    return render(request, 'GeneralQuestions.html')
#Home page
def home(request):
    return render(request, 'Home.html')
#Logini page
def login(request):
    return render(request, 'Login.html')
#Logout page
def logout(request):
    return render(request, 'Home.html')
# manage student page
def manageStudents(request):  
    allKey = {}
    data = fr.getDatabase()
    data = db.reference('/users/')
    users = data.get()
    for user in users:
        temp = db.reference('/users/'+ user)
        temp = temp.get()
        #print(temp)
        allKey[user] = temp
    return render(request, 'ManageStudents.html',{'allUsers':allKey})
# Start detection function
def startDetect(request):
    fr.initFirebaseDB()
    fr.startDetect()
    return render(request,'AdminHome.html')
#support page
def support(request):
    return render(request, 'Support.html')
#Tips page
def tips(request):
    return render(request, 'Tips.html')

