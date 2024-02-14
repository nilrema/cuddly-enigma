import cv2 as cv 
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # create a blank image

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0, 255, 0 # BGR
#cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED) # thickness=cv.FILLED fills the rectangle
#cv.imshow('Rectangle', blank)

# draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1) # thickness=-1 fills the circle
#cv.imshow('Circle', blank)

# draw a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3)
#cv.imshow('Line', blank)

# write text
cv.putText(blank, 'Hello, my name is Merlin', (150, 150), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 200, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0) # 0 means wait for any key to be pressed
