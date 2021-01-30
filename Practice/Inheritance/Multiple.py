class A():
	def __init__(self):
		print("A: __init__")
		#super().__init__()
		#self.i = 123
		
class B():
	print("B: without __init__ constructor.")
	
	def __init__(self):
		print("B: __init__")
		self.i = 10
		
		
class C(A,B):
	def __init__(self):
		print("C: __init__")
		#self.i = 11
		#super().__init__()
		
		super(A,self).__init__() #B is super of A only in this flow
		super(C,self).__init__() #A is direct super of C
		
c = C()
print("C in i", c.i)
		
		
		
		