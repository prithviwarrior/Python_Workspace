
class Student():
	count=10 #class level variable
	def __init__(self, i):
		self.i = i #object 
		print("Student:: __init__")
		
	def show(self):
		print("Student:: show", self.i)
		
	@classmethod
	def mod_count(cls):
		cls.count = cls.count + 100
		
		
s1 = Student(11)#s1.__init__(s1,11)
print(Student.count)
print(dir())

Student.mod_count()#s1.mod_count(Student)
print(s1.__dict__)
s1.mod_count()

print(s1.__dict__)

print(Student.count)
print(s1.count)
