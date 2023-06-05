import cv2
import numpy as np
import math as m
from statistics import pvariance
                        # orginal image
img = cv2.imread('demo.jpg',0)
or_mean = img.mean()
print("original mean",str(or_mean))
or_var = np.var(img)
print('original variance ',str(or_var))

img = img/255

cv2.imshow('original image', img)

# blank image
x,y = img.shape
g = np.zeros((x,y), dtype=np.float32)
# salt and pepper amount
pepper = 0.1
salt = 0.95
# # create salt and peper noise image
for i in range(x):
    for j in range(y):
        rdn = np.random.random()
        print(str(rdn))
        if rdn < pepper:
            g[i][j] = 0
        elif rdn > salt:
            g[i][j] = 1
        else:
            g[i][j] = img[i][j]
cv2.imshow('salt paper noise', g)
p_mean = g.mean()
print('paper mean is ', str(p_mean))
pap_var = np.var(g)
print('paper variance ',str(pap_var))

x, y = img.shape
a = 0
b = 0.2
n = np.zeros((x,y), dtype=np.float64)
for i in range(x):
    for j in range(y):
        n[i][j] = np.random.uniform(a,b)
uni = img + n
cv2.imshow('uniform noise', uni)
uni_mean = uni.mean()
print('uniform mean is ',str(uni_mean))
uni_var = np.var(uni)
print('original variance ',str(uni_var))

x, y = img.shape
mean = 0
var = 0.01
sigma = np.sqrt(var)
n = np.random.normal(loc=mean,
                     scale=sigma,
                     size=(x,y))
gaussian = img + n
cv2.imshow('Gaussian noise', gaussian)
gau_mean = gaussian.mean()
print('gaussian mean is ',str(gau_mean))
gau_var = np.var(gaussian)
print('original variance ',str(gau_var))
        #rayleigh noise
x, y = img.shape
a = 0
b = 0.2
n = np.zeros((x,y), dtype=np.float64)
for i in range(x):
    for j in range(y):
        n[i][j] = np.random.rayleigh()
rn = img + n
cv2.imshow('rayleigh',rn)

cv2.waitKey(0)
cv2.destroyAllWindows()
