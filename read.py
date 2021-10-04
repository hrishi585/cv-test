import cv2 as cv

# Reading Images
# img = cv.imread('Photos/cat3.jpg')
# cv.imshow('cat',img)
# cv.waitKey(0)

# Reading videos
vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
vid.release()
cv.destroyAllWindows()

