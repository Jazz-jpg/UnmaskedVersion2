"""unmasked_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project import views
from django.conf import settings

urlpatterns = [
    #path ('firebaseTest', views.firebaseTest, name='test2'),
    path ('', views.index, name='test'), #Testing
    path ('About', views.about, name= 'about'),
    path ('Add', views.add,name="add"),
    path ('addStud', views.addStud,name="addStud"),
    path ('deletestudent', views.deletestudent, name='deletestudent'),
    path ('updatestudent' , views.studentupdate, name='studentupdate'),
    path ('update', views.update, name="update"),
    path ('AdminHome',views.adminHome, name= 'adminHome'),
    path ('alert',views.alert, name="alert"),
    path ('Contact',views.contact, name ='contact'),
    path ('GeneralQuestions',views.genQuestions, name="generalQuestions"),
    path ('Home', views.home, name='home'),
    path ('Login', views.login, name="login"),
    path ('Logout', views.logout, name='logout'),
    path ('ManageStudents', views.manageStudents, name="manageStudents"),
    path ('startDetect', views.startDetect, name="startDetect"),
    path ('Support', views.support, name="support"),
    path ('Tips',views.tips,name='tips'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
