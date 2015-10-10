import math
import random
from z3 import *
import itertools

txt = '''
Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
Grid 02
200080300
060070084
030500209
000105408
000000000
402706000
301007040
720040060
004010003
Grid 03
000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000
Grid 04
030050040
008010500
460000012
070502080
000603000
040109030
250000098
001020600
080060020
Grid 05
020810740
700003100
090002805
009040087
400208003
160030200
302700060
005600008
076051090
Grid 06
100920000
524010000
000000070
050008102
000000000
402700090
060000000
000030945
000071006
Grid 07
043080250
600000000
000001094
900004070
000608000
010200003
820500000
000000005
034090710
Grid 08
480006902
002008001
900370060
840010200
003704100
001060049
020085007
700900600
609200018
Grid 09
000900002
050123400
030000160
908000000
070000090
000000205
091000050
007439020
400007000
Grid 10
001900003
900700160
030005007
050000009
004302600
200000070
600100030
042007006
500006800
Grid 11
000125400
008400000
420800000
030000095
060902010
510000060
000003049
000007200
001298000
Grid 12
062340750
100005600
570000040
000094800
400000006
005830000
030000091
006400007
059083260
Grid 13
300000000
005009000
200504000
020000700
160000058
704310600
000890100
000067080
000005437
Grid 14
630000000
000500008
005674000
000020000
003401020
000000345
000007004
080300902
947100080
Grid 15
000020040
008035000
000070602
031046970
200000000
000501203
049000730
000000010
800004000
Grid 16
361025900
080960010
400000057
008000471
000603000
259000800
740000005
020018060
005470329
Grid 17
050807020
600010090
702540006
070020301
504000908
103080070
900076205
060090003
080103040
Grid 18
080005000
000003457
000070809
060400903
007010500
408007020
901020000
842300000
000100080
Grid 19
003502900
000040000
106000305
900251008
070408030
800763001
308000104
000020000
005104800
Grid 20
000000000
009805100
051907420
290401065
000000000
140508093
026709580
005103600
000000000
Grid 21
020030090
000907000
900208005
004806500
607000208
003102900
800605007
000309000
030020050
Grid 22
005000006
070009020
000500107
804150000
000803000
000092805
907006000
030400010
200000600
Grid 23
040000050
001943600
009000300
600050002
103000506
800020007
005000200
002436700
030000040
Grid 24
004000000
000030002
390700080
400009001
209801307
600200008
010008053
900040000
000000800
Grid 25
360020089
000361000
000000000
803000602
400603007
607000108
000000000
000418000
970030014
Grid 26
500400060
009000800
640020000
000001008
208000501
700500000
000090084
003000600
060003002
Grid 27
007256400
400000005
010030060
000508000
008060200
000107000
030070090
200000004
006312700
Grid 28
000000000
079050180
800000007
007306800
450708096
003502700
700000005
016030420
000000000
Grid 29
030000080
009000500
007509200
700105008
020090030
900402001
004207100
002000800
070000090
Grid 30
200170603
050000100
000006079
000040700
000801000
009050000
310400000
005000060
906037002
Grid 31
000000080
800701040
040020030
374000900
000030000
005000321
010060050
050802006
080000000
Grid 32
000000085
000210009
960080100
500800016
000000000
890006007
009070052
300054000
480000000
Grid 33
608070502
050608070
002000300
500090006
040302050
800050003
005000200
010704090
409060701
Grid 34
050010040
107000602
000905000
208030501
040070020
901080406
000401000
304000709
020060010
Grid 35
053000790
009753400
100000002
090080010
000907000
080030070
500000003
007641200
061000940
Grid 36
006080300
049070250
000405000
600317004
007000800
100826009
000702000
075040190
003090600
Grid 37
005080700
700204005
320000084
060105040
008000500
070803010
450000091
600508007
003010600
Grid 38
000900800
128006400
070800060
800430007
500000009
600079008
090004010
003600284
001007000
Grid 39
000080000
270000054
095000810
009806400
020403060
006905100
017000620
460000038
000090000
Grid 40
000602000
400050001
085010620
038206710
000000000
019407350
026040530
900020007
000809000
Grid 41
000900002
050123400
030000160
908000000
070000090
000000205
091000050
007439020
400007000
Grid 42
380000000
000400785
009020300
060090000
800302009
000040070
001070500
495006000
000000092
Grid 43
000158000
002060800
030000040
027030510
000000000
046080790
050000080
004070100
000325000
Grid 44
010500200
900001000
002008030
500030007
008000500
600080004
040100700
000700006
003004050
Grid 45
080000040
000469000
400000007
005904600
070608030
008502100
900000005
000781000
060000010
Grid 46
904200007
010000000
000706500
000800090
020904060
040002000
001607000
000000030
300005702
Grid 47
000700800
006000031
040002000
024070000
010030080
000060290
000800070
860000500
002006000
Grid 48
001007090
590080001
030000080
000005800
050060020
004100000
080000030
100020079
020700400
Grid 49
000003017
015009008
060000000
100007000
009000200
000500004
000000020
500600340
340200000
Grid 50
300200000
000107000
706030500
070009080
900020004
010800050
009040301
000702000
000008006'''

sudoku = [[[int(b) for b in a] for a in i.split('\n')[1:-1]] for i in txt.split('Grid')][1:]
result = []

sudoku[49].append([int(b) for b in txt.split('\n')[-1]])

