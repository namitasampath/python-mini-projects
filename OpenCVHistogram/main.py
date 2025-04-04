import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Histograms help us understand pixel intensity distribution
img = cv.imread('Cat1.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2],dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Mask", mask)

gray_hist= cv.calcHist([gray],[0],mask, [256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
