import cv2
import numpy as np

# img = cv2.imread('demo.jpg', 0)
img = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 255, 0, 0, 0],
    [0, 0, 255, 255, 255, 0, 0, 0],
    [0, 0, 0, 255, 255, 255, 0, 0],
    [0, 0, 0,255, 255, 255, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0,0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]), dtype="uint8")
img = cv2.resize(img, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
kernel = np.array((
    [0, 0, 0,0,0],
    [0, 255, 255,0,0],
    [0, 255, 255,0,0],
    [0, 0,0,0,0],
    [0, 0, 0,0,0]), dtype="int")
# kernel = (kernel)*127
kernel = np.uint8(kernel)
kernel = cv2.resize(kernel, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
cv2.imshow("kernel", kernel)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow("erossion",img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey(0)