#lambda expression
#nameless function

'''
def inc(x):
	return x+1
'''

#lambda <arguments> : <expressions>
'''
f = lambda x : x+1

print(f(10))

print(dir()) #here f is still there and the memory is allocated
'''


print((lambda x,y : x+y)(10,y=20))
print(dir())