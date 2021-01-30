#filter (function, list)
#based on return value, assigns the value

'''
def is_even(i):
	print("received:{}".format(i))
	return(i%2==0)
'''
#filter
'''
L1 = [1,2,3,4,5,6,7,8,9,10]

L2 = list(filter((lambda x : x%2 ==0),L1))

print(L2)
'''

#map
def inc(i, j):
	print("received:{},{}".format(i,j))
	return(i+j)

L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]

L2 = list(map(inc,L1,L2))

print(L2)