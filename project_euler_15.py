import math
r = []
r.append([1 for i in range(22)])
for i_1 in range(20):
	t = [1]
	for i_2 in range(1,21):
		t.append(t[-1]+r[-1][i_2])
	r.append(t)
for i in r:print i