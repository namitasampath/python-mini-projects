import cv2 as cv
import numpy as np

img = cv.imread('Cat1.jpg')
cv.imshow('Cat', img)

# Masking is used to focus on specified region of an image while ignoring other positions.

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank',blank)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100,255,-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)