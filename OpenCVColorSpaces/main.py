import cv2 as cv
import matplotlib.pyplot as plt

img= cv.imread('Cat1.jpg')
cv.imshow('Cat', img)

plt.imshow(img)
plt.show()

# BGR to GrayScale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to LAB
lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# HSV to BGR
hsv_bgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

plt.imshow(rgb)
plt.show()

# in matplotlib default color code is RGB and in opencv default color code is BGR


cv.waitKey(0)