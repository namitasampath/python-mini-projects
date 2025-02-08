import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
# paint the image in certain colors
# blank[200:300, 300:400]=0,0,255
# cv.imshow('green',blank)
# cv.rectangle(blank,(50,50),(500,500),(0,250,0),thickness=cv.FILLED)

# draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//3),(0,250,0),thickness=cv.FILLED)
cv.imshow('rectangle',blank)

# draw a circle
cv.circle(blank, (250,250),40,(0,0,255),thickness=-1)#another way of filling color is by setting thickness as -1
cv.imshow('circle',blank)

# draw a line
cv.line(blank, (10,10),(blank.shape[1]//2,blank.shape[0]//3),(0,255,255),thickness=2)
cv.imshow('line',blank)

# text on image
cv.putText(blank,'Hello World',(225,225),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)
