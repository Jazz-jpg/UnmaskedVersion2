# Unmasked
*Oakland University - CSI 4999 - Senior Capstone - Fall 2021*

## Problem Statement
With the rampant spread of the delta variant, and now the existence of Omicron. Schools and communities are looking now more than ever to enforce social distancing and mask mandates for the safety of their communities.

## Our Solution
We concluded a need for a Mask Detection/Facial Recognition system that will detect people within the school system who are not wearing a mask in an effort to provide schools and effective methood to enforce mask mandates and solve a portion of this problem.


# Primary Themes
Public health and safety, in addition to social responsibilities and ethical considerations. It is a social system in that it will have a large social impact, and it is Ethical in the sense that we as communities have an ethical duty to have our populations best interest at heart.



## How It Was Accomplished
- We Adopted the Agile Scrum Process
- Applied a Divide and Conquer Approach
- Established a team specific workflow
- Created supporting backlogs and Use cases


## Technoologies Used
- Firebase
- Python/Django
- HTML/CSS/Bootstrap
- OpenCV
- Figma & Webflo

## Our Team and Roles
* Team Lead (Scrum Master) - Jasmin Medic ([Jazz-jpg](https://github.com/Jazz-jpg))
* Product Owner - Rachel Yang ([Lunar-Flare](https://github.com/Lunar-Flare))

* Developer - Justin Chorazyczewski ([JChorazyczewski](https://github.com/JChorazyczewski))
* Developer -Andy Lu ([AndyLu](https://github.com/luandycs)
* Developer -Nancy Hana ([Nancy617](https://github.com/nancy617)


## Challenges We Faced As A Team
This kind of project was a new frontier for us. Neither of us have had previous Machine Learning Experiences and there was a significant learning curve with regards to our technology stack. We learned a lot about the limitations of our software. And the sheer amount of knowledge still left to be learned with regards to machine learning and it's applications.

## Key System Components
- Facial Detection
- Facial Recognition
- Database
- UI


## Current Working Features
- Live identification of mask status of an individual
- Pattern Searching database for said individual
- Documenting the offense and storing it
- Notifying Individual via email of offense
- UI for administrative Use
- CRUD functionality for adding students and maintaining training Data

## Software Limitations
- Limited to frontal face detection
- limited to identifying 1 individual at a time
- Scalability with regards to massive amounts of data


## How It works
Our software is a web-based software that allows admin users to run multiple cameras on a system. The system requires admins to enter student information into the database including some pictures of the individual. The Pictures are used as training Data to identify individuals using our Facial Recognition Algorithm which is comprised of Haar Cascade Classifiers. The administrator will press the big red Run Button which will launch the camera system and then enable screencapture of individuals on the system. A person with a mask is invisible to the system. But a person without a mask is immediately recognized. After a small delay that we had programmed due to ethical reasons. The system will take a cropped screencapture of the individual and cross reference their photo with what is on hand using our Facial Recognition Classifier. If a match is found the system will notify the individual that is in opposition of mask Mandate via an e-mail that they have under their profile. All the nescessary support functions to make this work are also implemented and functional.


# How to run the program
??? Ensure your PC has both python and Django installed You can check this by navigating to your root directory and typing python --version, later when you navigate into the scripts file you can check the django version by launching python in the terminal and following these commands as well as having any missing dependencies

??? >python

??? >Import django

??? >django.get_version()

??? download the repo and append the files into a new project app created within the django virtual env

??? Open up your command terminal and navigate to the cloned repo folder

??? Navigate to the Scripts file in the command terminal and type in activate

??? Navigate back to the root folder and change directory into the Unmasked folder

??? Type > python manage.py runserver

??? Paste the localhost link into your browser of choice and you should be good to go


## Landing Page
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/1.png)
## About Page
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/2.png)
## Resources Page
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/3.png)
## Login
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/4.png)
## Manage Students
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/5.png)
## Update Students
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/6.png)
## Alert
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/7.png)
## System Home
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/8.png)
## Camera
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/9.png)
## What A Match Looks like
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/10.png)
![alt-text](https://github.com/Jazz-jpg/UnmaskedVersion2/blob/main/Screenshots/Unmasked%20Screenshot/11.png)
