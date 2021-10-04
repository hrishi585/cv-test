import cv2 as cv

img = cv.imread('Photos/dog.jpg')
cv.imshow('dog', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#Edge cascade
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

#Crop
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)