from cv2 import fastNlMeansDenoisingColoredMulti
from django.shortcuts import render, redirect#will render/show web files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect  
from django.conf import settings
import pyrebase 
import firebase_admin
from pyrebase.pyrebase import Firebase

config = {
            "apiKey": "AIzaSyAxV8-iToKuLitUmG48EEkIddvq7iYrN2Y",
            "authDomain": "facial-recongition-38069.firebaseapp.com",
            "databaseURL": "https://facial-recongition-38069-default-rtdb.firebaseio.com",
            "projectId": "facial-recongition-38069",
            "storageBucket": "facial-recongition-38069.appspot.com",
            "messagingSenderId": "937313859878",
            "appId": "1:937313859878:web:25d017bad4c1df1255e9e7"
        }
cred_obj = firebase_admin.credentials.Certificate(
            'C:/Users/justi/Desktop/Unmasked2Ripo/UnmaskedVersion2/Unmasked_V2/project/Facial_Recog/facial-recongition-38069-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(
            cred_obj, {'databaseURL': config["databaseURL"]})
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

#Testing db hookup test, getting email       
def firebaseTest(request):
    name = database.child("users").child("G2356732").child("email").get().val()
    name2 = database.child("users").child("G4589350").child("email").get().val()
    return HttpResponse(name)

#All student show up for management
def studAdd(request):
    fName = request.GET['first-name']
    lName = request.GET['last-name']
    GID = request.GET['grizzID']
    email = request.GET['email']
    #studPic = request.GET['student-pic']
    
    #Inserting data 
    data = {"email":email,"f_name":fName,"l_name":lName}
    database.child(GID).set(data)
    return render(request, 'ManageStudents.html')       


#Renders all webpages
def index (request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, welcome to the index page.This is a test.")
def about (request):
    return render(request,'About.html')
def add(request):
    return render(request, 'add.html')
def adminHome(request):
    return render(request, 'AdminHome.html')
def alert(request):
    return render(request, 'alert.html')
def contact(request):
    return render(request, 'Contact.html')
def genQuestions(request):
    return render(request, 'GeneralQuestions.html')
def home(request):
    return render(request, 'Home.html')
def login(request):
    return render(request, 'Login.html')
def logout(request):
    return render(request, 'LogoutPage.html')
def manageStudents(request):
    return render(request, 'ManageStudents.html')
def support(request):
    return render(request, 'Support.html')
def tips(request):
    return render(request, 'Tips.html')

