import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math

                                    # Original image/identity
ref = cv2.imread('demo.jpg')
img = ref
h=img.shape[0]
w= img.shape[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
                                         #log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1+ img)
 # Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)
# Save the output.
cv2.imshow("original img", ref)
cv2.imshow('log_transformed', log_transformed)
#
                                        # gamma values.
for gamma in [0.2, 0.5, 1.2, 2.2]:
    # Apply gamma correction.
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')
    cv2.imshow('gamma_transformed', gamma_corrected)
    cv2.waitKey(2000)
    # Save edited images.
cv2.imshow('gamma_transformed', gamma_corrected)

                                # negative transformation
height = img.shape[0]
print("height",height)
width = img.shape[1]
print('width', width)
neg = ~img
neg1 = abs(255-img)
# Display the negative image
cv2.imshow("negative", neg)
cv2.imshow("negative1", neg1);
#                 log inverse
for i in range(0,h):
    for j in range (0,w):
        img[i][j]= np.exp(img[i][j])
cv2.imshow('inv log_transformed', img)
#
plt.hist(img.ravel(), 255, [0,255], color="blue")
plt.hist(log_transformed.ravel(), 255, [0,255], color="blue")
# plt.hist(gamma.ravel(), 255, [0, 255], color="green")
plt.hist(neg.ravel(), 255, [0,255], color="red")
plt.hist(gray.ravel(), 255, [0,255], color="gray")
# # plt.axvline(color='black')
# plt.plot(log_transformed, img)
# plt.plot(np.log(log_transformed))
plt.title("Pixel Intensities And Counts In Enhanced Image", color="crimson")
plt.ylabel("Number Of Pixels Belonging To Pixel Intensity", color="crimson")
plt.xlabel("Pixel Intensity", color="crimson")
plt.show()
cv2.waitKey(0)

