#Translation means shifting an image in x and y axis or also the
#combinations of both x and y axis

import cv2 as cv
import numpy as np
img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")

#We need to create a transalation method with img,x,y as parameters
def translate(img,x,y):
    #We need to create a translation matrix
    transMat = np.float32([[1,0,x],[0,1,y]])
    #We also need dimenions of the image
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#Values are
# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img,100,150)
cv.imshow("Image",translated)
cv.waitKey(0)
cv.destroyAllWindows()