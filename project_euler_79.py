numbers = ['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']

def check(password,frag):
	digit = frag[0]
	password = str(password)
	pos = password.find(digit)
	if pos == -1:
		return False
	else:
		if len(frag)-1 == frag.index(digit):
			return True
		else:
			return check(password[pos:],frag[1:])

for password in range(10**4,10**8):
	if password % 1000 == 0: print password
	for fragment in numbers:
		if check(password,fragment) == False:
			break
	else:
		print 'pass: {}'.format(password)
		break



