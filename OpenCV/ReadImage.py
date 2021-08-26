import cv2 as cv
import os
img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")
cv.imwrite("CV.png",img)
cv.imshow("PHOTO",img)
cv.waitKey(0)