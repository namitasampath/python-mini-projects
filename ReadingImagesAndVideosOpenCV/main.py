import cv2 as cv

img = cv.imread('images/cat1.jpg')

cv.imshow('cat',img)

cv.waitKey(0)
