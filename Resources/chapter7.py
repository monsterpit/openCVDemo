import cv2
import numpy as np

###Color detection


def empty(a):
    pass
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

cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars",640,240)
#name of window,add on which window,initial value, max value, function executed when trak bar value is changed
#Hue ranges from 0 to 255 but opencv supports still 179 so max value 179
cv2.createTrackbar("Hue Min","trackBars",0,179,empty)
cv2.createTrackbar("Hue Max","trackBars",13,179,empty)
cv2.createTrackbar("Sat Min","trackBars",24,255,empty)
cv2.createTrackbar("Sat Max","trackBars",250,255,empty)
cv2.createTrackbar("Value Min","trackBars",119,255,empty)
cv2.createTrackbar("Value Max","trackBars",255,255,empty)

while True:
    img = cv2.imread("lambo.png")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #trackbar name, window name is which it belongs
    h_min = cv2.getTrackbarPos("Hue Min","trackBars")
    h_max = cv2.getTrackbarPos("Hue Max","trackBars")
    s_min = cv2.getTrackbarPos("Sat Min","trackBars")
    s_max = cv2.getTrackbarPos("Sat Max","trackBars")
    v_min = cv2.getTrackbarPos("Value Min","trackBars")
    v_max = cv2.getTrackbarPos("Value Max","trackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    #creating a mask
    mask = cv2.inRange(imgHSV,lower,upper)
    #cv2.imshow("lambo ",img)
    #cv2.imshow("lamboHSV ",imgHSV)
    #cv2.imshow("mask  ", mask)
    # keep things in black color if you dont want it

    #which will add 2 images together to create a new image it will check both images and wherever the pixel are both present it will take it has a yes or a 1  and it will store that in new image
    # cv2.bitwise_and(img,img,mask=mask)   source image,output image, mask
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    #cv2.imshow("Result masked image  ", imgResult)

    imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("Stack Images",imgStack)
    cv2.waitKey(1)