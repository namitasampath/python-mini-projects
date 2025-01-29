import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow('Video',frame)
    
    if cv.waitKey(1) != -1:
        break

capture.release()
cv.destroyAllWindows
