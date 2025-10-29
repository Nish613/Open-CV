import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')#uint8 is image datatype; 3 is the no of colour channels RGB
#cv.imshow('Blank',blank)

#1.Paint the image a certain colour
'''blank[200:300,300:400] = 0,0,255
cv.imshow('Red_reduced',blank)

blank [:] = 0,255,0 #[:] means all pixels ie full img is coloured (255,255,255) is white
cv.imshow('Green',blank)

blank[:] = 255,0,0
cv.imshow('Blue',blank)

blank[:] = 0,0,255
cv.imshow('Red',blank)

#2.Make a rectangle
cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=4) #1st point,2nd point,colour,thickness of line
cv.imshow('Rectangle',blank)

cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=cv.FILLED) #1st point,2nd point,colour,filled rectangle or u can dothickness=-1 for filled rect
cv.imshow('Rectangle',blank)


#3.Make a circle
cv.circle(blank,(250,250),100,(0,255,0),thickness=-1) #100 is the radius
cv.imshow('Circle',blank)


#4.Make a line
cv.line(blank,(0,0),(blank.shape[1],blank.shape[0]),(255,255,255),thickness=5) 
cv.imshow('Line',blank)
cv.waitKey(0)'''

#5.Write text on image
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2) #1.0 is the size of text and 2 is the thickness of font
cv.imshow('Text',blank)
cv.waitKey(0)