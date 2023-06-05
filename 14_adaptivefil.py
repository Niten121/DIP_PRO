from PIL import Image
import random
import math
import matplotlib.pyplot as plt


im = Image.open('demo.jpg').convert('L')
size = im.size
noise = Image.new("L", im.size)
temp = Image.new("L", im.size)
diff = Image.new("L", im.size)
output = Image.new("L", im.size)


iset = 0
rand1 = -1
rand2 = -1
var = 100
for i in range(0, size[0]):
	for j in range(0, size[1]):
		
		if(iset == 0):
			r = 0
			
			while(r >= 1.0 or r == 0):
				temp1 = random.uniform(-1,1)
				temp2 = random.uniform(-1,1)
				r = temp1 ** 2 + temp2 ** 2;
			fac = (-2.0 * math.log(r) / r) ** 0.5;
			
			rand1 = int(temp1 * fac * (var ** 0.5));
			rand2 = int(temp2 * fac * (var ** 0.5));
			iset = 1;
			
			l = im.getpixel((i,j)) + rand2
		
			noise.putpixel((i,j), rand2)
		
		if(iset == 1):
			iset = 0;
			l = im.getpixel((i,j)) + rand1
			noise.putpixel((i,j), rand1)
		
		temp.putpixel((i,j), l)


ignore = int((3 - 1) / 2)


for i in range(0 + ignore, size[0] - ignore):
	for j in range(0 + ignore, size[1] - ignore):
		
		p1 = temp.getpixel((i-1,j-1))
		p2 = temp.getpixel((i,j-1))
		p3 = temp.getpixel((i+1,j-1))
		p4 = temp.getpixel((i-1,j))
		p5 = temp.getpixel((i,j))
		p6 = temp.getpixel((i+1,j))
		p7 = temp.getpixel((i-1,j+1))
		p8 = temp.getpixel((i,j+1))
		p9 = temp.getpixel((i+1,j+1))
		
		ap = (p1+p2+p3+p4+p5+p6+p7+p8+p9)/9
		
		ap2 = (p1**2+p2**2+p3**2+p4**2+p5**2+p6**2+p7**2+p8**2+p9**2)/9
		vp = (p1-ap) ** 2 + (p2-ap) ** 2 + (p3-ap) ** 2 + (p4-ap) ** 2 + (p5-ap) ** 2 + (p6-ap) ** 2 + (p7-ap) ** 2 + (p8-ap) ** 2 + (p9-ap) ** 2
		
		vp2 = ap2 - ap ** 2
		
		interval = 1000
		
		if(vp2 < var):
			l = temp.getpixel((i,j)) - (var / vp2) * (temp.getpixel((i,j)) - ap)
		
		elif(vp2 < var + interval):
			l = temp.getpixel((i,j)) - (var / vp2) * (temp.getpixel((i,j)) - ap)
		
		else:
			l = temp.getpixel((i,j))

		
		output.putpixel((i,j), int(l))


for i in range(0, size[0]):
	for j in range(0, size[1]):
		
		if (temp.getpixel((i,j)) != output.getpixel((i,j))):
			a=255
		else:
			a=0
		diff.putpixel((i,j),a)

plt.title("output")
plt.imshow(output)
plt.show()

plt.title("temp")
plt.imshow(temp)
plt.show()
plt.title("noise")
plt.imshow(noise)
plt.show()
plt.title("diff")
plt.imshow(diff)
plt.show()


