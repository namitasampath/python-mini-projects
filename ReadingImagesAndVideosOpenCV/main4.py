import cv2 as cv 

img = cv.imread('images/cat1.jpg')

cv.imshow('cat',img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)

cv.imshow('Resize_cat',resized_image)
cv.waitKey(0)

#This program displays the image twice and displays the resize feature
