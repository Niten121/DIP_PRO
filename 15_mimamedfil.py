# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
# creating a image object
img = Image.open("demo.jpg")

# applying the min filter
im1 = img.filter(ImageFilter.MinFilter(size = 3))
plt.title("min filter")
plt.imshow(im1)
plt.show()
# Importing Image and ImageFilter module from PIL package
# applying the max filter
im2 = img.filter(ImageFilter.MaxFilter(size = 3))
plt.title("max filter")
plt.imshow(im2)
plt.show()
# applying the max filter
im3 = img.filter(ImageFilter.MedianFilter(size = 3))
plt.title("median filter")
plt.imshow(im3)
plt.show()