
def add(a, b):
	return a+b

'''
def myfilter(f, L):
	while(len(L) > 1):
		a, b = L[0],L[1]
		del(L[0:2])
		L.insert(0, f(a,b))
	return L[0]
'''
def myfilter(f, L):
	while(len(L) > 1):
		L[0:2] = [f(L[0], L[1])]
	return L[0]

L = [1,2,3,4,5,6,7,8,9]
result = myfilter(add, L)
print (result)