import cv2
import matplotlib
import numpy as np

img = cv2.imread('C:/Users/sethy/PycharmProjects/DIP/demo.jpg')
height = img.shape[0]
print("height",height)
width = img.shape[1]
print('width', width)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale=3
rows = int(img.shape[0]*scale)
cols = int(img.shape[1]*scale)

zoomed = np.zeros((rows,cols),dtype=img.dtype)
for i in range (0 , rows):
    for j in range(0, cols):
        zoomed[i,j]= gray[int(i/scale), int(j/scale)]

height = zoomed.shape[0]
print("height", height)
width = zoomed.shape[1]
print('width', width)

cv2.imshow('image', img)
cv2.imshow('gray', gray)
cv2.imshow('zoomed', zoomed)
cv2.waitKey(0)

cv2.destroyAllWindows()