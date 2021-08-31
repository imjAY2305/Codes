#Resize is bascially known as altering the pixel dimensions of image
import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")
cv.imshow("Image",img)

#We can do that by using resize method
resized = cv.resize(img,(200,200),interpolation=cv.INTER_AREA)
cv.imshow("Resized",resized)
cv.waitKey(0)
cv.destroyAllWindows()