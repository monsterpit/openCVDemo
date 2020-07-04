import cv2
print("package imported")

#For image
#img = cv2.imread("trump.png")
#cv2.imshow("Output", img)
#cv2.waitKey(0)

cap = cv2.VideoCapture("nature.mp4")

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break