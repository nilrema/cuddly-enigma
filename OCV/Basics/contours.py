import cv2 as cv
import numpy as np

img = cv.imread('Photos/Photo1.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8') # create a blank image

# contours are the boundaries of objects
# we can use contours to detect the edges of objects

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert to grayscale
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) # apply gaussian blur
canny = cv.Canny(blur, 125, 175) # apply canny edge detection
cv.imshow('Canny Edges', canny)

#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # apply threshold
#cv.imshow('Thresh', thresh)

# hierarchy is the relationship between contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # find contours
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,255,255), 1) # draw contours on the blank image
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
