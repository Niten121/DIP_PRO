
import cv2
import numpy as np
img = cv2.imread('demo.jpg', 0)
m, n = img.shape[0],img.shape[1]
cv2.imshow('Original Image:',img)
mask = np.ones([3, 3], dtype = int)
mask = mask / 9

img1 = np.zeros([m, n])

for i in range(1, m):
	for j in range(1, n):
		img1[i, j] = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2]
		img1[i,j]=m*n/(1/img1[i,j])
		
		
img1 = img1.astype(np.uint8)
cv2.imshow('After Harmonic Mean:',img1)

img11=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        img11[i, j] = (img[i-1, j-1]*mask[0, 0]*img[i-1, j]*mask[0, 1]*img[i-1, j + 1]*mask[0, 2]*img[i, j-1]*mask[1, 0]* img[i, j]*mask[1, 1]*img[i, j + 1]*mask[1, 2]*img[i + 1, j-1]*mask[2, 0]*img[i + 1, j]*mask[2, 1]*img[i + 1, j + 1]*mask[2, 2])**1/(m*n)
img11 = img11.astype(np.uint8)
cv2.imshow('Image After Geometric Filter:',img11)		
    
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
from PIL import Image,ImageFilter,ImageOps
import cv2
im=Image.open('median.png')
img=ImageOps.grayscale(im)
min_img=img.filter(ImageFilter.MinFilter(size=3))
max_img=img.filter(ImageFilter.MaxFilter(size=3))
median_img=img.filter(ImageFilter.MedianFilter(size=3))
#mid_point=min_img+max_img
img.show()
median_img.show()
min_img.show()
max_img.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

'''