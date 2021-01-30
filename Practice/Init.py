class Student():

	def __init__(self, i):
		self.i = i
		print("Stu:__init__")
		
		
	def show(self): #self => s1, i=10
		print("Stu:show", self.i)
		
s1 = Student(111) #s1.__init__(s1)
s1.show() #s1.show(s1) this
#print("i in s1", s1.i)

s2 = Student(222) #s1.__init__(s1)
s2.show()


