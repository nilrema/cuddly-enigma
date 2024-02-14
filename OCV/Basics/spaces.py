import cv2 as cv

img = cv.imread('Photos/Photo1.jpg')

# color spaces are different color representations
# we can convert an image to different color spaces
# some of the most common color spaces are:
# BGR, Grayscale, HSV, L*a*b, YUV

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)
