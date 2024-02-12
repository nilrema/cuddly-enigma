import cv2 as cv
import numpy as np

img = cv.imread('Photos/Photo1.jpg')

# Translation
# shifting an image along the x and y axis
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # translation matrix
    dims = (img.shape[1], img.shape[0]) # width, height

    return cv.warpAffine(img, transMat, dims)

# if you have negative values, the image will shift to the left or up
# if you have positive values, the image will shift to the right or down

translated = translate(img, 100, 100)
#cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] # get the height and width of the image

    if rotPoint is None:
        rotPoint = (width//2, height//2) # center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # rotation matrix
    dims = (width, height)

    return cv.warpAffine(img, rotMat, dims)

rotated = rotate(img, 45)  # 45 degrees counter-clockwise
#cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

# Flipping
# 0 flips the image vertically, 1 flips the image horizontally, -1 flips the image both vertically and horizontally
flip = cv.flip(img, 1)
#cv.imshow('Flip', flip)

# Cropping
# use array slicing to crop an image
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
