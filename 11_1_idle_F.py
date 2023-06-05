import cv2
import numpy as np
import math as m
import matplotlib.pyplot as plt
f = cv2.imread("demo.jpg",0)
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.title("Original Image")
plt.show()
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
# lpf
M,N = f.shape
H = np.zeros((M,N), dtype=np.float32)
D0 = 50
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        if D <= D0:
            H[u,v] = 1
        else:
            H[u,v] = 0
# ilpf
Gshift = Fshift* H
# Inverse Fourier Transform
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.title("Ideal Low Pass Filter")
plt.show()
# hpf
H = 1 - H
# ihpf
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.title("Ideal High Pass Filter")
plt.show()