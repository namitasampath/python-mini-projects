import cv2 as cv

img = cv.imread('Cat1.jpg')
cv.imshow('Cat',img)

# Averaging
# Blurring middle pixel average
average = cv.blur(img, (7,7))
cv.imshow('Average',average)

# Gaussian blur
gaussian = cv.GaussianBlur(img, (7,7),0)
cv.imshow('Average Gaussian', gaussian)

# Median Blur
median = cv.medianBlur(img,9)
cv.imshow('Median',median)

# Bilateral blur - blur and maintain sharpness
Bilateral = cv.bilateralFilter(img,9,75,75)
cv.imshow('Bilateral', Bilateral)

cv.waitKey(0)