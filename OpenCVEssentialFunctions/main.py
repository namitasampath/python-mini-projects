import cv2 as cv

img = cv.imread('Cat1.jpg')
cv.imshow('Cat',img)

#converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', gray)

#Blurring image
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur cat', blur)

#Edge Cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny',canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilated', dilated)

#Resize
resize = cv.resize(img, (400,500))
cv.imshow('Resize', resize)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
