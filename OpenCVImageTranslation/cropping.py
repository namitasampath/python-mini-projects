import cv2 as cv
import numpy as np

img = cv.imread('Cat1.jpg')

cv.imshow('Cat', img)


#Resizing

resized = cv.resize(img, (300,300),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#Flipping

flip=cv.flip(img, 1)
cv.imshow('flip',flip)
# 1:horizontal
# 0:vertical
# -1:both vertical and horizontal

#Cropping
cropped=img[50:200,100:600]
cv.imshow('Cropped',cropped)

cv.waitKey(0)