#Exception Handling
'''
print("before")
try:
	a = 10
	b = 0
	c = a/b
	print(c)
	print("after")
except ZeroDivisionError:
	print("Exception:ZeroDivisionError")
	
print("done")

'''


print("before")
try:
	a = 10
	b = 0
	L = [1,2,3,4,5,6]
	j = j+1
	L[7] = 7
	c = a/b
	print(c)
	print("after")
except (ZeroDivisionError, IndexError) as e:
	print("Exception - 1:", e.args )
	'''	
	except IndexError as e:
		print("Exception:", e.args )
	'''
except Exception as e:
	print("Main Exception:", e.args )
else:
	print("In else block")
finally:
	print("Finally block")

print("done")
