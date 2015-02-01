dig = list(reversed(range(2,21	)))

def isDiv(n):
	global dig
	for d in dig:
		if n % d != 0:
			return False
	else:
		return True

cur_n = 1

while True:
	if isDiv(cur_n):
		print '\a'
		print 'Result: ',cur_n
		break
	else:
		cur_n += 1
	if cur_n % 1000 == 0:
		print cur_n