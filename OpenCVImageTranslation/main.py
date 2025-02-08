import cv2 as cv
import numpy as np

img = cv.imread('Cat1.jpg')

cv.imshow ('Boston', img)

#Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimention= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat,dimention)

translated = translate(img, -100,-100)
cv.imshow('Translate', translated) 
#-x -->Left
#-y -->Up
# x -->Right
# y -->Down

cv.waitKey(0)
