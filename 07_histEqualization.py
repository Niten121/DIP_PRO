import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('demo.jpg',0)

equ= cv2.equalizeHist(img)
res=np.hstack((img,equ))

cv2.imshow("image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(img.ravel(), 256, [0,256], color="r")
plt.title("Pixel Intensities And Counts In Enhanced Image", color="crimson")
plt.ylabel("Number Of Pixels Belonging To Pixel Intensity", color="crimson")
plt.xlabel("Pixel Intensity", color="crimson")
plt.show()

plt.hist(res.ravel(), 256, [0,256], color="b")
plt.title("Pixel Intensities And Counts In Enhanced Image", color="crimson")
plt.ylabel("Number Of Pixels Belonging To Pixel Intensity", color="crimson")
plt.xlabel("Pixel Intensity", color="crimson")
plt.show()