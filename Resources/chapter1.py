import cv2
import numpy as np

###Warp perspective
#To get bird eye view of image

img = cv2.imread("cards.png")

width,height = 250,300
pt1 = np.float32([[44,356],[250,314],[71,669],[315,603]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])


matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("output Image",imgOutput)
cv2.waitKey(0)