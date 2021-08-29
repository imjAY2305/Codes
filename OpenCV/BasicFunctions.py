import cv2 as cv

img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")

cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()