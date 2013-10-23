from scipy import stats
import random
import numpy as np
import matplotlib.pyplot as plt
import math as mt
x = object()
max = 100
age = []	#age distribution
cigs = []	#cig distribution
pcan = []	#prior probabilities
fv = []		#feature vectors array

for j in range(0,max):			#generate gaussian distribution for age[],cigs[] and fv[]
	rga = int(random.gauss(40,10))
	rgc = int(random.gauss(10,2))
	rp = random.randint(0,2)
	age.append(rga)
	cigs.append(rgc)
	pcan.append(rp)
	if age[j] < 20:
		age[j] = age[j] + 20
	if age[j] > 80:
		age[j] = age[j]-(age[j]-80)
	if cigs[j] < 0:
		cigs[j]=0	
	fv_x = ([age[j],cigs[j]])
	fv.append(fv_x)

#Prior probability calculations
count_0, count_1, count_2 = 0,0,0

for i in range(0,max):
	if pcan[i] == 0:
		count_0+= 1
	elif pcan[i] == 1:
		count_1+= 1
	else:

		count_2+= 1
prior = [float(count_0)/max, float(count_1)/max, float(count_2)/max]

#Parameter estumation using MLE
m = np.mean(fv,0,int)	#Mean Estimate
v = np.cov(fv,None,0)	#Covariance estimate

sigma_1 = np.sqrt(np.var(age,0,int))	#standard deviation of age
sigma_2 = np.sqrt(np.var(cigs,0,int))	#	,,	    of cigs


h1=1.06*sigma_1*pow(max,-0.2)
h2=1.06*sigma_2*pow(max,-0.2)

#Parzen window function
def fun_K(u):
	if (u > -0.5 and u < 0.5):
		return 1
	else:
		return 0

#KDE 
def fun_Ktot(x):
	t = 0
	for i in range(0,max):
		t+= fun_K((x-age[i])/h1)
	return t

P = 0
tp = 0
Prob=[]
for k in range(0,max):
	P=fun_Ktot(k)/(max*h1)
	tp+=P	
	Prob.append(P)
	P=0
print tp

#Plot age
m1 = np.array(age)
m2 = np.array(Prob)
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()
plt.axis([xmin,xmax,ymin,ymax])
dist_space = np.linspace(xmin, xmax,max)
plt.plot( dist_space, Prob )
plt.show()
