import cv2 ,argparse
import numpy as np
import math as m

# orginal image

# ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--image', required=True, help='Path to the input image')
# args = vars(ap.parse_args())

img = cv2.imread('demo.jpg',0)
img = img/255
cv2.imshow('original image', img)
x,y = img.shape
#blank image
g = np.zeros((x,y), dtype=np.float32)
pepper = 0.1
salt = 0.95

# # create salt and peper noise image
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
cv2.imshow('salt paper noise', g)
cv2.waitKey(0)
# denoise image
noise_1 = cv2.fastNlMeansDenoising(img,None ,2, 3, 7.0, 21)
cv2.imshow('denoise', noise_1)
cv2.waitKey(0)
cv2.destroyAllWindows()