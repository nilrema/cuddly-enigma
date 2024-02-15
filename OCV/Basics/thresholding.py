import cv2 as cv

img = cv.imread('Photos/Photo1.jpg')

# first convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # if value is higher than 150, it will be set to 255, otherwise 0
cv.imshow('Simple Thresholded', thresh)

# adaptive thresholding
# it's good for images with varying lighting conditions
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitKey(0)
