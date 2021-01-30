class A():
	def __init__(self):
		print("A: __init__")
		self.i = 11
		
class B(A):
	print("B: without __init__ constructor.")
	
	def __init__(self):
		print("B: __init__")
		self.i = 11
		
		
class C(B):
	pass
	'''
	def __init__(self):
		print("C: __init__")
		self.i = 11
		'''
c = C()
print("C in i", c.i)
		
		
		
		