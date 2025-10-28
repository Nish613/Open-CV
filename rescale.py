import cv2 as cv

def rescaleFrame(frame,scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)#when we resize an img interpolation adjusts pixels and colour to match it 

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat',img)
resized_img = rescaleFrame(img)
cv.imshow('Cat_resized',resized_img)
cv.waitKey(0)

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video_resized',frame_resized)

    if cv.waitKey(20)&0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
