
class A():
	i = 20
	@classmethod
	def __init__(self):
		self.i = 10
		
class B(A):
	pass
class C(B):
	pass

c = C()
print(c.i)
print(C.i)

