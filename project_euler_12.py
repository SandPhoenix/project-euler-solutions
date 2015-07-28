import math

n = 2

def findDiv(u):
	div = []
	for i in range(1,u):
		if u % i == 0:
			div.append(i)
	return div


while True:
	n += 1
	n = int(math.fsum(range(n)))
	d = findDiv(n)
	l =  len(d)
	print l
	if l > 500:
		print n,len(l)
		break
