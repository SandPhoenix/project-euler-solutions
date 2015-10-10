import itertools as it
import math
import numpy as np
import operator

def unorderedCombinations(objs,spaces): #generates all 30 character string possibilities

	combinations = list(it.combinations_with_replacement(objs,spaces))
	combinations = [c for c in combinations if c.count('L') <= 1 and c.count('A') <= math.ceil((len(c) - c.count('L'))/2)]
	return list(set(combinations))

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def isPrized(comb): #checks if a string is correct

	if comb.count('L') > 1: return False
	absences = 0

	for day in comb:

		if day == 'A': absences += 1
		else: absences = 0

		if absences >= 3: return False

	return True

def calcCombNum(comb): # calculates total number of possibilities per string

	elems = list(set(comb))
	duplicates = []
	for e in elems:
		c = comb.count(e)
		if c > 1: duplicates.append(math.factorial(c))
	
	r = math.factorial(len(comb)) / prod(duplicates)
	print duplicates,r
	return r

def partition(number): # create all possible partitions of an integer [http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning]
	answer = set()
	answer.add((number, ))
	for x in range(1, number):
		for y in partition(number - x):
			answer.add(tuple(sorted((x, ) + y)))
	return answer

def calcPossibilities(comb): #calculates all the valid string grouping possibilities
	group_num = 1
	parts = partition(comb.count('A'))
	correct_num = 0
	for p in parts:
		for elem in p:
			if elem >= 3:
				break
		else:
			correct_num += 1
	print parts,correct_num
	return correct_num


#1918080160
# print len([c for c in orderedCombinations('AOL',4) if isPrized(c) == True])
counts = math.fsum([len(comb) for comb in unorderedCombinations('AOL',30)])
p = math.fsum([calcCombNum(n) for n in unorderedCombinations('AOL',30)])
print counts,p



