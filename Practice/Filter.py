#filter (function, list)
#based on return value, assigns the value
'''
def is_even(i):
	print("received:{}".format(i))
	return(i%2==0)
	
L1 = [1,2,3,4,5,6,7,8,9,10]

L2 = list(filter(is_even,L1))

print(L2)
'''


#filter
'''
def is_even(i):
	print("received:{}".format(i))
	return(i%2==0)
	
L1 = [1,2,3,4,5,6,7,8,9,10]

L2 = list(filter(is_even,L1))

print(L2)
'''


#map
#writes the return value itself
def is_even(i):
	print("received:{}".format(i))
	return(i%2==0)

L1 = [1,2,3,4,5,6,7,8,9,10]

L2 = list(map(is_even,L1))

print(L2)




