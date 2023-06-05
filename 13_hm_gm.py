import cv2
import numpy as np

img = cv2.imread('img1.png', 0)
m, n = img.shape[0], img.shape[1]
cv2.imshow('Original Image:', img)
mask = np.ones([3, 3], dtype=int)
mask = mask / 9

# 3X3 mask over the image mean
img_new = np.zeros([m, n])

for i in range(1, m - 1):
    for j in range(1, n - 1):
        img_new[i, j] = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
        img_new[i, j] = m * n / (1 / img_new[i, j])

img_new = img_new.astype(np.uint8)
cv2.imshow('After Harmonic Mean:', img_new)
# 3x3 mask over image median
img_new1 = np.zeros([m, n])
for i in range(1, m - 1):
    for j in range(1, n - 1):
        img_new1[i, j] = (img[i - 1, j - 1],mask[0, 0] * img[i-1, j] * mask[0, 1] * img[i-1, j + 1] * mask[0, 2] * img[i, j-1] * mask[1, 0], img[i, j] * mask[1, 1] * img[i, j + 1] * mask[1, 2] * img[i + 1, j-1] * mask[2, 0] * img[i + 1, j] * mask[2, 1] * img[i + 1, j + 1] * mask[2, 2]) * 1 / (m * n)
img_new1 = img_new1.astype(np.uint8)
cv2.imshow('Image After Geometric Filter:', img_new1)

cv2.waitKey(0)
cv2.destroyAllWindows()