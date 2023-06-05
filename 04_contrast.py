import cv2
import numpy as np

def pixelVal(pix, r1, s1, r2, s2):
	if (0 <= pix and pix <= r1):
		return (s1 / r1)*pix
	elif (r1 < pix and pix <= r2):
		return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
	else:
		return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
img = cv2.imread('demo.jpg',0)
cv2.imshow('Original',img)
# Define parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255

pixelVal_vec = np.vectorize(pixelVal)

contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

cv2.imwrite('contrast_stretch.jpg', contrast_stretched)
cv2.imshow('contrast_stretch.jpg', contrast_stretched)
#binarization
thresh = int(input("Enter threshold value"))
for i in range(0, contrast_stretched.size[0]-1):
    for j in range(0, contrast_stretched.size[1]-1):
      if img.getpixel((i,j)) < thresh:
        img.putpixel((i,j),0)
      else:
        img.putpixel((i,j),255)
img.show(title='Binarization')
cv2.waitKey(0)