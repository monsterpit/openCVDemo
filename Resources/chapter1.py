import cv2

### function image resize

img = cv2.imread("trump.png")

# To find size of image we use shape function (486,360,3) (height,width,no of color channel)
print(img.shape)

#image , (width,height for resize)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

#similar you can increase the number of pixels but it wont increase quality of image
imgResize2 = cv2.resize(img,(1000,500))
print(imgResize2.shape)

cv2.imshow("image",img)
cv2.imshow("image Resize",imgResize)
cv2.imshow("image Resize2",imgResize2)


###Cropping image
#So image itself is a array of pixels  , height comes first and then width opencv width comes first and then height
#0 to 200 pixels [0:200]
imgCropped = img[0:200,200:300]
cv2.imshow("image cropped",imgCropped)


cv2.waitKey(0)
