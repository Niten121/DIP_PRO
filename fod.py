
import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img0 = cv2.imread('demo.jpg',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

# import cv2
# import numpy as np
# img = cv2.imread('demo.jpg',0)
# m = img.shape[0]
# n = img.shape[1]
# cv2.imshow('Original Image:',img)
#
#
# temp1 = np.zeros([m, n])
# temp2 = np.zeros([m, n])
#
# for i in range(0, m-1):
#     for j in range(0 , n-1):
#         temp1[i,j]=img[i+1,j]-img[i,j]
#         temp2[i,j]=img[i,j+1]-img[i,j]
#
# temp1= temp1.astype(np.uint8)
# temp2= temp2.astype(np.uint8)
# cv2.imshow('First X:',temp1)
# cv2.imshow('First Y:',temp2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()