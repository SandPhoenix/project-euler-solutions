import math

def prod(l):
	a = 1
	for term in l:
		a *= int(term)
	return a

def findTriplet():
	n = 1
	results = []
	sublist = []
	while True:
		p = n**2
		sublist.append(p)
		for p1 in sublist:
			for p2 in sublist:
				if p1 + p2 == p:
					res = [math.sqrt(p1),math.sqrt(p2),n]
					pr = math.fsum(res)
					print res,pr
					if pr == 1000:
						print 'result: ',res, prod(res)
						return res
		n += 1

findTriplet()