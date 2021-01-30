
'''
class Number():
	def __init__(self, no):
		self.no = no
		
	def __add__(self, other):
		print("Number : __add__")
		self.no = self.no + other.no
		
n1 = Number(10)
n2 = Number(20)
print("n1.no :", n1.no)
n1 + n2 #n1.__add__(self(n1),n2)
print("n1.no :", n1.no)

'''

class Number():
	def __init__(self, no):
		self.no = no
		
	def __add__(self, other):
		#print("Number : __add__")
		temp = Number(0)
		temp.no = self.no + other.no
		return temp
		
n1 = Number(10)
n2 = Number(20)
n3 = Number(20)
print("n1.no :", n1.no)
#n1 + n2 #n1.__add__(self(n1),n2)
n3 = n1 + n2  
print("n3.no :", n3.no)

n4 = n1 + n2 + n3  #n1.__add__(n1,(n2.__add__(n2, n3)))
print("n1.no :", n1.no)
print("n2.no :", n2.no)
print("n4.no :", n4.no)

