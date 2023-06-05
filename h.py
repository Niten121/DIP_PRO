import cv2
import numpy as np

input_image = np.array((
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 0, 0, 255, 255, 0],
    [0, 255, 255, 0, 0, 255, 255, 0],
    [0, 255, 255, 0, 0, 255, 255, 0],
    [0, 255, 255, 255, 255, 255, 255, 0],
    [0, 255, 255,255, 255, 255, 255, 0],
    [0, 255, 255, 0, 0, 255, 255, 0],
    [0,255, 255, 0, 0, 255, 255, 0],
    [0, 255, 255, 0, 0, 255, 255, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]), dtype="uint8")
input_image = cv2.resize(input_image, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Original", input_image)

kernel = np.array((
    [0, 255, 0],
    [255, 255, 255],
    [0, 255, 0]), dtype="int")
# kernel = (kernel + 1)
kernel = np.uint8(kernel)
kernel = cv2.resize(kernel, None, fx=50, fy=50, interpolation=cv2.INTER_NEAREST)
cv2.imshow("kernel", kernel)

cv2.waitKey(0)