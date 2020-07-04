import cv2
print("package imported")

#For image
#img = cv2.imread("trump.png")
#cv2.imshow("Output", img)
#cv2.waitKey(0)
#cv2.waitKey(0) 0 means infinite 1 means 1000 milliseconds

#For playing a Stored Video
#cap = cv2.VideoCapture("nature.mp4")
#while True:
#    success,img = cap.read()
#    cv2.imshow("Video",img)
#    if cv2.waitKey(1) & 0xFF == ord("q"):
#        break

#For webcam
cap = cv2.VideoCapture(0)  #1 means video cam
cap.set(3,640)  # cap.set 3 means width, 4  means height and 10 means brightness
cap.set(4,720)
cap.set(10,100)
while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break