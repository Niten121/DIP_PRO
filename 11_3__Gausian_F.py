import cv2
import numpy as np
import matplotlib.pyplot as plt
f = cv2.imread("demo.jpg",0)
plt.figure(figsize=(5,5))
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.title("Original Image")
plt.show()
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
#lpf
M,N = f.shape
H = np.zeros((M,N), dtype=np.float32)
D0 = 10
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = np.exp(-D**2/(2*D0*D0))
#glpf
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.figure(figsize=(5,5))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.title("Gaussian Low Pass Filter")
plt.show()
#hpf
HPF = 1 - H
#ghpf
Gshift = Fshift * HPF
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.figure(figsize=(5,5))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.title("Gaussian High Pass Filter")
plt.show()

