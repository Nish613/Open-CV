import cv2 as cv
import numpy as np

img = cv.imread('black.jpeg')

lab_img = cv.cvtColor(img,cv.COLOR_BGR2LAB)
l,a,b = cv.split(lab_img)

equ = cv.equalizeHist(l)

cv.imshow('Black_new',equ)
cv.waitKey(0)