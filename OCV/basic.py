import cv2 as cv

img = cv.imread('Photos/Photo1.jpg')
#cv.imshow('Photo1', img)

# Convert image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blur the image
# to increase the blur, increase the kernel size
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade
# two thresholds: low and high
# more blur, less edges
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)

# Dilating the image using a specific strucuring element
dilated = cv.dilate(canny, (7, 7), iterations=3) # iterations increases the thickness of the edges
#cv.imshow('Dilated', dilated)

# Eroding the image using a specific strucuring element
eroded = cv.erode(dilated, (7, 7), iterations=3) # iterations decreases the thickness of the edges
#cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
# images are arrays, so we can slice them
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
