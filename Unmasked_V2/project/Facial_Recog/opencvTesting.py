#Importing openCV
import cv2 as cv

#Title: OpenCV Course - Full Tutorial with Python
#Author: freeCodeCamp.org
# #Date: 2020
#Code Version: Python3
#Abailability: https://www.youtube.com/watch?v=oXlwWbU8l2o, https://github.com/jasmcaus/opencv-course


#Reading Images
#Assigning image to img from TestingPhotos File in Current Directory
img = cv.imread('TestingPhotos/10-of-the-deadliest-sea-creatures-in-the-world-6.jpg')

#Showcases image in new window
cv.imshow("Fish",img)

#keyboard binding function, # indicates wait time. 0 indicates waiting for button press
cv.waitKey(0)

# #Reading Videos
# #Takes integer values or path to video file. Integer values are for webcam/camera usage (for one webcame you can use 0)
# #capture = cv.VideoCapture('TestingVideos/【Official】Pokémon Special Music Video 「GOTCHA！」 _ BUMP OF CHICKEN - Acacia_1080p.mp4')

# #You read videos frame by frame using while
# while True:
#     #Capture.read takes the video frame by frame and reads it
#     isTrue, frame = capture.read()
#     #display individual frame
#     cv.imshow("Video", frame)
    
#     #stopping video
#     #If letter d is pressed break out of loop and stop display
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()