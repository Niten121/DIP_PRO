# # importing required libraries
# import numpy as np
# import mahotas
# import cv2
# from pylab import imshow, show
#
# # loading image
# img = mahotas.imread('demo.jpg')
#
# # filtering the image
# img = img[:, :, 0]
#
# print("Image with filter")
# # showing the image
# imshow(img)
# show()
#
# # getting mean value
# mean = img.mean()
# median = cv2.medianBlur(img,5)
#
# # printing mean value
# print("Mean Value for 0 channel : " + str(mean))
# cv2.imshow('median img',median)
# cv2.waitKey(0)
#
import cv2
import numpy as np

img = cv2.imread('demo.jpg',0)
m, n = img.shape[0], img.shape[1]
cv2.imshow('Original Image:', img)
mask = np.ones([3, 3], dtype=int)
mask = mask / 9

# 3X3 mask over the image mean
img_new = np.zeros([m, n])

for i in range(1, m - 1):
    for j in range(1, n - 1):
        img_new[i, j] = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]

img_new = img_new.astype(np.uint8)
cv2.imshow('After Mean:', img_new)
# 3x3 mask over image median
img_new1 = np.zeros([m, n])
for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = [img_new[i - 1, j - 1], img_new[i - 1, j], img_new[i - 1, j + 1], img_new[i, j - 1], img_new[i, j],img_new[i, j + 1], img_new[i + 1, j - 1], img_new[i + 1, j], img_new[i + 1, j + 1]]
temp = np.sort(temp)
img_new1[i, j] = temp[1]
img_new1 = img_new1.astype(np.uint8)
cv2.imshow('Image After median Filter:', img_new1)

cv2.waitKey(0)
cv2.destroyAllWindows()
