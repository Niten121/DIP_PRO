import cv2
import numpy as np

img = cv2.imread('C:/Users/sethy/PycharmProjects/DIP/demo.jpg')
height = img.shape[0]
print("height", height)
width = img.shape[1]
print('width', width)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale = 2
rows = int(img.shape[0]/scale)
cols = int(img.shape[1]/scale)

shrink = np.zeros((rows, cols), dtype=img.dtype)
for i in range(0, rows):
    for j in range(0, cols):
        shrink[i, j] = gray[int(i*scale), int(j*scale)]

scale = 2
rows = int(img.shape[0]*scale)
cols = int(img.shape[1]*scale)
zoom = np.zeros((rows, cols), dtype=img.dtype)
for i in range(0, rows):
    for j in range(0, cols):
        zoom[i, j] = gray[int(i/scale), int(j/scale)]

height = shrink.shape[0]
print("height", height)
width = shrink.shape[1]
print('width', width)
height1 = zoom.shape[0]
print("height", height1)
width1 = zoom.shape[1]
print('width', width1)

cv2.imshow('image', img)
cv2.imshow('gray', gray)
cv2.imshow('Shrinked', shrink)
cv2.imshow('Zooming', zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()