primes = [2]

def isPrime(n):
	for p in primes:
		if n % p == 0:
			return False
	else:
		primes.append(n)
		return True

cur_p = 3

while True:
	isPrime(cur_p)
	if len(primes) == 10001:
		print primes[-1]
		break
	cur_p += 1