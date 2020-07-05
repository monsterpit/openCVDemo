import cv2
import numpy as np

#functions

img = cv2.imread("trump.png")

#GrayScale Image  cvtColor basically converts your image to different colors
#in openCV color channel are bgr
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#edge detector we are using canny  . we can increase the value of threshold to decrease the edges displayed
imgCanny = cv2.Canny(img,150,200)

#dilation:- Now sometime we detecting a edge but because there is a gap or its not joint properly it doesnt detect it has a proper lineso what we can do is increase the thickness of edge

#numpy is a library to deal with matrices
#np.ones we need  all the values to be ones and kernel size (5,5) 5x5 and type of object np.unit8 which means value can range from 0 to 255
kernel = np.ones((5,5),np.uint8)
#has we are dealing with edges we will use canny Image , kernel requires a matrix
#how many iteration we want our kernel to move around which means how much thickness do we want
imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)

#opposite of dilation which is erosion to make edges thinner
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)