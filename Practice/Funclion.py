def add(a, b):
	print("before addition")
	a+=1
	b+=1
	return a,b
	
a= 2
b= 3
a, b = add(a, b)
print(a, b)
	