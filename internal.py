import cv2 as cv
import numpy as np

img = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 255, 255, 0, 0, 255,255,0],
    [0, 0, 255, 255, 0, 0, 255,255,0],
    [0, 0, 255, 255, 255, 255, 255,255,0],
    [0, 0, 255, 255, 0, 0, 255,255,0],
    [0, 0, 255, 255, 0, 0, 255, 255, 0],
    [0, 0, 0, 0, 0, 0, 0, 0,0]), dtype="uint8")

kernel = np.array((
    [1,0,0],
    [0,-2,0],
    [0,0,1]

    ), dtype="uint8")

op = cv.morphologyEx(img, cv.MORPH_HITMISS, kernel)
rate = 50
kernel = cv.resize(kernel, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
cv.imshow("kernel", kernel)

img = cv.resize(img, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
cv.imshow("Original", img)

op = cv.resize(op, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
cv.imshow("Hit or Miss", op)

cv.waitKey(0)
