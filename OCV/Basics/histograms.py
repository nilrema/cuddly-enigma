import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/Photo1.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

# histograms are a graphical representation of the pixel intensity distribution
# histograms can help us understand the contrast, brightness, intensity distribution, etc. of an image
# histograms can help us understand the color distribution of an image

# we can create a histogram for the entire image, or we can create a histogram for each color channel
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# create a mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

# create a grayscale histogram
# the first parameter is the image
# the second parameter is the number of channels
# the third parameter is the mask
# the fourth parameter is the number of bins
# the fifth parameter is the range
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
