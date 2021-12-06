from cv2 import fastNlMeansDenoisingColoredMulti
from django.shortcuts import render, redirect#will render/show web files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect  
from django.conf import settings
import pyrebase 
import firebase_admin
from pyrebase.pyrebase import Firebase

#Configuration for firebase database
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

#Testing db connection via getting an email from db to print      
def firebaseTest(request):
    name = database.child("users").child("G2356732").child("email").get().val()
    name2 = database.child("users").child("G4589350").child("email").get().val()
    return HttpResponse(name)
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
    fName = request.GET['first-name']
    lName = request.GET['last-name']
    GrizzID = request.GET['Grizz-ID']
    email = request.GET['Email']
    #studPic = request.GET['student-pic']
    
    #Inserting data in firebase db
    data = {"email":email,"f_name":fName,"l_name":lName}
    database.child("users").child(GrizzID).set(data)
    
    #redirecting to manage student page
    return render(request, 'ManageStudents.html')
#Admin homepage
def adminHome(request):
    return render(request, 'AdminHome.html')
#Alert page
def alert(request):
    return render(request, 'alert.html')
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
    return render(request, 'LogoutPage.html')
# manage student page
# Looping through students in db and showing them 
def manageStudents(request):
    #Currently not implemented into manage students
    #Is a dynamic list of all students in db
    all_students = database.child("users")
    return render(request, 'ManageStudents.html', {'students':all_students})
#support page
def support(request):
    return render(request, 'Support.html')
#Tips page
def tips(request):
    return render(request, 'Tips.html')

