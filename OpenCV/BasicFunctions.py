import cv2 as cv

img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")
#cv.imshow("Image",img)

#Converting to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Image",gray)

#Blur a image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow("BLUR",blur)

#Edge Cascade
edge = cv.Canny(img,125,175) #We can reduce the number of edges by passing an blured image
cv.imshow("EDGE",edge)

#Dilating the Image
dilate = cv.dilate(edge,(7,7),iterations=5)
cv.imshow("Dilate",dilate)
cv.waitKey(0)
cv.destroyAllWindows() 