import cv2 as cv

def reScale(frame,scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized = reScale(frame)
    cv.imshow("Video",frame)
    cv.imshow("Video ReSized",frame_resized)
    if(cv.waitKey(0)):
        break
capture.release()
cv.destroyAllWindows()