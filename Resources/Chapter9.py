import cv2
import numpy as np

# Face detection method by violla and jones
#so if we where to collect faces we would collect lots of positive faces images and lots of negative non faces images
#from this positives and negaives we would train and create a casade file that will help us find faces
#+ve and -ve images -> train -> xml file
# in our case we would not going to train model but instead we will use pretrained file provided by openCV
#Now openCV has provided number of different casade files that can detect different things such as eyes, nose full body etc.
#we can create our custom casade to detect cars, phones,etc
# haarcascade_frontalcatface.xml is not most accurate one but its fast
faceCasade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

img = cv2.imread("trump.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCasade.detectMultiScale(imgGray,1.1,4) #img,imagescale,nneighbours

#create bounding boxes around faces we have detected

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)