import random
x = object()
age = [x] * 10
i = 0
for j in age:
	age[i] = int(random.gauss(40,10))
	if age[i] < 20:
		age[i] = age[i] + 20	
	print "%d" % age[i]
	i=i+i

