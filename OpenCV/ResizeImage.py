import cv2 as cv
ref = cv.imread("C:/Users/vijay/Desktop/photo.jpg")
ref1 = cv.resize(ref,(720,600),interpolation=cv.INTER_CUBIC)
cv.imshow("Image",ref)
cv.imshow("Image Re-Sized",ref1)
cv.waitKey(0)