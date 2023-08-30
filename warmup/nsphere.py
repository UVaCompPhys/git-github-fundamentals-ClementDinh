import math
import matplotlib.pyplot as plt

def volume(dim,rad):
	g = math.gamma((dim/2)+1)
	return (pow(math.pi,dim/2)*pow(rad,dim))/g


rad = 1;

for x in range(0,20):
	dim = []
	vol = []

	for y in range(0,50):
		dim.append(y)
		vol.append(volume(y,rad))
	
	plt.plot(dim,vol)
	rad += 0.05

plt.show()	
