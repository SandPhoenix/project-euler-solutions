
results = [[0,0]]
start = 10**6

while start > 1:
	n = start
	c = 0
	while n > 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3*n+1
		c += 1
	m = max([i[0] for i in results])
	# print m
	if c > m:
		results.append([c,start])
		print c,start
	start -= 1


