import cv2 as cv

img = cv.imread('Photos\cat.jpg')
#cv.imshow('Cat',img)

#Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#Blurring an image
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) #7,7 is the kernal size to increase blur increase the no.
#cv.imshow('Blur',blur)

#Edge cascade
canny = cv.Canny(img,125,175)
canny_blur = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)
cv.imshow('Canny_blur',canny_blur) #reduced edges after blurring

#Dilating the image
dilated = cv.dilate(canny_blur,(7,7),iterations = 5)
cv.imshow('Dilated',dilated)

#Eroding 
eroded = cv.erode(dilated,(7,7),iterations = 5)
cv.imshow('Eroded',eroded)

#Resize
resized = cv.resize(img,(500,500),interpolation = cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)