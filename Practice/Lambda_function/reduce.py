from functools import reduce
def add(i,j):
	return i+j

L1 = [1,2,3,4,5]

result = reduce(add, L1)

'''
[1,2,3,4,5]
[3,3,4,5]

'''