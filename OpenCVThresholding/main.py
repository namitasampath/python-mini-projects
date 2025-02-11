import cv2 as cv

img = cv.imread('Cat1.jpg')
# cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# simple thresholding inverse
threshold, thresh_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold inverse', thresh_inv)

# Adaptive Thresholding
a_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold', a_thresh)


cv.waitKey(0)