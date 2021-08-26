import cv2 as cv
capture = cv.VideoCapture(0) # 0-> Camera index
while True:
    isTrue, frame = capture.read() #Captures image frame by frame
    cv.imshow("Video",frame)
    if(cv.waitKey(0)):
        break
capture.release()
cv.destroyAllWindows()