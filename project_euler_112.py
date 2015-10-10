def isDec(n):
	n = str(n)
	for i,digit in enumerate(n):
		if i == 0: continue
		if int(digit) > int(n[i-1]):
			break
	else:
		return True
	return False

def isInc(n):
	n = list(str(n))
	n.reverse()
	n = ''.join(n)
	return isDec(n)

def isBouncy(n):
	if isInc(n) == False and isDec(n) == False:
		return True
	else:
		return False

b = 0

for i in range(1,10**7):
	if isBouncy(i):
		b += 1
	perc = 100.0 * b / i
	print perc,i
	if perc == 99: break