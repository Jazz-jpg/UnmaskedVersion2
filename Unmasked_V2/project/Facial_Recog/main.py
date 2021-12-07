"""
import os
from os import walk

import firebase_admin
from firebase import FireBase

usersdir = 'C:/Users/PCAero/Desktop/UnmaskedVersion2/Unmasked_V2/project/Facial_Recog/TestingFaces/'

directories = next(os.walk(usersdir), (None, [], None))[1]
counter = 0
fb = FireBase()
#img = r"C:\Users\PCAero\Desktop\UnmaskedVersion2\Unmasked_V2\project\Facial_Recog\TestingFaces\Scarlett Johansson\MV5BMTM3OTUwMDYwNl5BMl5BanBnXkFtZTcwNTUyNzc3Nw@@._V1_.jpg"

#fb.addUserPic('G3', img)

for i in directories:
    userdir = usersdir + i
    if i == "Validation":
        pass
    else:
        spaceParser = i.find(" ")
        f_name = i[:spaceParser]
        l_name = i[spaceParser+1:]
        filenames = next(os.walk(userdir), (None, None, []))[2]
        gid = "G" + str(counter)
        data = {"f_name": f_name, "l_name": l_name}
        fb.createUser(gid, data)
        for j in filenames:
            pic = userdir + '/' + j
            fb.addUserPic(gid, pic)
        counter += 1
"""