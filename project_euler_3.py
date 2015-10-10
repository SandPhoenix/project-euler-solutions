import math

n = 600851475143
max_d = 2
cur_d = 2

while n > 1:
	if n % cur_d == 0:
		n = n/cur_d
		max_d = cur_d
		cur_d = 2
	else:
		cur_d += 1
		print cur_d
