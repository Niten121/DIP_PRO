from PIL import Image
import numpy as np
img = Image.open('images.jpeg').convert('L')
img.show(title="Gray Image")
#contrast
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        pixelColor = img.getpixel((i,j))
        minI=90
        maxI=225
        minO=0
        maxO=255
        pixel=round((pixelColor-minI)*(((maxO-minO)/(maxI-minI))+minO))
        img.putpixel((i,j),(pixel))
img.show(title='contrast')
#binarization
thresh = int(input("Enter threshold value"))
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
      if img.getpixel((i,j)) < thresh:
        img.putpixel((i,j),0)
      else:
        img.putpixel((i,j),255)
img.show(title='Binarization')
#Slicing
img2 = Image.open("images.jpeg").convert('L')
slicingF = int(input("Enter first slicing value"))
slicingL = int(input("Enter last slicing value"))
for i in range(0, img2.size[0]-1):
    for j in range(0, img2.size[1]-1):
      if img2.getpixel((i,j)) >= slicingF and img2.getpixel((i,j)) <= slicingL :
        img2.putpixel((i,j),255)
      else:
        img2.putpixel((i,j),0)
img2.show(title='Slicing')