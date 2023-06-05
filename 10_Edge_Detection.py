import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('demo.jpeg')
cv2.imshow('Original', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  # Sobel Edge Detection on the Y axis
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)  # Canny Edge Detection
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)


laplacian = cv2.Laplacian(img_blur, 5, cv2.CV_64F)
filtered_image = cv2.convertScaleAbs(laplacian)
plt.figure(figsize=(18, 19))
plt.subplot(121)
plt.imshow(img_blur, cmap='gray')
plt.title('Original')
plt.axis("off")

plt.subplot(122)
plt.imshow(filtered_image, cmap='gray')
plt.title('Edge image')
plt.axis("off")
plt.show()

cv2.destroyAllWindows()