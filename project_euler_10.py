import math
primes = [2]

def isPrime(n):
	for p in primes:
		if n % p == 0:
			return False
	else:
		print n
		primes.append(n)
		return True

limit = 2 * 10 ** 6
cur_n = 3
while cur_n < limit:
	isPrime(cur_n)
	cur_n += 1

print math.fsum(primes)