#Rotation - is rotating an image in a particular angle.
#OpenCV allows us to rotate image from a particular point
import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")
cv.imshow("Image",img)

#Create a rotation method with img,angle,rotpoint=NONE as parameters
def rotate(img,angle,rotPoint=None):
    #We need height and width for this
    (height,width) = img.shape[:2]
    #if the rotation point is NONE, we gonna assume it as center
    if(rotPoint is None):
        rotPoint = (width//2,height//2)

    #We need to create a rotated new matrix of pixels. so we use a method
    #called getRotationMatrix2D()
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow("Rotated",rotated)
cv.waitKey(0)
cv.destroyAllWindows()