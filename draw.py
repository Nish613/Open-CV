import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')#uint8 is image datatype; 3 is the no of colour channels RGB
cv.imshow('Blank',blank)

#1.Paint the image a certain colour
'''blank[200:300,300:400] = 0,0,255
cv.imshow('Red_reduced',blank)

blank [:] = 0,255,0 #[:] means all pixels ie full img is coloured
cv.imshow('Green',blank)

blank[:] = 255,0,0
cv.imshow('Blue',blank)

blank[:] = 0,0,255
cv.imshow('Red',blank)'''

#2.Make a rectangle
cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=4) #1st point,2nd point,colour,thickness of line
cv.imshow('Rectangle',blank)

cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=cv.FILLED) #1st point,2nd point,colour,filled rectangle
cv.imshow('Rectangle',blank)
cv.waitKey(0)