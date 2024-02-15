import cv2 as cv

img = cv.imread('Photos/Photo1.jpg')

# we can get away with equating gradients to edges
# we will compute methods to get the edges of an image

#first convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
# it calculates the laplacian of the image
# it's good for detecting edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = cv.convertScaleAbs(lap) # convert to unsigned 8-bit integer
cv.imshow('Laplacian', lap)

# Sobel
# it calculates the gradient of the image
# it computes the gradient in the x and y direction
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # gradient in the x direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # gradient in the y direction
combined_sobel = cv.bitwise_or(sobelx, sobely) # combine the gradients
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny
# it's the most effective method for edge detection
# it applies gradient calculation, non-maximum suppression, and hysteresis thresholding
canny = cv.Canny(gray, 150, 175) # lower and upper threshold
cv.imshow('Canny', canny)


cv.waitKey(0)
