import cv2 as cv
import numpy as np

img = cv.imread('Cat1.jpg')

# cv.imshow('Cat',img) 

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Cat', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(img,125,175)
cv.imshow('Canny', canny)


contours, hierarchise = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# hierarchise will contain information about topology
# contour is the list of all the contours. Each contour stores a numpy array point.

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours, hierarchise = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)


print(len(contours))

cv.drawContours(blank, contours,-1,(0,0,255),thickness=1)
cv.imshow('Cat', blank)
cv.waitKey(0)
