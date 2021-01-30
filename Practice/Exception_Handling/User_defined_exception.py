#Exception Handling
class MyException(Exception):
	def __init__(self, msg):
		self.args = (msg,) #tuple with 1 arg

print("before")	
try:
	a = 10
	b = 10
	if(a == b):
		myEx = MyException("Something went wrong")
		raise myEx
except (ZeroDivisionError, IndexError) as e:
	print("Exception - 1:", e.args )
except MyException as e:
	print("My Exception:", e.args[0] )
else:
	print("In else block")
finally:
	print("Finally block")

print("done")
