import random
import numpy as np
x = object()
max = 50
age = []
cigs = []
fv = []
for j in range(0,max):
	rga = int(random.gauss(40,10))
	rgc = int(random.gauss(10,2))
	age.append(rga)
	cigs.append(rgc)
	if age[j] < 20:
		age[j] = age[j] + 20
	if cigs[j] < 0:
		cigs[j]=0	
	fv_x = np.matrix([age[j],cigs[j]])
	fv.append(fv_x)
#print fv
m = np.mean(fv,0,int)
print m
v = np.var(fv,0,int)
print v
