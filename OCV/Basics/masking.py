import cv2 as cv
import numpy as np

img = cv.imread('Photos/Photo1.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

# masking is the process of extracting a part of an image
# we can use masking to apply an effect to a part of an image
# we can use masking to remove a part of an image

# create a mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)
