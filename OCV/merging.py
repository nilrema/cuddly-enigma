import cv2 as cv
import numpy as np

img = cv.imread('Photos/Photo1.jpg')

# create a blank image with the same dimensions as the original image
blank = np.zeros(img.shape[:2], dtype='uint8')

# we can split the image into its color channels
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank]) # merge the blue channel with the blank image
green = cv.merge([blank, g, blank]) # merge the green channel with the blank image
red = cv.merge([blank, blank, r]) # merge the red channel with the blank image

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(b.shape)
print(g.shape)
print(r.shape)

merge_image = cv.merge([b, g, r]) # pass in a list of the channels
cv.imshow('Merged Image', merge_image)

cv.waitKey(0)   
