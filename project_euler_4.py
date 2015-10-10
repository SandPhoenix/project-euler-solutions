def isPal(n):
	n = str(n)
	n_len = len(n)
	n_1 = n_1 = n[:n_len/2]
	n_2 = ''
	if n_len % 2 != 0:
		n_2 = n[n_len/2+1:]
	else:
		n_2 = n[n_len/2:]
	n_2 = n_2[::-1]
	if n_1 == n_2: return True
	else: return False



def findP():
	dig = list(reversed(range(1,10)))
	for a_1 in dig:
		for b_1 in dig:
			for a_2 in dig:
				for b_2 in dig:
					for a_3 in dig:
						for b_3 in dig:
							first = a_1*10**2 + a_2*10 + a_3
							second = b_1*10**2 + b_2*10 + b_3
							p = first*second
							if isPal(p):
								print p,first,second
								return p

findP()




