import cv2
import numpy as np
import matplotlib.pyplot as plt
f = cv2.imread("demo.jpg",0)
plt.figure(figsize=(3,3))
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.title("Original Image")
plt.show()
#lpf
F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
#blpf
M,N = f.shape
H = np.zeros((M,N), dtype=np.float32)
D0 = 10 
n = 10 
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = 1 / (1 + (D/D0)**n)
#hpf
Gshift = Fshift * H
#bhpf
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.title("Butterworth low pass Filter")
plt.show()
HPF = np.zeros((M,N), dtype=np.float32)
D0 = 10
n = 1
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        HPF[u,v] = 1 / (1 + (D0/D)**n)
Gshift = Fshift * HPF
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.title("Butterworth high pass Filter")
plt.show()