import cv2
import numpy as np
img = np.array((
    [0,    0,   0,   0  ,   0,   0,   0, 0],
    [0,    0,   0,   0  ,   0,   0,   0, 0],
    [255, 255 , 0, 0    ,   0, 0, 255, 255],
    [255, 255 , 0, 255    ,   0, 0, 255, 255],
    [255, 255 , 255, 255, 255, 255, 255, 255],
    [255, 255 , 0,   255,   0, 0, 255, 255],
    [255, 225 , 0,   0,   0, 0, 225, 255],
    [255, 225 , 0,   0,   0, 0, 225, 255],
    [0,   0 ,   0,   0,   0,   0,   0, 0],
    [0,   0 ,   0,   0,   0,   0,   0, 0]), dtype="uint8")

img = cv2.resize(img, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
kernel = np.array([[255,255,255],
                   [255,255,255],
                   [255,255,255]],dtype='uint8')
# kernel = np.ones((5, 5), np.uint8)
kernel = cv2.resize(kernel, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)
opening = img_dilation
img_dilation255 = cv2.dilate(img, kernel, iterations=1)
img_erosion255 = cv2.erode(img_dilation255, kernel, iterations=1)
closing = img_erosion255
cv2.imshow('Input', img)
cv2.imshow('structuring',kernel)
cv2.imshow("err",img_erosion)
cv2.imshow('Opening', opening)
cv2.imshow('dia',img_dilation255)
cv2.imshow('closing', closing)
cv2.waitKey(0)
