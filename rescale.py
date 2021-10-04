import cv2 as cv

img = cv.imread('Photos/cat4.jpg')
cv.imshow('cat',img)

# Resizing image
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resizedImage = rescaleFrame(img)
cv.imshow('Resized image', resizedImage)

cv.waitKey(0)

# Changing Resolution of video
# Only for live video
def changeRes(width,height):
    vid.set(3,width)
    vid.set(4,height)


# Resizing video
vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()
    # Rescale frame
    # for images, video and live video
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Resized video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
vid.release()
cv.destroyAllWindows()