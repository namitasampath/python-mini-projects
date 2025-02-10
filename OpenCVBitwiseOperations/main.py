import cv2 as cv
import numpy as np
blank = np.zeros((400,400),dtype='uint8')

rect = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rect)
cv.imshow('Circle',circle)

# Bitwise And
bitwise_and = cv.bitwise_and(rect,circle)
cv.imshow('Bitwise And', bitwise_and)

# Bitwise Or
bitwise_or = cv.bitwise_or(rect,circle)
cv.imshow('Bitwise Or', bitwise_or)

# Bitwise And
bitwise_xor = cv.bitwise_xor(rect,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise not', bitwise_not)



cv.waitKey(0)