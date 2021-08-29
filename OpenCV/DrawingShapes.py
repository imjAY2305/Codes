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
rect[:] = 0,255,0 #Green Colour
cv.rectangle(rect,(20,20),(250,250),(0,0,255),thickness=-1)
#cv.imshow("Rectangle",rect)

#Draw Circle
circle = np.zeros((600,600,3), dtype = "uint8") 
cv.circle(circle,(300,300),100,(0,0,255),thickness=-1)
#cv.imshow("Circle",circle)

#Draw Line
line = np.zeros((600,600,3),dtype = "uint8")
cv.line(line,(0,0),(600,600),(0,0,255),thickness=2)
#cv.imshow("Line",line)

#Write Text
text = np.zeros((600,600,3),dtype="uint8")
cv.putText(text,"IMJAY",(300,300),cv.FONT_HERSHEY_COMPLEX,1.0,(255,255,255),2)
cv.imshow("Text",text)

cv.waitKey(20000)
cv.destroyAllWindows() 