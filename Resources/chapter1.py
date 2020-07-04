import cv2
print("package imported")

img = cv2.imread("trump.png")
cv2.imshow("Output", img)

cv2.waitKey(0)