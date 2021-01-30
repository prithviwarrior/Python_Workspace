'''
class Number():
	def __init__(self, no):
		self.no = no
		
	def __add__(self, other):
		temp = Number(0)
		
		if (isinstance(other, Number)):
			print("Is Number")
			temp.no = self.no + other.no
			
		else:
			print("Is not Number")
		
			temp.no = self.no + other
		return temp
		
n1 = Number(10)
n2 = Number(20)
print("n1.no :", n1.no)
#n1 + n2 #n1.__add__(self(n1),n2)
#n3 = n1 + n2  
n3 = n1 + 10

print("n3.no :", n3.no)

print("n1.no :", n1.no)
print("n2.no :", n2.no)
'''


class Number():
	def __init__(self, no):
		self.no = no
		
	def __lt__(self, other):
			print("Number.__lt__")
			return self.no < other.no
			
	def __str__(self):
		return("number is :" + str(self.no))
		
	def __call__(self):
		return("number.__call__")
		
		
n1 = Number(10)
n2 = Number(20)
result = n1 > n2 #reflexive nature(output will be reversed)
print(result)
print(n1)#n1.__str__(n1)
print(n1())#n1.__call__(n1)