for a,sudo in enumerate(sudoku):
	# print a
	s = Solver()
	m = [[Int('z_{}_{}'.format(x,y)) for y in range(1,10)] for x in range(1,10)]
	for x in range(9):
		s.add(Distinct(m[x])) # the rows must have all different values
		s.add(Distinct([m[i][x] for i in range(9)])) # and so should columns
		for y in range(9):
			# print x,y,len(sudo[x]),len(sudo)
			if sudo[x][y] != 0:
				s.add(m[x][y] == sudo[x][y]) 	# set the given values
			s.add(And(m[x][y] <= 9,m[x][y] >= 1)) # set a max and min value

	for x in range(0,9,3):
		for y in range(0,9,3):
			s.add(Distinct([m[x+i][y+j] for i, j in itertools.product(range(3), range(3))])) # values should be distinct also in groups

	if s.check() == sat: # check if it's true
		mod = s.model()
		r = ""
		for x in range(9):
			r += "".join([str(mod.evaluate(m[x][y])) for y in range(9) ]) + '\n'
		else:
			result.append(r)
	else:
		print "Failed to solve"


print math.fsum([int(a[:3]) for a in result])





# Relics of a simpler time

# class Sudoku():
# 	"""docstring for Sudoku"""

# 	def __init__(self, sudo):
# 		self.raw = sudo
# 		self.score = []

# 	def __str__(self):
# 		for row in self.raw:
# 			print row
# 		return ''

# 	def quads(self):
# 		l = [ self.raw[:3], self.raw[3:6], self.raw[6:]]
# 		quads = [[[],[],[]],[[],[],[]],[[],[],[]]]
# 		for y in range(3):
# 			for x in range(3):
# 				for l_m in l[y]:
# 					quads[y][x].extend(l_m[3*x:3*x+3])
# 		return quads

# 	def scores(self,compute=True):
# 		if compute:
# 			oriz_score = [r.count(0) for r in self.raw]
# 			vert_score = [[r[i] for r in self.raw].count(0) for i in range(9)]
# 			quad_score = [[a.count(0) for a in r] for r in self.quads()]
# 			scores = [[[] for a in range(9)] for i in range(9)]
# 			for y in range(9):
# 				for x in range(9):
# 					if self.raw[y][x] != 0:
# 						scores[y][x] = 0
# 					else:
# 						scores[y][x] = oriz_score[y] + vert_score[x] + quad_score[int(math.floor(x/3))][int(math.floor(y/3))]
# 			for s in scores: print s

# 	def alt_scores(self,matrix=0):
# 		if matrix == 0:
# 			matrix = self.raw
# 		scores = [[0 for a in range(9)] for i in range(9)]
# 		for y in range(9):
# 			for x in range(9):
# 				if matrix[y][x] == 0:
# 					for i in range(1,10):
# 						matrix[y][x] = i
# 						if self.check(matrix) == 0:
# 							scores[y][x] += 1
# 						matrix[y][x] = 0
# 		self.print_matrix(scores,title='Scores')



# 	def check(self,matrix=0):
# 		nums = range(1,10)
# 		ret = 0

# 		if matrix == 0:
# 			matrix = self.raw

# 		def checkSeries(s):
# 			ret = 0
# 			if math.fsum(s) <= 45: # sum of all digits
# 				for z in range(1,10): 
# 					if s.count(z) > 1:
# 						ret += 1
# 			else:
# 				ret+=1
# 			return ret

# 		for u in matrix:
# 			ret += checkSeries(u)

# 		for u in [[r[i] for r in matrix] for i in range(9)]:
# 			ret += checkSeries(u)

# 		for a in self.quads():
# 				for u in a:
# 					ret += checkSeries(u)

# 		if ret == True:
# 			return Z3_L_TRUE
# 		else:
# 			return Z3_L_FALSE

# 	def is_solved(self):
# 		for y in range(9):
# 			for x in range(9):
# 				if self.raw[y][x] == 0:
# 					return False
# 		return True

# 	def solve(self):
# 		nums = set(range(1,10))
# 		while True:
# 			miss_y = [] #rows
# 			miss_x = [] #columns
# 			miss_q = [[[],[],[]],[[],[],[]],[[],[],[]]] #quads
# 			for y in self.raw:
# 				miss_y.append(list(nums - set(y)))
# 			for x in [[r[i] for r in self.raw] for i in range(9)]:
# 				miss_x.append(list(nums - set(x)))
# 			for y,a in enumerate(self.quads()):
# 				for x,q in enumerate(a):
# 					miss_q[y][x] = list(nums - set(q))

# 			n = 0

# 			for y in range(9):
# 				for x in range(9):
# 					m = set.intersection(set(miss_q[int(math.floor(y/3))][int(math.floor(x/3))]),set(miss_y[y]),set(miss_x[x]))
# 					if len(m) == 1 and self.raw[y][x] == 0:
# 						self.raw[y][x] = list(m)[0]
# 						print y,x,m
# 						n += 1

# 			for y in self.raw:
# 				if n > 0:
# 					if y.count(0) > 0:
# 						break
# 			else:
# 				return self

# 	def randomTry(self):
# 		while True:
# 			matrix = self.raw
# 			for y in range(9):
# 				for x in range(9):
# 					if matrix[y][x] == 0:
# 						while True:
# 							matrix[y][x] = random.randint(1,9)
# 							if self.check(matrix) == 0:
# 								break
# 			if self.check(matrix) == 0:
# 				print matrix
# 				print "done"
# 				break

# 	def print_matrix(self,matrix=0,title=''):
# 		if matrix == 0:
# 			matrix = self.raw

		
# 		print '\n' + title + '\n'

# 		for y in range(9):
# 			s = ''
# 			for x in range(9):
# 				if matrix[y][x] == 0:
# 					s += '\033[1;38m' + str(matrix[y][x]) + '\033[1;m '
# 				else:
# 					s += '\033[1;32m' + str(matrix[y][x]) + '\033[1;m '
# 			print s





