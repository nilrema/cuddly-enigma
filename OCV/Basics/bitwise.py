import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8') # create a blank image
img = cv.imread('Photos/Photo1.jpg')

# there are four bitwise operations: AND, OR, XOR, and NOT
# we can use these operations to combine images
# we can use these operations to create a mask
# we can use these operations to extract a part of an image
# we can use these operations to remove a part of an image
# we can use these operations to apply an effect to a part of an image

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1) # create a rectangle
cirlce = cv.circle(blank.copy(), (200, 200), 200, 255, -1) # create a circle

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', cirlce)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, cirlce)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, cirlce)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, cirlce)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)
