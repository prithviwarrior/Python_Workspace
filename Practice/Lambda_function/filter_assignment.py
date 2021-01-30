#filter
def inc(i):
	print("received:{}".format(i))
	return i+2
	
def myFilter(func, to_list):
	L2 = []
	for i in to_list:
		L2.append(func(i))
	return L2
	

L1 = [1,2,3,4,5]

result = myFilter(inc,L1)

print(result)

