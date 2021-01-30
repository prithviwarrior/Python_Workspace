#map
def inc(i):
	print("received:{}".format(i))
	return i+2
	
def myMap(func, to_list):
	L2 = []
	for i in to_list:
		L2.append(func(i))
	return L2
	

L1 = [1,2,3,4,5]

result = myMap(inc,L1)

print(result)

