import cv2
import numpy as np
img = cv2.imread('demo.jpg',0)
m, n = img.shape[0],img.shape[1]
cv2.imshow('Original Image:',img)

temp1 = np.zeros([m, n])
temp2 = np.zeros([m, n])
for i in range(0, m-1):
    for j in range(0 , n-1):
        temp1[i,j]=img[i+1,j]-2*(img[i,j])+img[i-1,j]
        temp2[i,j]=img[i,j+1]-2*img[i,j]+img[i,j-1]

temp1= temp1.astype(np.uint8)
temp2= temp2.astype(np.uint8)
cv2.imshow('second X:',temp1)
cv2.imshow('second Y:',temp2)
cv2.waitKey(0)

cv2.destroyAllWindows()