import cv2 as cv
import numpy as np

#img = cv.imread("C:/Users/vijay/Desktop/photo.jpg")
#cv.imshow("Image",img)

blank = np.zeros((500,500,3), dtype="uint8")
#cv.imshow("Blank",blank)

# Paint the image
blank[200:300,100:400] = 0,0,255
#cv.imshow("Painted Image",blank)

#Draw Rectangle
rect = np.zeros((500,500,3), dtype="uint8")
cv.rectangle(rect,(20,20),(250,250),(0,0,255),thickness=5)
cv.imshow("Rectangle",rect) 

cv.waitKey(20000)
cv.destroyAllWindows()