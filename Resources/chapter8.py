import cv2
import numpy as np

###Contours/ shape detection
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    #image,retrieval method     RETR_EXTERNAL it return outer corners, approximation we want all values or uyou can request for compressed value
    #CHAIN_APPROX_NONE get all values for contours
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 10: # remove noise
            # drawContours (imageTo draw on,contours,contour index(-1 means all the indexs),color,thickness)
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)

            #curve length to approx corner of our shape
            peri = cv2.arcLength(cnt,True)  #contour, True (its close is True)
            #print(peri)

            #approx how many corner points we have
            approx = cv2.approxPolyDP(cnt, 0.02 *peri , True ) #contours,reolution, True(closed poly)
            print(len(approx))

            objCor = len(approx)
            if objCor == 3: objType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objType = "Square"
                else: objType = "rectangle"
            elif objCor > 4:  objType = "circle"
            else: objType = "none"

            x,y,w,h = cv2.boundingRect(approx) #bounding Box of  objects from this we can get width and height of object
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.putText(imgContour,objType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),1)



img = cv2.imread("shapes.jpg")
#copy image
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blur (img,kernel,sigma) higher sigma equals more blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))

cv2.imshow("image stack",imgStack)
cv2.waitKey(0)