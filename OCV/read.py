import cv2 as cv

#img = cv.imread('Photos/Photo1.jpg')
#cv.imshow('Photo1', img)

# downscale the image, it is good practice to downscale the image
def rescaleFrame(frame, scale=0.75):
    # works for images, videos, and live videos
    width = int(frame.shape[1] * scale) # frame.shape[1] is the width of the frame
    height = int(frame.shape[0] * scale) # frame.shape[0] is the height of the frame
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only works for live video
    capture.set(3, width) # 3 is the width of the frame
    capture.set(4, height) # 4 is the height of the frame

capture = cv.VideoCapture('Videos/Video1.mp4') # read the video file
while True:
    isTrue, frame = capture.read() # read each frame of the video
    frame_resized = rescaleFrame(frame, scale=0.2) # rescale the frame

    cv.imshow('Video1', frame) # show each frame of the video
    cv.imshow('Video1 Resized', frame_resized) # show each frame of the video

    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter d is pressed, break the loop
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0) # 0 means wait for any key to be pressed
