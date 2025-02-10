import cv2 as cv
import numpy as np

img = cv.imread('pic.jpg')
# cv.imshow('image',img)

b,g,r=cv.split(img)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(g.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merge',merged)

cv.waitKey(0)