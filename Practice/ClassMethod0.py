class Student():
	count=10 #class level variable
	def __init__(self, i):
		self.i = 5 #object 
		print("Student:: __init__")
		
	def show(self):
		print("Student:: show", self.i)
		
#	@classmethod
	def mod_count(cls):
		cls.count = cls.count + 100
		
		
s1 = Student(11)#s1.__init__(s1,11)
print("s1.i: ", s1.i)
print("s1.count: ", s1.count)
#print("s1.Student: ", s1.Student)
print(dir())
s1.mod_count()
print("s1.count: ", s1.count)
#print("s1.Student: ", s1.Student)
print(s1.__dict__)

Student.mod_count(Student) #s1.mod_count()
print(Student.count)
