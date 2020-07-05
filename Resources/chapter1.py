import cv2
import numpy as np

###Shapes and Text
#How to draw shapes and text on image
# np.zeros((512,512)) black image
#creating image
img = np.zeros((512,512,3),np.uint8)
print(img.shape)

#making image color blue
#img[:] whole image
#img[0:200,200:300] specific part of image
img[:] = 255,0,0

#Draw Line
#Line (img,startPoint,endPoint,colorOfLine,thickness)
#cv2.line(img,(0,0),(300,300),(0,255,0),3)

#img.shape[1] => width of image img.shape[0] => height of image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#Draw Rectangle (img,startPoint,endPoint,color of rect,thickness of line)
#cv2.rectangle(img,(0,0),(200,200),(0,0,255),2)

#Fill rectangle
cv2.rectangle(img,(0,0),(200,200),(0,0,255),cv2.FILLED)

#Draw Circle (img,centerPoint,radius,color,thickness)
cv2.circle(img,(250,250),20,(0,0,255),1)

###Put Text of image (img,text,originPoint,font Style,scale,color,thickness)
cv2.putText(img,"Hello world",(300,100),cv2.FONT_HERSHEY_COMPLEX,2.5,(0,0,255),5)

cv2.imshow("image",img)
cv2.waitKey(0)