import time
import sys

import matplotlib.pyplot as plt
import numpy as np

n=1
step = float(sys.argv[1])
target = float(sys.argv[2])

x0 = 0
y0 = 1

xn = x0
yn = y0

XPoints = []
YPoints = []

def F (x, y):
	return x + y

def Xn (n ,h):
	return x0 + n * h

def Yn (n, h):
	return (yn + h * F(xn, yn))

print('List of points:')

while True:
	#Print point
	print(f'({xn:.3f},  {yn:.3f})')
	XPoints.append(xn)
	YPoints.append(yn)
	#time.sleep(0.3)
	#Step
	xn = Xn(n, step)
	yn = Yn(n, step)
	n = n + 1

	if(xn > target):
		break

plt.plot(XPoints, YPoints)
plt.show()
