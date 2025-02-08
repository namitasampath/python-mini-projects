import cv2 as cv
import numpy as np

img= cv.imread('Cat1.jpg')

cv.imshow('Image',img)

def rotate(img,angle,rotPoint=None):
    (height, width)= img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimention = (width, height)

    return cv.warpAffine(img, rotMat, dimention)

rotated= rotate(img, -45)
rotated2= rotate(img, 45)

cv.imshow("Rotated", rotated)
cv.imshow("Rotated2", rotated2)


cv.waitKey(0)    