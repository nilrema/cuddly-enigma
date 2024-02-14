import cv2 as cv

img = cv.imread('Photos/Photo1.jpg')

# we can smooth an image using various techniques
# the most common technique is the Gaussian blur
# the Gaussian blur is a weighted average of the pixels in the image
# the weight is determined by the standard deviation
# the standard deviation is determined by the kernel size
# the kernel size must be a positive odd integer
# the higher the standard deviation, the more blurred the image will be
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

# Averaging blur
# we define the kernel size as a tuple
# the kernel size must be a positive odd integer
average = cv.blur(img, (6, 6))
cv.imshow('Average Blur', average)

# Median blur
# the median blur is a non-linear filter
# it replaces each pixel's value with the median value of the pixels in the kernel
# the kernel size must be a positive odd integer
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)

# Bilateral blur
# the bilateral blur is a non-linear filter
# it preserves the edges of the image
# the first parameter is the image, the second parameter is the diameter of the pixel neighborhood
# the third parameter is the standard deviation in color
# the fourth parameter is the standard deviation in space
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
