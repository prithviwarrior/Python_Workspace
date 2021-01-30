
class Student():
	count=10 #class level variable
	def __init__(self, i):
		self.i = i #object 
		self.__pr = 111 #private variable
		print("Student:: __init__")
		
	def show(self):
		print("Student:: show", self.i)
	
		
		
s1 = Student(11)#s1.__init__(s1,11)
print(s1.i)
print(s1.__dict__)
